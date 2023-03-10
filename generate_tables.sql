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
    CONSTRAINT Togrute_PK1 PRIMARY KEY togRuteID,
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
    CONSTRAINT TogruteForekomst_PK1  PRIMARY KEY togRuteForekomstID,
    CONSTRAINT TogruteForekomst_FK1 FOREIGN KEY (togRuteID) REFERENCES Togrute(togRuteID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

HEi