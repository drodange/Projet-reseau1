-- PostgreSQL n'accepte pas les contraintes d'integrite avec un SELECT
-- Il faut definir une fonction
CREATE FUNCTION Dates.DatesDebutFinEdt(integer, integer, date, date) 
  RETURNS boolean AS $$ 
SELECT NOT EXISTS (
  SELECT *
  FROM Dates.Edt
  WHERE (($1 = idEns) OR ($2 = idAmphi))
    AND $3 <= date_fin
    AND $4 >= date_debut
  )
$$ LANGUAGE SQL;
