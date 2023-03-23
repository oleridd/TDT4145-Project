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
	avgang					TIME,
	ankomst					TIME,
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
    CONSTRAINT VognTabel PRIMARY KEY (vognID)
);

CREATE TABLE SoveVogn (
    vognID                 INTEGER,
    nKupe                  INTEGER,
    nSengPerKupe           INTEGER,
    CONSTRAINT SoveVogn_PK PRIMARY KEY (vognID),
    CONSTRAINT SoveVogn_FK FOREIGN KEY (vognID) REFERENCES VognTabel(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE SitteVogn (
    vognID                 INTEGER,
    nRad                   INTEGER,
    nSeterPerKupe          INTEGER,
    CONSTRAINT SitteVogn_PK PRIMARY KEY (vognID),
    CONSTRAINT SitteVong_FK FOREIGN KEY (vognID) REFERENCES VognTabel(vognID)
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
    togruteForekomstID  INTEGER,
	Reisedato			DATE,
    CONSTRAINT SitteBillett_PK PRIMARY KEY(ordereID, billettNR),
    CONSTRAINT SitteBillett_FK1 FOREIGN KEY(vognID) REFERENCES SitteVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SitteBillett_FK2 FOREIGN KEY(seteNR) REFERENCES Sete(seteNR)
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
    CONSTRAINT SoveBillett_PK PRIMARY KEY(ordereID, billettNR),
    CONSTRAINT SoveBillett_FK1 FOREIGN KEY(vognID) REFERENCES SoveVogn(vognID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SoveBillett_FK2 FOREIGN KEY(kupeNR) REFERENCES Kupe(kupeNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SoveBillett_FK3 FOREIGN KEY(togruteForekomstID) REFERENCES Togruteforekomst(togruteForekomstID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE Kunde (
    kID                 INTEGER,
    navn                TEXT,
    epost               TEXT,
    mobilnummer         INTEGER,
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
    CONSTRAINT SitteBillettPaaDelStrekning_FK2 FOREIGN KEY (ordereID) REFERENCES KundeOrdere(ordereID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT SitteBillettPaaDelStrekning_FK3 FOREIGN KEY (billettNR) REFERENCES SitteBillett(billettNR)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);