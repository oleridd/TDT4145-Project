INSERT INTO VognTabel (vognID)
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