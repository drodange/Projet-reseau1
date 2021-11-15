CREATE SCHEMA Dates;
-- Les entités
CREATE TABLE Dates.Edt (
  idEns integer NOT NULL, -- Le conferencier
  idAmphi integer NOT NULL,
  date_debut date NOT NULL,
  date_fin date NOT NULL,
  -- clefs candidates
  PRIMARY KEY (idEns, date_debut),
  UNIQUE (idEns, date_fin),
  UNIQUE (idAmphi, date_debut),
  UNIQUE (idAmphi, date_fin),
  -- Contrainte intégrité élémentaire
  CHECK (date_debut <= date_fin)
);
