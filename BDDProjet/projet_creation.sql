CREATE SCHEMA Projet;
SET search_path TO Projet, public;
CREATE TABLE Projet.Adherents (
	matricule serial NOT NULL,
	nom text NOT NULL,
	prenom text NOT NULL,
	admin boolean,
	conferencier boolean,
	auditeurs boolean,
	PRIMARY KEY (matricule)
);
CREATE TABLE Projet.Conference (
	num_conf serial NOT NULL,
	theme text NOT NULL,
	matricule serial NOT NULL,
	PRIMARY KEY (num_conf),
	FOREIGN KEY (matricule) REFERENCES Projet.Adherents(matricule)
);
CREATE TABLE Projet.Amphi (
	num_amphi serial NOT NULL,
	nb_place integer NOT NULL CHECK (nb_place >= 0),
	/*emplacement text NOT NULL,*/
	num_conf serial NOT NULL,
	cout_loc integer NOT NULL CHECK (cout_loc >= 0),
	PRIMARY KEY (num_amphi),
	FOREIGN KEY (num_conf) REFERENCES Projet.Conference(num_conf)
);
CREATE TABLE Projet.Compta (
	prix_conf integer NOT NULL CHECK (prix_conf >= 0),
	cout_total integer NOT NULL CHECK (cout_total >= 0),
	indeminite integer NOT NULL CHECK (indeminite >= 0),
	num_amphi serial NOT NULL,
	PRIMARY KEY (num_amphi),
	FOREIGN KEY (num_amphi) REFERENCES Projet.Amphi(num_amphi)
);
CREATE TABLE Projet.Programme (
	num_conf serial NOT NULL,
	matricule serial NOT NULL,
	date_debut date NOT NULL,
	date_fin date NOT NULL,
	PRIMARY KEY (date_debut, date_fin),
	FOREIGN KEY (matricule) REFERENCES Projet.Adherents(matricule),
	FOREIGN KEY (num_conf) REFERENCES Projet.Conference(num_conf),
	CHECK (date_debut <= date_fin)
);


