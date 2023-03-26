import numpy as np
from logg_inn import hent_innloggingsinfo
from utility import get_valid_input
from sql_util import hent_stasjonID, hent_alle_stasjonID

from hent_togruter   import hent_togruter, hent_togruteforekomst_info, hent_ankomsttid # Opt 1
from registrer_kunde import registrer_kunde                           # Opt 3

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
    for i, togruteforekomstID in enumerate(togruter):
        print(f"{i+1}.", hent_togruteforekomst_info(int(togruteforekomstID)))



def opt_2():
    """
    Alternativ 2: Søk togruter som går mellom start- og sluttstasjon
    """
    pass


def opt_3():
    """
    Alternativ 3: Registrer deg som kunde
    """
    navn  = get_valid_input("Navn: ",   FEILMELDING, valid_inputs=str)
    epost = get_valid_input("e-post: ", FEILMELDING, valid_inputs=str)
    tlf   = get_valid_input("Tlf: ",    FEILMELDING, valid_inputs=str)
    registrer_kunde(navn, epost, tlf)
    print("Kunde registrer")


def opt_4():
    """
    Alternativ 4: Kjøp billett
    """
    kID  = logg_inn()
    dato = get_valid_input("Avreisedato: ", FEILMELDING, valid_inputs=str)
    


def opt_5():
    """
    Alternativ 5: Få informasjon om ordre og reiser
    """
    kID = logg_inn()


opts_functions = (opt_1, opt_2, opt_3, opt_4, opt_5)


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
    """

    bruker_in = get_valid_input(
        input_prompt=input_prompt,
        error_message=FEILMELDING,
        valid_inputs=('1', '2', '3', '4', '5')
    )
    
    opts_functions[int(bruker_in)-1]()