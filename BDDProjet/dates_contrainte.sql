-- puis appeler la fonction dans une contrainte d'integrite
ALTER TABLE Dates.Edt ADD CONSTRAINT DatesPossibles
  CHECK(Dates.DatesDebutFinEdt(idEns, idAmphi, date_debut, date_fin));
