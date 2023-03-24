import numpy as np
from logg_inn import hent_innloggingsinfo

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
    input_er_gyldig = False
    print("E-post eller tlf: ")

    while not input_er_gyldig:
        bruker_in = input()
        kID = hent_innloggingsinfo(bruker_in)
        if kID == -1:
            print("Ugyldig input")
        else:
            input_er_gyldig = True
        
    return kID


def opt_1():
    """
    Alternativ 1: Sjekk togruter på din stasjon for en gitt ukedag
    """
    pass


def opt_2():
    """
    Alternativ 2: Søk togruter som går mellom start- og sluttstasjon
    """
    pass


def opt_3():
    """
    Alternativ 3: Registrer deg som kunde
    """
    pass


def opt_4():
    """
    Alternativ 4: Kjøp billett
    """
    kID = logg_inn()


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
    # Input:
    print("""
            Vennligst velg alternativ:
            1. Sjekk togruter på din stasjon for en gitt ukedag
            2. Søk togruter som går mellom start- og sluttstasjon
            3. Registrer deg som kunde
            4. Kjøp billett
            5. Få informasjon om ordre og reiser
        """)
    input_er_gyldig = False
    while not input_er_gyldig:
        bruker_in = input()
        try:
            input_er_gyldig = np.any([int(bruker_in) == i+1 for i in range(5)])
        except ValueError:
            pass

        if not input_er_gyldig:
            print("Ugyldig input")
    
    # Videre delegering:
    opts_functions[int(bruker_in)-1]()