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
(1, 3),
(1, 5),
(1, 7),
(2, 2),
(2, 4),
(2, 6),
(2, 8);


INSERT INTO StoppPaa
VALUES
(1, 2, '00:57:00', '00:57:00'), /* Antar at hvert tog blir på stasjonen i 2 min */
(1, 3, '04:41:00', '04:43:00'),
(1, 4, '05:55:00', '05:57:00'),
(1, 5, '08:19:00', '08:21:00'),

(2, 2, '00:57:00', '00:57:00'),
(2, 3, '04:41:00', '04:43:00'),
(2, 4, '05:55:00', '05:57:00'),
(2, 5, '08:19:00', '08:21:00'),

(3, 2, '00:57:00', '00:57:00'),
(3, 3, '04:41:00', '04:43:00'),
(3, 4, '05:55:00', '05:57:00'),
(3, 5, '08:19:00', '08:21:00'),

(4, 2, '00:57:00', '00:57:00'),
(4, 3, '04:41:00', '04:43:00'),
(4, 4, '05:55:00', '05:57:00'),
(4, 5, '08:19:00', '08:21:00'),

(5, 2, '00:57:00', '00:57:00'),
(5, 3, '04:41:00', '04:43:00'),
(5, 4, '05:55:00', '05:57:00'),
(5, 5, '08:19:00', '08:21:00'),

(6, 2, '00:57:00', '00:57:00'),
(6, 3, '04:41:00', '04:43:00'),
(6, 4, '05:55:00', '05:57:00'),
(6, 5, '08:19:00', '08:21:00'),

(7, 2, '00:57:00', '00:57:00'),
(7, 3, '04:41:00', '04:43:00'),
(7, 4, '05:55:00', '05:57:00'),
(7, 5, '08:19:00', '08:21:00'),

(8, 2, '00:57:00', '00:57:00'),
(8, 3, '04:41:00', '04:43:00'),
(8, 4, '05:55:00', '05:57:00'),
(8, 5, '08:19:00', '08:21:00'),

(9, 2, '00:57:00', '00:57:00'),
(9, 3, '04:41:00', '04:43:00'),
(9, 4, '05:55:00', '05:57:00'),
(9, 5, '08:19:00', '08:21:00'),

(10, 2, '00:57:00', '00:57:00'),
(10, 3, '04:41:00', '04:43:00'),
(10, 4, '05:55:00', '05:57:00'),
(10, 5, '08:19:00', '08:21:00'),

(11, 2, '00:57:00', '00:57:00'),
(11, 3, '04:41:00', '04:43:00'),
(11, 4, '05:55:00', '05:57:00'),
(11, 5, '08:19:00', '08:21:00'),

(12, 2, '00:57:00', '00:57:00'),
(12, 3, '04:41:00', '04:43:00'),
(12, 4, '05:55:00', '05:57:00'),
(12, 5, '08:19:00', '08:21:00'),

(13, 5, '09:51:00', '09:53:00'),
(13, 4, '13:20:00', '13:22:00'),
(13, 3, '14:31:00', '14:33:00'),
(13, 2, '16:49:00', '16:51:00'),

(14, 5, '09:51:00', '09:53:00'),
(14, 4, '13:20:00', '13:22:00'),
(14, 3, '14:31:00', '14:33:00'),
(14, 2, '16:49:00', '16:51:00'),

(15, 5, '09:51:00', '09:53:00'),
(15, 4, '13:20:00', '13:22:00'),
(15, 3, '14:31:00', '14:33:00'),
(15, 2, '16:49:00', '16:51:00'),

(16, 5, '09:51:00', '09:53:00'),
(16, 4, '13:20:00', '13:22:00'),
(16, 3, '14:31:00', '14:33:00'),
(16, 2, '16:49:00', '16:51:00'),

(17, 5, '09:51:00', '09:53:00'),
(17, 4, '13:20:00', '13:22:00'),
(17, 3, '14:31:00', '14:33:00'),
(17, 2, '16:49:00', '16:51:00');