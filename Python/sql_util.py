import sqlite3 as sql
import numpy as np


def hent_alle_stasjonID() -> np.ndarray:
    """
    Henter ID på alle stasjoner.
    """
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT stasjonID
            FROM Stasjon
        """)
        return np.array(cursor.fetchall()).flatten()


def hent_stasjonID(stasjonnavn: str) -> int:
    """
    Henter stasjonID gitt navn på en stasjon.
    Denne funksjonen antar at alle stasjoner har unike navn.
    """
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT stasjonID
            FROM Stasjon
            WHERE navn = (:stasjonnavn)
        """,
        {'stasjonnavn': stasjonnavn}
        )
        stasjonID = np.array(cursor.fetchall())
    
    if len(stasjonID) > 1:
        raise RuntimeError("Fant ikke unik stasjon")
    else: 
        return int(stasjonID[0])
    

def reset_database() -> None:
    """
    Resets the database
    """
    with sql.connect("Jernbanenett.db") as con:
        cursor = con.cursor()
        cursor.execute("""
/* Creation */
CREATE TABLE Stasjon (
    stasjonID    INTEGER,
    navn         VARCHAR(30),
    moh          DECIMAL,
    CONSTRAINT Stasjon_PK PRIMARY KEY (stasjonID)
);


CREATE TABLE Delstrekning (
    delStrekningID    INTEGER,
    startStasjonID     INTEGER,
    endeStasjonID      INTEGER,
    lengde             INTEGER,
    sporType          TEXT,
    CONSTRAINT Delstrekning_PK PRIMARY KEY (delStrekningID),
    CONSTRAINT Delstrekning_FK1 FOREIGN KEY (startStasjonID) REFERENCES Stasjon(stasjonID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Delstrekning_FK2 FOREIGN KEY (endeStasjonID) REFERENCES Stasjon(stasjonID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Banestrekning (
    baneStrekningID     INTEGER,
    forsteStrekning     INTEGER,
    sisteStrekning      INTEGER,
    navn                TEXT,
    fremdriftEnergi     TEXT,
    erHovedrettning     BOOLEAN,
    CONSTRAINT Banestrekning_PK PRIMARY KEY (baneStrekningID),
    CONSTRAINT Banestrekning_FK1 FOREIGN KEY (forsteStrekning) REFERENCES Delstrekning(DelstrekningID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Banestrekning_FK2 FOREIGN KEY (sisteStrekning) REFERENCES Delstrekning(DelstrekningID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE StrekningPaaBanestrekning (
    baneStrekningID     INTEGER,
    delStrekningID      INTEGER,
    CONSTRAINT StrekningPaaBanestrekning_PK1  PRIMARY KEY (baneStrekningID, delStrekningID),
    CONSTRAINT StrekningPaaBanestrekning_FK1 FOREIGN KEY (baneStrekningID) REFERENCES Banestrekning(BanestrekningID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT StrekningPaaBanestrekning_FK2 FOREIGN KEY (delStrekningID) REFERENCES Delstrekning(delStrekningID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Togrute (
    togRuteID    		INTEGER,
	baneStrekningID		INTEGER,
	operatorID			INTEGER,
    CONSTRAINT Togrute_PK1 PRIMARY KEY (togRuteID),
    CONSTRAINT Togrute_FK1 FOREIGN KEY (baneStrekningID) REFERENCES Banestrekning(BanestrekningID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Togrute_FK2 FOREIGN KEY (operatorID) REFERENCES Operator(operatorID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE TogruteForekomst (
    togruteForekomstID     INTEGER,
	togRuteID			   INTEGER,
	ukedag		           TEXT,
	startStasjonID		   INTEGER,
	avgang				   TIME,
	endeStasjonID		   INTEGER,
	ankomst			       TIME,
    CONSTRAINT TogruteForekomst_PK1 PRIMARY KEY (togRuteForekomstID),
    CONSTRAINT TogruteForekomst_FK1 FOREIGN KEY (togRuteID) REFERENCES Togrute(togRuteID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT TogruteForekomst_FK2 FOREIGN KEY (startStasjonID) REFERENCES Stasjon(stasjonID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT TogruteForekomst_FK3 FOREIGN KEY (endeStasjonID) REFERENCES Stasjon(stasjonID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE StoppPaa (
	togruteForekomstID		INTEGER,
	stasjonID				INTEGER,
	ankomst					TIME,
	avgang				    TIME,
    dagNr                   INTEGER,
	CONSTRAINT StoppPaa_PK PRIMARY KEY (togruteForekomstID, stasjonID),
	CONSTRAINT StoppPaa_FK1 FOREIGN KEY (togruteForekomstID) REFERENCES Togruteforekomst(togruteForekomstID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT StoppPaa_FK2 FOREIGN KEY (stasjonID) REFERENCES Stasjon(stasjonID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


CREATE TABLE Operator (
    operatorID              INTEGER,
    navn                    INTEGER,
    CONSTRAINT Operator_PK PRIMARY KEY (operatorID)
);

CREATE TABLE VognTable (
    vognID          INTEGER,
    CONSTRAINT VognTable PRIMARY KEY (vognID)
);

CREATE TABLE SoveVogn (
    vognID                 INTEGER,
    nKupe                  INTEGER,
    nSengPerKupe           INTEGER,
    CONSTRAINT SoveVogn_PK PRIMARY KEY (vognID),
    CONSTRAINT SoveVogn_FK FOREIGN KEY (vognID) REFERENCES VognTable(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE SitteVogn (
    vognID                 INTEGER,
    nRad                   INTEGER,
    nSeterPerKupe          INTEGER,
    CONSTRAINT SitteVogn_PK PRIMARY KEY (vognID),
    CONSTRAINT SitteVong_FK FOREIGN KEY (vognID) REFERENCES VognTable(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE OperatorHarVogn (
    operatorID     INTEGER,
    vognID         INTEGER,
    CONSTRAINT OperatorHarVogn_PK1  PRIMARY KEY (operatorID, vognID),
    CONSTRAINT OperatorHarVogn_FK1 FOREIGN KEY (operatorID) REFERENCES Operator(operatorID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT OperatorHarVogn_FK2 FOREIGN KEY (vognID) REFERENCES SoveVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE VognITog (
    vognID                  INTEGER,
    togRuteID               INTEGER,
    vognNr                  INTEGER,
    CONSTRAINT VognITog_PK PRIMARY KEY (vognID, togRuteID),
    CONSTRAINT VognITog_FK1 FOREIGN KEY (vognID) REFERENCES VognTable(vognID)
        ON  UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT VognITog_FK2 FOREIGN KEY (togRuteID) REFERENCES Togrute(togRuteID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Kupe (
    vognID              INTEGER,
    kupeNR              INTEGER,
    CONSTRAINT Kupe_PK PRIMARY KEY (vognID, kupeNR),
    CONSTRAINT Kupe_FK FOREIGN KEY (vognID) REFERENCES SoveVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Sete (
    vognID              INTEGER,
    seteNR              INTEGER,
    CONSTRAINT Sete_PK PRIMARY KEY (vognID, seteNR),
    CONSTRAINT Sete_FK FOREIGN KEY (vognID) REFERENCES SitteVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE SitteBillett (
    ordereID            INTEGER,
	billettNR			INTEGER,
    vognID              INTEGER,
    seteNR              INTEGER,
    togruteForekomstID  INTEGER,
	Reisedato			DATE,
    CONSTRAINT SitteBillett_PK PRIMARY KEY(ordereID, billettNR),
    CONSTRAINT SitteBillett_FK1 FOREIGN KEY(vognID) REFERENCES SitteVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SitteBillett_FK2 FOREIGN KEY(vognID, seteNR) REFERENCES Sete(vognID, seteNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SitteBillett_FK3 FOREIGN KEY(togruteForekomstID) REFERENCES Togruteforekomst(togruteForekomstID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE SoveBillett (
    ordereID            INTEGER,
	billettNR			INTEGER,
    vognID              INTEGER,
    kupeNR              INTEGER,
    togruteForekomstID  INTEGER,
	Reisedato			DATE,
    antallSeng          INT,
    CONSTRAINT SoveBillett_PK PRIMARY KEY(ordereID, billettNR),
    CONSTRAINT SoveBillett_FK1 FOREIGN KEY(vognID) REFERENCES SoveVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SoveBillett_FK2 FOREIGN KEY(vognID, kupeNR) REFERENCES Kupe(vognID, kupeNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SoveBillett_FK3 FOREIGN KEY(togruteForekomstID) REFERENCES Togruteforekomst(togruteForekomstID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Kunde (
    kID                 INTEGER,
    navn                TEXT,
    epost               TEXT UNIQUE,
    mobilnummer         INTEGER UNIQUE,
    CONSTRAINT Kunde_PK PRIMARY KEY (kID)
);


CREATE TABLE KundeOrdere (
    ordereID                INTEGER,
    dato                    DATE,
    kID                     INTEGER,
    CONSTRAINT KundeOrdere_PK PRIMARY KEY (ordereID),
    CONSTRAINT KundeOrdere_FK FOREIGN KEy (kID) REFERENCES Kunde(kID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE SitteBillettPaaDelStrekning (
    delStrekningID          INTEGER,
    ordereID                INTEGER,
    billettNr               INTEGER,
    CONSTRAINT SitteBillettPaaDelStrekning_PK PRIMARY KEY (delStrekningID, ordereID, billettNr),
    CONSTRAINT SitteBillettPaaDelStrekning_FK1 FOREIGN KEY (delStrekningID) REFERENCES Delstrekning(delStrekningID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SitteBillettPaaDelStrekning_FK2 FOREIGN KEY (ordereID, billettNR) REFERENCES SitteBillett(ordereID, billettNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


/* Inserting */
INSERT INTO VognTable (vognID)
VALUES
(1),
(2),
(3),
(4),
(5);

INSERT INTO SitteVogn (vognID, nRad, nSeterPerKupe)
VALUES 
(1, 3, 4),
(2, 3, 4),
(3, 3, 4),
(4, 3, 4);

INSERT INTO Sete (VognID, SeteNR)
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),

(2, 1),
(2, 2),
(2, 3),
(2, 4),
(2, 5),
(2, 6),
(2, 7),
(2, 8),
(2, 9),
(2, 10),
(2, 11),
(2, 12),

(3, 1),
(3, 2),
(3, 3),
(3, 4),
(3, 5),
(3, 6),
(3, 7),
(3, 8),
(3, 9),
(3, 10),
(3, 11),
(3, 12),

(4, 1),
(4, 2),
(4, 3),
(4, 4),
(4, 5),
(4, 6),
(4, 7),
(4, 8),
(4, 9),
(4, 10),
(4, 11),
(4, 12);

INSERT INTO SoveVogn (vognID, nKupe, nSengPerKupe)
VALUES
(5, 4, 2);

INSERT INTO Stasjon (stasjonID, navn, moh)
VALUES 
(1, "Bodo", 4.1),
(2, "Fauske", 34.0),
(3, "Mo i Rana", 3.5),
(4, "Mosjoen", 6.8),
(5, "Steinkjer", 3.6),
(6, "Trondheim", 5.1);


INSERT INTO Delstrekning (delstrekningID, startStasjonID, endeStasjonID, lengde, sporType)
VALUES 
(1, 1, 2, 60, "enkeltspor"),
(2, 2, 1, 60, "enkeltspor"),
(3, 2, 3, 170, "enkeltspor"),
(4, 3, 2, 170, "enkeltspor"),
(5, 3, 4, 90, "enkeltspor"),
(6, 4, 3, 90, "enkeltspor"),
(7, 4, 5, 280, "enkeltspor"),
(8, 5, 4, 280, "enkeltspor"),
(9, 5, 6, 120, "dobbeltspor"),
(10, 6, 5, 120, "dobbeltspor");

INSERT INTO Kupe (VognID, KupeNR)
VALUES
(5, 1),
(5, 2),
(5, 3),
(5, 4);

INSERT INTO Operator (operatorID, navn)
VALUES 
(1, "SJ");


INSERT INTO Banestrekning (baneStrekningID, forsteStrekning, sisteStrekning, navn, fremdriftEnergi, erHovedrettning)
VALUES
(1, 1, 9, "Nordlandsbanen", "diesel", FALSE),
(2, 10, 2, "Nordlandsbanen", "diesel", TRUE);

INSERT INTO StrekningPaaBanestrekning (baneStrekningID, delStrekningID)
VALUES
(1, 1), /* Har lagt inn første her... */
(1, 3),
(1, 5),
(1, 7),
(1, 9), /* ...og siste her */

(2, 10),
(2, 8),
(2, 6),
(2, 4),
(2, 2);


INSERT INTO Togrute (togRuteID, baneStrekningID, operatorID)
VALUES 
(1, 1, 1),
(2, 2, 1);

INSERT INTO VognITog 
VALUES
(1, 2, 1),
(2, 2, 2), 
(3, 2, 1),
(5, 2, 2),
(4, 1, 1);

INSERT INTO TogruteForekomst (togruteForekomstID, togRuteID, ukedag, startStasjonID, avgang, endeStasjonID, ankomst)
VALUES
(1, 2, "mandag", 6, '07:49:00', 1, '17:34:00'),
(2, 2, "tirsdag", 6, '07:49:00', 1, '17:34:00'),
(3, 2, "onsdag", 6, '07:49:00', 1, '17:34:00'),
(4, 2, "torsdag", 6, '07:49:00', 1, '17:34:00'),
(5, 2, "fredag", 6, '07:49:00', 1, '17:34:00'),
(6, 2, "mandag", 6, '23:05:00', 1, '09:05:00'),
(7, 2, "tirsdag", 6, '23:05:00', 1, '09:05:00'),
(8, 2, "onsdag", 6, '23:05:00', 1, '09:05:00'),
(9, 2, "torsdag", 6, '23:05:00', 1, '09:05:00'),
(10, 2, "fredag", 6, '23:05:00', 1, '09:05:00'),
(11, 2, "lørdag", 6, '23:05:00', 1, '09:05:00'),
(12, 2, "søndag", 6, '23:05:00', 1, '09:05:00'),
(13, 1, "mandag", 3, '08:11:00', 6, '14:13:00'),
(14, 1, "tirsdag", 3, '08:11:00', 6, '14:13:00'),
(15, 1, "onsdag", 3, '08:11:00', 6, '14:13:00'),
(16, 1, "torsdag", 3, '08:11:00', 6, '14:13:00'),
(17, 1, "fredag", 3, '08:11:00', 6, '14:13:00');

INSERT INTO StoppPaa
VALUES
/* Antar at hvert tog blir på stasjonen i 2 min */
(1, 6, NULL, '07:49:00', 0),
(1, 5, '09:51:00', '09:53:00', 0), 
(1, 4, '13:20:00', '13:22:00', 0),
(1, 3, '14:31:00', '14:33:00', 0),
(1, 2, '16:49:00', '16:51:00', 0),
(1, 1, '17:34:00', NULL, 0),

(2, 6, NULL, '07:49:00', 0),
(2, 5, '09:51:00', '09:53:00', 0), 
(2, 4, '13:20:00', '13:22:00', 0),
(2, 3, '14:31:00', '14:33:00', 0),
(2, 2, '16:49:00', '16:51:00', 0),
(2, 1, '17:34:00', NULL, 0),

(3, 6, NULL, '07:49:00', 0),
(3, 5, '09:51:00', '09:53:00', 0), 
(3, 4, '13:20:00', '13:22:00', 0),
(3, 3, '14:31:00', '14:33:00', 0),
(3, 2, '16:49:00', '16:51:00', 0),
(3, 1, '17:34:00', NULL, 0),

(4, 6, NULL, '07:49:00', 0),
(4, 5, '09:51:00', '09:53:00', 0), 
(4, 4, '13:20:00', '13:22:00', 0),
(4, 3, '14:31:00', '14:33:00', 0),
(4, 2, '16:49:00', '16:51:00', 0),
(4, 1, '17:34:00', NULL, 0),

(5, 6, NULL, '07:49:00', 0),
(5, 5, '09:51:00', '09:53:00', 0), 
(5, 4, '13:20:00', '13:22:00', 0),
(5, 3, '14:31:00', '14:33:00', 0),
(5, 2, '16:49:00', '16:51:00', 0),
(5, 1, '17:34:00', NULL, 0),


(6, 6, NULL, '23:05:00', 0),
(6, 5, '00:57:00', '00:59:00', 1),
(6, 4, '04:41:00', '04:43:00', 1),
(6, 3, '05:55:00', '05:57:00', 1),
(6, 2, '08:19:00', '08:21:00', 1),
(6, 1, '09:05:00', NULL, 1),

(7, 6, NULL, '23:05:00', 0),
(7, 5, '00:57:00', '00:59:00', 1),
(7, 4, '04:41:00', '04:43:00', 1),
(7, 3, '05:55:00', '05:57:00', 1),
(7, 2, '08:19:00', '08:21:00', 1),
(7, 1, '09:05:00', NULL, 1),

(8, 6, NULL, '23:05:00', 0),
(8, 5, '00:57:00', '00:59:00', 1),
(8, 4, '04:41:00', '04:43:00', 1),
(8, 3, '05:55:00', '05:57:00', 1),
(8, 2, '08:19:00', '08:21:00', 1),
(8, 1, '09:05:00', NULL, 1),

(9, 6, NULL, '23:05:00', 0),
(9, 5, '00:57:00', '00:59:00', 1),
(9, 4, '04:41:00', '04:43:00', 1),
(9, 3, '05:55:00', '05:57:00', 1),
(9, 2, '08:19:00', '08:21:00', 1),
(9, 1, '09:05:00', NULL, 1),

(10, 6, NULL, '23:05:00', 0),
(10, 5, '00:57:00', '00:59:00', 1),
(10, 4, '04:41:00', '04:43:00', 1),
(10, 3, '05:55:00', '05:57:00', 1),
(10, 2, '08:19:00', '08:21:00', 1),
(10, 1, '09:05:00', NULL, 1),

(11, 6, NULL, '23:05:00', 0),
(11, 5, '00:57:00', '00:59:00', 1),
(11, 4, '04:41:00', '04:43:00', 1),
(11, 3, '05:55:00', '05:57:00', 1),
(11, 2, '08:19:00', '08:21:00', 1),
(11, 1, '09:05:00', NULL, 1),

(12, 6, NULL, '23:05:00', 0),
(12, 5, '00:57:00', '00:59:00', 1),
(12, 4, '04:41:00', '04:43:00', 1),
(12, 3, '05:55:00', '05:57:00', 1),
(12, 2, '08:19:00', '08:21:00', 1),
(12, 1, '09:05:00', NULL, 1),

(13, 1, NULL, '08:11:00', 0),
(13, 2, '09:14:00', '09:16:00', 0),
(13, 3, '12:31:00', '12:22:00', 0),
(13, 4, '14:31:00', NULL, 0),

(14, 1, NULL, '08:11:00', 0),
(14, 2, '09:14:00', '09:16:00', 0),
(14, 3, '12:31:00', '12:22:00', 0),
(14, 4, '14:31:00', NULL, 0),

(15, 1, NULL, '08:11:00', 0),
(15, 2, '09:14:00', '09:16:00', 0),
(15, 3, '12:31:00', '12:22:00', 0),
(15, 4, '14:31:00', NULL, 0),

(16, 1, NULL, '08:11:00', 0),
(16, 2, '09:14:00', '09:16:00', 0),
(16, 3, '12:31:00', '12:22:00', 0),
(16, 4, '14:31:00', NULL, 0),

(17, 1, NULL, '08:11:00', 0),
(17, 2, '09:14:00', '09:16:00', 0),
(17, 3, '12:31:00', '12:22:00', 0),
(17, 4, '14:31:00', NULL, 0);
        """)