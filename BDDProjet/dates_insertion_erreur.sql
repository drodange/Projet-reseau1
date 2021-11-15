-- Toutes les insertions de ce ficheir doivent être refusées
-- Forum.Programme
-- UNIQUE (idConferencier, date_debut),
INSERT INTO Dates.edt
  VALUES(1,4,'2021-12-11','2021-12-12');
-- UNIQUE (idConferencier, date_fin)
INSERT INTO Dates.edt
  VALUES(1,4,'2021-11-30','2021-12-15');
-- UNIQUE (idAmphi, date_debut)
INSERT INTO Dates.edt
  VALUES(6,2,'2021-12-01','2021-12-10');
-- UNIQUE (idAmphi, date_fin)
INSERT INTO Dates.edt
  VALUES(6,2,'2021-11-25','2021-12-05');
-- CHECK (date_debut <= date_fin)
INSERT INTO Dates.edt
  VALUES(6,4,'2022-01-25','2022-01-23');

-- Erreurs de chevauchement de dates sur conférencier-conférencier
INSERT INTO Dates.Edt
  VALUES(2,4,'2021-11-30','2021-12-03');
INSERT INTO Dates.Edt
  VALUES(2,4,'2021-11-29','2021-12-07');
INSERT INTO Dates.Edt
  VALUES(2,4,'2021-12-02','2021-12-04');
INSERT INTO Dates.Edt
  VALUES(2,4,'2021-12-03','2021-12-08');
-- Erreurs de chevauchement de dates sur amphi
INSERT INTO Dates.Edt
  VALUES(6,2,'2021-11-30','2021-12-03');
INSERT INTO Dates.Edt
  VALUES(6,2,'2021-11-29','2021-12-07');
INSERT INTO Dates.Edt
  VALUES(6,2,'2021-12-02','2021-12-04');
INSERT INTO Dates.Edt
  VALUES(6,2,'2021-12-03','2021-12-08');
