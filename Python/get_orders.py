import sqlite3 as sql
from datetime import datetime

def get_all_tickets_for_person(kID: int):

    """
    Denne funksjonen returnerer en liste med lister hvor hver liste inneholder informasjon om en reise.
    """

    today = datetime.today().strftime('%d-%m-%Y')
    print(today)
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor() #Remember to change the limitation of date
        cursor.execute("""
            CREATE TEMPORARY TABLE my_table AS
            SELECT ordereID, dato
            FROM KundeOrdere
            WHERE kID = (:kID) and dato >= (:today); 
        """,
        {'kID': kID, 'today': today}
        )
        cursor.execute("""
            CREATE TEMPORARY TABLE fremtidige_sitte_billetter AS
            SELECT vognID, seteNR, togruteForekomstID, delStrekningID, dato
            FROM SitteBillett NATURAL JOIN my_table NATURAL JOIN SitteBillettPaaDelStrekning;
        """)
        cursor.execute("""
            CREATE TEMPORARY TABLE fremtidig_sitte AS
            SELECT *
            FROM fremtidige_sitte_billetter
            WHERE(delStrekningID = (SELECT MAX(delStrekningID) from fremtidige_sitte_billetter) or delStrekningID = (SELECT MIN(delStrekningID) from fremtidige_sitte_billetter))
            ORDER BY delStrekningID;
        """)
        cursor.execute("""
            CREATE TEMPORARY TABLE fremtidig_sitte_2 AS
            SELECT fremtidig_sitte.*, Delstrekning.startStasjonID, Delstrekning.endeStasjonID
            FROM fremtidig_sitte NATURAL JOIN Delstrekning
        """)
        cursor.execute("""
            CREATE TEMPORARY TABLE fremtidig_sitte_3 AS
            SELECT fremtidig_sitte_2.*, StoppPaa.avgang AS startAvgang, StoppPaa.ankomst AS startAnkomst
            FROM fremtidig_sitte_2 INNER JOIN StoppPaa ON (startStasjonID = stasjonID and fremtidig_sitte_2.togruteForekomstID = StoppPaa.togruteForekomstID)
        """)
        cursor.execute("""
            CREATE TEMPORARY TABLE fremtidig_sitte_4 AS
            SELECT fremtidig_sitte_3.*, StoppPaa.avgang AS endeAvgang, StoppPaa.ankomst AS endeAnkomst
            FROM fremtidig_sitte_3 INNER JOIN StoppPaa ON (endeStasjonID = stasjonID and fremtidig_sitte_3.togruteForekomstID = StoppPaa.togruteForekomstID)
        """)
        cursor.execute("""
            SELECT *
            FROM fremtidig_sitte_4
        """)

    my_table = cursor.fetchall()
    
    my_table = [list(t) for t in my_table]

    #Legger til informasjon om sitte billetter i final_tabel
    final_table = []
    #print(final_table)
    for i in range(int(len(my_table)/2)):
        if(my_table[2*i][7] < my_table[2*i + 1][7] or my_table[2*i][4] < my_table[2*i + 1][4]):
            final_table.append([my_table[2*i][0], my_table[2*i][1], my_table[2*i][4], my_table[2*i][5], my_table[2*i][7], my_table[2*i + 1][6], my_table[2*i + 1][10], "sitte billett"])
        else:
            final_table.append([my_table[2*i][0], my_table[2*i][1], my_table[2*i][4], my_table[2*i + 1][5], my_table[2*i + 1][7], my_table[2*i][6], my_table[2*i][10], "sitte billett"])
    #print(final_table)
    


    #Finner all dataen for sovebiletter.
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor() 
        cursor.execute("""
            CREATE TEMPORARY TABLE my_table2 AS
            SELECT ordereID, dato
            FROM KundeOrdere
            WHERE kID = (:kID) and dato >= (:today); 
        """,
        {'kID': kID, 'today': today}
        )
        cursor.execute("""
            CREATE TEMPORARY TABLE fremtidig_sove_billetter AS
            SELECT vognID, kupeNR, togruteForekomstID, dato
            FROM SoveBillett NATURAL JOIN my_table2;
        """)
        cursor.execute("""
            CREATE TEMPORARY TABLE sove_biletter AS
            SELECT vognID, kupeNR, dato, startStasjonID, avgang, endeStasjonID, ankomst
            FROM fremtidig_sove_billetter INNER JOIN TogruteForekomst ON(fremtidig_sove_billetter.togRuteForekomstID = TogruteForekomst.togRuteForekomstID)
        """)
        cursor.execute("""
            SELECT *
            FROM sove_biletter
        """)
        

    my_table = cursor.fetchall()

    
    my_table = [list(t) for t in my_table]

    for i in range(len(my_table)):
        my_table[i].append("kupe billett")
        final_table.append(my_table[i])

    for i in range(len(final_table)):
        start_stasjon = final_table[i][3]
        ende_stasjon = final_table[i][5]
        cursor.execute("""
            SELECT navn
            FROM Stasjon
            WHERE stasjonID = (:start_stasjon)
        """,
        {'start_stasjon': start_stasjon}
        )
        start_stasjon = str(cursor.fetchall()[0][0])
        final_table[i][3] = start_stasjon
        cursor.execute("""
            SELECT navn
            FROM Stasjon
            WHERE stasjonID = (:ende_stasjon)
        """,
        {'ende_stasjon': ende_stasjon}
        )
        ende_stasjon = str(cursor.fetchall()[0][0])
        final_table[i][5] = ende_stasjon

        vognNR = final_table[i][0]
        cursor.execute("""
            SELECT vognNR
            FROM VognITog
            WHERE vognID = (:vognNR)
        """,
        {'vognNR': vognNR}
        )
        final_table[i][0] = str(cursor.fetchall()[0][0])

    #Jeg tror final_table inneholder alle informasjon vi er ute etter for sitte biletter.
    #Dataen kommer på formen vognNR, seteNR, Dato, startStasjon, startAvgang, sluttStasjon, endeAnkomst
    #Dette er vell all informasjonen som er relevant for sitte biletter.

    now = datetime.now()
    print(now)

    for i in range(len(final_table)):
        if(final_table[i][2] == today and final_table[i][6] > final_table[i][4] and final_table[i][6] < now):
            del final_table[i]


    return final_table
