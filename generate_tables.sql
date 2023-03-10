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


CREATE TABLE OperatorHarVogn (
    operatorID              INTEGER,
    vognID                  INTEGER,
    CONSTRAINT OperatorHarVogn_PK PRIMARY KEY (operatorID, vognID),
    CONSTRAINT OperatorHarVogn_FK FOREIGN KEY (vognID) REFERENCES Operator(operatorID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
) ;     


CRATE TABLE Vogn (
    vognID INTEGER PRIMARY KEY,
    Vogn BIT NOT NULL,
    UNIQUE(VognID)
);


CREATE TABLE SoveVogn (
    vognID                 INTEGER,
    Vogn AS CAST(1 AS BIT) PERSISTED,
    nKupe                  INTEGER,
    nSengPerKupe           Integer,
    CONSTRAINT SoveVogn PRIMARY KEY (vognID),
    Constraint SoveVogn_FK FOREIGN KEY (vognID) REFERENCES Vogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE SitteVogn (
    vognID                 INTEGER,
    Vogn AS CAST(0 AS BIT) PERSISTED,
    nRad                   INTEGER,
    nSeterPerKupe          Integer,
    CONSTRAINT SoveVogn PRIMARY KEY (vognID),
    CONSTRAINT SoveVogn_FK FOREIGN KEY (vognID) REFERENCES Vogn(vognID)
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


CRATE TABLE Kupe (
    vognID              INTEGER,
    kupeNR              INTEGER,
    antallSeng          INTEGER,
    CONSTRAINT Seng_PK PRIMARY KEY (vognID, sengNR),
    CONSTRAINT Seng_FK FOREIGN KEY (vognID) REFERENCES Vogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CRATE TABLE Sete (
    vognID              INTEGER,
    seteNR              INTEGER,
    CONSTRAINT Sete_PK PRIMARY KEY (vognID, seteNR),
    CONSTRAINT Sete_FK FOREIGN KEY (vognID) REFERENCES Vogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CRATE TABLE SitteBillett (
    ordereID            INTEGER,
    togRuteForekomstID  INTEGER,
    vognID              INTEGER,
    seteNR              INTEGER,
    CONSTRAINT SitteBillett_PK PRIMARY KEY(ordereID, togRuteForekomstID),
    CONSTRAINT SitteBillett_FK1 FOREIGN KEY(vognID) REFERENCES Vogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SitteBillett_FK2 FOREIGN KEY(seteNR) REFERENCES Sete(seteNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CRATE TABLE SoveBillett (
    ordereID            INTEGER,
    togRuteForekomstID  INTEGER,
    vognID              INTEGER,
    sengNR              INTEGER,
    CONSTRAINT SoveBillett_PK PRIMARY KEY(ordereID, togRuteForekomstID),
    CONSTRAINT SoveBillett_FK1 FOREIGN KEY(vognID) REFERENCES Vogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SoveBillett_FK2 FOREIGN KEY(sengNR) REFERENCES Seng(sengNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CRATE TABLE Kunde (
    kID                 INTEGER,
    navn                TEXT,
    epost               TEXT,
    CONSTRAINT Kunde_PK PRIMARY KEY (kID)
);


CRATE TABLE KundeOrdere (
    ordereID                INTEGER,
    dato                    DATE,
    kID                     INTEGER,
    CONSTRAINT KundeOrdere_PK PRIMARY KEY (ordereID),
    CONSTRAINT KundeOrdere_FK FOREIGN KEy (kID) REFERENCES Kunde(kID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);