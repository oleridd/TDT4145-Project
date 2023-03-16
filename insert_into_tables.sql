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




