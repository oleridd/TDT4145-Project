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
/* Antar at hvert tog blir på stasjonen i 2 min */
(1, 1, NULL, '07:49:00'),
(1, 2, '09:51:00', '09:53:00'), 
(1, 3, '13:20:00', '13:22:00'),
(1, 4, '14:31:00', '14:33:00'),
(1, 5, '16:49:00', '16:51:00'),
(1, 6, '17:34:00', NULL),

(2, 1, NULL, '07:49:00'),
(2, 2, '09:51:00', '09:53:00'), 
(2, 3, '13:20:00', '13:22:00'),
(2, 4, '14:31:00', '14:33:00'),
(2, 5, '16:49:00', '16:51:00'),
(2, 6, '17:34:00', NULL),

(3, 1, NULL, '07:49:00'),
(3, 2, '09:51:00', '09:53:00'), 
(3, 3, '13:20:00', '13:22:00'),
(3, 4, '14:31:00', '14:33:00'),
(3, 5, '16:49:00', '16:51:00'),
(3, 6, '17:34:00', NULL),

(4, 1, NULL, '07:49:00'),
(4, 2, '09:51:00', '09:53:00'), 
(4, 3, '13:20:00', '13:22:00'),
(4, 4, '14:31:00', '14:33:00'),
(4, 5, '16:49:00', '16:51:00'),
(4, 6, '17:34:00', NULL),

(5, 1, NULL, '07:49:00'),
(5, 2, '09:51:00', '09:53:00'), 
(5, 3, '13:20:00', '13:22:00'),
(5, 4, '14:31:00', '14:33:00'),
(5, 5, '16:49:00', '16:51:00'),
(5, 6, '17:34:00', NULL),


(6, 1, NULL, '23:05:00'),
(6, 2, '00:57:00', '00:59:00'),
(6, 3, '04:41:00', '04:43:00'),
(6, 4, '05:55:00', '05:57:00'),
(6, 5, '08:19:00', '08:21:00'),
(6, 6, '09:05:00', NULL),

(7, 1, NULL, '23:05:00'),
(7, 2, '00:57:00', '00:59:00'),
(7, 3, '04:41:00', '04:43:00'),
(7, 4, '05:55:00', '05:57:00'),
(7, 5, '08:19:00', '08:21:00'),
(7, 6, '09:05:00', NULL),

(8, 1, NULL, '23:05:00'),
(8, 2, '00:57:00', '00:59:00'),
(8, 3, '04:41:00', '04:43:00'),
(8, 4, '05:55:00', '05:57:00'),
(8, 5, '08:19:00', '08:21:00'),
(8, 6, '09:05:00', NULL),

(9, 1, NULL, '23:05:00'),
(9, 2, '00:57:00', '00:59:00'),
(9, 3, '04:41:00', '04:43:00'),
(9, 4, '05:55:00', '05:57:00'),
(9, 5, '08:19:00', '08:21:00'),
(9, 6, '09:05:00', NULL),

(10, 1, NULL, '23:05:00'),
(10, 2, '00:57:00', '00:59:00'),
(10, 3, '04:41:00', '04:43:00'),
(10, 4, '05:55:00', '05:57:00'),
(10, 5, '08:19:00', '08:21:00'),
(10, 6, '09:05:00', NULL),

(12, 1, NULL, '23:05:00'),
(12, 2, '00:57:00', '00:59:00'),
(12, 3, '04:41:00', '04:43:00'),
(12, 4, '05:55:00', '05:57:00'),
(12, 5, '08:19:00', '08:21:00'),
(12, 6, '09:05:00', NULL),

(13, 4, NULL, '08:11:00'),
(13, 3, '09:14:00', '09:16:00'),
(13, 2, '12:31:00', '12:22:00'),
(13, 1, '14:31:00', NULL),

(14, 4, NULL, '08:11:00'),
(14, 3, '09:14:00', '09:16:00'),
(14, 2, '12:31:00', '12:22:00'),
(14, 1, '14:31:00', NULL),

(15, 4, NULL, '08:11:00'),
(15, 3, '09:14:00', '09:16:00'),
(15, 2, '12:31:00', '12:22:00'),
(15, 1, '14:31:00', NULL),

(16, 4, NULL, '08:11:00'),
(16, 3, '09:14:00', '09:16:00'),
(16, 2, '12:31:00', '12:22:00'),
(16, 1, '14:31:00', NULL),

(17, 4, NULL, '08:11:00'),
(17, 3, '09:14:00', '09:16:00'),
(17, 2, '12:31:00', '12:22:00'),
(17, 1, '14:31:00', NULL),