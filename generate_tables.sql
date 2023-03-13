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
    CONSTRAINT Delstrekning_PK PRIMARY KEY (delStrekningID),
    CONSTRAINT Delstrekning_FK1 FOREIGN KEY (startStasjonID) REFERENCES Stasjon(stasjonID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Delstrekning_FK2 FOREIGN KEY (endeStasjonID) REFERENCES Stasjon(stasjonID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Banestrekning (
    baneStrekningID    INTEGER,
    forsteStrekning     INTEGER,
    sisteStrekning      INTEGER,
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
    togRuteForekomstID     INTEGER,
	togRuteID			   INTEGER,
	ukedag		           TEXT,
	tidspunkt			   TIME,
    CONSTRAINT TogruteForekomst_PK1  PRIMARY KEY (togRuteForekomstID),
    CONSTRAINT TogruteForekomst_FK1 FOREIGN KEY (togRuteID) REFERENCES Togrute(togRuteID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Operator (
    operatorID              INTEGER,
    navn                    INTEGER,
    CONSTRAINT Operator_PK PRIMARY KEY (operatorID)
);


CREATE TABLE SoveVogn (
    vognID                 INTEGER,
    nKupe                  INTEGER,
    nSengPerKupe           INTEGER,
    CONSTRAINT SoveVogn_PK PRIMARY KEY (vognID)
);

CREATE TABLE SitteVogn (
    vognID                 INTEGER,
    nRad                   INTEGER,
    nSeterPerKupe          INTEGER,
    CONSTRAINT SitteVogn_PK PRIMARY KEY (vognID)
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
    antallSeng          INTEGER,
    CONSTRAINT Kupe_PK PRIMARY KEY (vognID, kupeNR),
    CONSTRAINT Kupe_FK FOREIGN KEY (vognID) REFERENCES SoveVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Sete (
    vognID              INTEGER,
    seteNR              INTEGER,
    CONSTRAINT Sete_PK PRIMARY KEY (vognID, seteNR),
    CONSTRAINT Sete_FK FOREIGN KEY (vognID) REFERENCES SoveVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE SitteBillett (
    ordereID            INTEGER,
	billettNR			INTEGER,
    vognID              INTEGER,
    seteNR              INTEGER,
	Reisedato			DATE,
    CONSTRAINT SitteBillett_PK PRIMARY KEY(ordereID, billettNR),
    CONSTRAINT SitteBillett_FK1 FOREIGN KEY(vognID) REFERENCES SitteVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SitteBillett_FK2 FOREIGN KEY(seteNR) REFERENCES Sete(seteNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE SoveBillett (
    ordereID            INTEGER,
	billettNR			INTEGER,
    vognID              INTEGER,
    kupeNR              INTEGER,
	Reisedato			DATE,
    CONSTRAINT SoveBillett_PK PRIMARY KEY(ordereID, billettNR),
    CONSTRAINT SoveBillett_FK1 FOREIGN KEY(vognID) REFERENCES SoveVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SoveBillett_FK2 FOREIGN KEY(kupeNR) REFERENCES Kupe(kupeNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Kunde (
    kID                 INTEGER,
    navn                TEXT,
    epost               TEXT,
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
    CONSTRAINT SitteBillettPaaDelStrekning_PK PRIMARY KEY (delStrekningID, ordereID, billettNr)
    CONSTRAINT SitteBillettPaaDelStrekning_FK1 FOREIGN KEY (delStrekningID) REFERENCES Delstrekning(delStrekningID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SitteBillettPaaDelStrekning_FK2 FOREIGN KEY (ordereID) REFERENCES KundeOrdere(ordereID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);