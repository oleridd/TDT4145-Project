INSERT INTO SoveBillett
VALUES
(1, 1, 5, 1, 4, "23/03/2023"),
(2, 1, 5, 4, 4, "23/03/2023");


INSERT INTO SitteBillett
VALUES
(3, 1, 2, 2, 4, "23/03/2023"),
(4, 1, 3, 1, 4, "23/03/2023"), /* Noe galt med disse to */
(4, 2, 3, 2, 4, "23/03/2023"),
(5, 1, 2, 5, 4, "23/03/2023");


INSERT INTO StrekningPaaBanestrekning
VALUES
(10, 4, 1), /* Disse to skal kun to strekninger */
(8, 4, 1),
(10, 4, 2),
(8, 4, 2),

(10, 3, 1), /* Billett (3, 1) skal hele veien */
(8, 3, 1),
(6, 3, 1),
(4, 3, 1),
(2, 3, 1),

(4, 5, 1); /* Billett (5, 1) skal kun ett stopp */