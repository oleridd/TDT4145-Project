import numpy as np
from logg_inn import hent_innloggingsinfo
from utility import get_valid_input, get_weekday_from_date
from sql_util import hent_stasjonID, hent_alle_stasjonID, hent_banestrekning, hent_delstrekninger_mellom_stasjoner, reset_database
from get_orders import get_all_tickets_for_person

from hent_togruter   import hent_togruter, hent_generell_togruteforekomst_info # Opt 1
from TrainRoutes import get_train_routes_at_date                               # Opt 2
from registrer_kunde import registrer_kunde                                    # Opt 3
from kjop_billett import hent_ledige_billetter, hent_vognNr                    # Opt 4

FEILMELDING = "Ugyldig input"

def logg_inn() -> int:
    """
    Innlogging for kunder, for de funksjonene som krever dette.
    Antagelse for simplifikasjon: En kunde er unikt identifisert
    av e-post eller tlf.

    Argumenter:
        None
    Returnerer:
        kID for den innloggede kunden
    """
    kID = get_valid_input(
        input_prompt="E-post eller tlf: ",
        error_message=FEILMELDING,
        input_transform=hent_innloggingsinfo,
        invalid_inputs=[-1]
    )

    return kID


def opt_1():
    """
    Alternativ 1: Sjekk togruter på din stasjon for en gitt ukedag
    """
    stasjonID = get_valid_input(
        input_prompt="Stasjon: ",
        error_message=FEILMELDING,
        valid_inputs=hent_alle_stasjonID(),
        input_transform=hent_stasjonID
    )

    ukedag = get_valid_input(
        input_prompt="Ukedag: ",
        error_message=FEILMELDING,
        valid_inputs=["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"],
        input_transform=lambda s: s.lower()
    )

    togruter = hent_togruter(stasjonID, ukedag)
    for i, data in enumerate(togruter):
        print(f"{i+1}.", "{} | Avgang fra {}: {} | Ankomst til {}: {} | Dato: ".format(*data))



def opt_2():
    """
    Alternativ 2: Søk togruter som går mellom start- og sluttstasjon
    """
    dato = get_valid_input("Dato: ", FEILMELDING, valid_inputs=str)
    time = get_valid_input("Tid: ", FEILMELDING, valid_inputs=str)
    startStasjonID = get_valid_input(
        input_prompt="Start Stasjon: ",
        error_message=FEILMELDING,
        valid_inputs=hent_alle_stasjonID(),
        input_transform=hent_stasjonID
    )
    endeStasjonID = get_valid_input(
        input_prompt="Ende Stasjon: ",
        error_message=FEILMELDING,
        valid_inputs=hent_alle_stasjonID(),
        input_transform=hent_stasjonID
    )

    togruter = get_train_routes_at_date(dato, time, startStasjonID, endeStasjonID)
    for i, data in enumerate(togruter):
        print(f"{i+1}.", "Avgang fra {}: {} | Ankomst til {}: {} | Dato: {}".format(*data))


def opt_3():
    """
    Alternativ 3: Registrer deg som kunde
    """
    navn  = get_valid_input("Navn: ",   FEILMELDING, valid_inputs=str)
    epost = get_valid_input("e-post: ", FEILMELDING, valid_inputs=str)
    tlf   = get_valid_input("Tlf: ",    FEILMELDING, valid_inputs=str)
    registrer_kunde(navn, epost, tlf)
    print("Kunde registrert")


def opt_4():
    """
    Alternativ 4: Kjøp billett
    """
    kID  = logg_inn()

    # Henter ut togruter som stopper ved stasjonen ved bruk av kode i opt_2:
    dato = get_valid_input(
        "Avreisedato: ",
        FEILMELDING,
        valid_inputs=str
    )

    startstasjonID = get_valid_input(
        input_prompt="Fra: ",
        error_message=FEILMELDING,
        valid_inputs=hent_alle_stasjonID(),
        input_transform=hent_stasjonID
    )

    endestasjonID = get_valid_input(
        input_prompt="Til: ",
        error_message=FEILMELDING,
        valid_inputs=hent_alle_stasjonID(),
        input_transform=hent_stasjonID
    )

    tid = get_valid_input(
        input_prompt="Avreise etter (tt:mm): ",
        error_message=FEILMELDING,
        valid_inputs=str
    )

    IDs, togruter = get_train_routes_at_date(dato, tid, startstasjonID, endestasjonID, id=True)
    
    # Valg av togruteforekomst: 
    print("Velg togruteforekomst:")
    for i, data in enumerate(togruter):
        print(f"{i+1}.", "Avgang fra {}: {} | Ankomst til {}: {} | Dato: {}".format(*data))
    
    togruteforekomstID = get_valid_input(
        input_prompt="Skriv et tall for å indikere togruteforekomst: ",
        error_message=FEILMELDING,
        input_transform=lambda i: IDs[int(i)-1],
        valid_inputs=IDs
    )

    # Henter ut relevante delstrekninger:
    banestrekningID = hent_banestrekning(togruteforekomstID)
    delstrekninger = hent_delstrekninger_mellom_stasjoner(banestrekningID, startstasjonID, endestasjonID)

    # Printer ledige billetter:
    ledige_sovebilletter, ledige_sittebilletter = hent_ledige_billetter(togruteforekomstID, dato, delstrekninger)

    print("\nVelg billett")
    print("Sovebilletter:")
    for i, (vognID, kupeNr) in enumerate(ledige_sovebilletter):
        print(f"{i+1}. ", f"Vogn: {hent_vognNr(vognID)}, Kupe: {kupeNr}")
    
    index_displacement = len(ledige_sovebilletter)
    print("Sittebilletter:")
    for i, (vognID, seteNr) in enumerate(np.unique(ledige_sittebilletter[:, :2], axis=0)):
        print(f"{i+index_displacement+1}. ", f"Vogn: {hent_vognNr(vognID)}, Sete: {seteNr}")
    
    billettvalg = get_valid_input(
        input_prompt="Skriv et tall for å indikere billett: ",
        error_message=FEILMELDING,
        input_transform=int,
        valid_inputs=range(len(ledige_sittebilletter) + len(ledige_sovebilletter) + 1)
    )



def opt_5():
    """
    Alternativ 5: Få informasjon om ordre og reiser
    """
    kID = logg_inn()

    info = get_all_tickets_for_person(kID)
    for i in range(len(info)):
        print(f"{info[i][-1]} i vogn {info[i][0]} med plass nr.{info[i][1]} den {info[i][2]} fra: {info[i][3]} klokken {info[i][4]} til: {info[i][5]} klokken {info[i][6]}.")


opts_functions = (opt_1, opt_2, opt_3, opt_4, opt_5, reset_database)


def hovedmeny() -> None:
    """
    Hovedmenyen for Jernbanenett databasen. Kjøres i en evig while-løkke
    til programmet termineres.
    Representerer funksjonaliteten i oppgave c), d), e), g) og h)
    """

    input_prompt = """
        Vennligst velg alternativ:
            1. Sjekk togruter på din stasjon for en gitt ukedag
            2. Søk togruter som går mellom start- og sluttstasjon
            3. Registrer deg som kunde
            4. Kjøp billett
            5. Få informasjon om ordre og reiser

            6. Reset database
    """

    bruker_in = get_valid_input(
        input_prompt=input_prompt,
        error_message=FEILMELDING,
        valid_inputs=('1', '2', '3', '4', '5', '6')
    )
    
    opts_functions[int(bruker_in)-1]()