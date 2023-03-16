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

INSERT INTO SoveVogn (vognID, nKupe, nSengPerKupe)
VALUES
(5, 4, 2);


INSERT INTO Operator (operatorID, navn)
VALUES 
(1, "SJ");

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