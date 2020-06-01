## 1- La cartographie des universités et grandes écoles publiques de Côte d’Ivoire
```js
SELECT  enseignement_etablissement.nom AS Etablissement,
		enseignement_etablissement.sigle, 
        enseignement_localite.nom AS Localite,
        enseignement_typeetablissement.nom AS Type,
        enseignement_statutetablissement.nom AS Statut
FROM    enseignement_etablissement
INNER JOIN 
	enseignement_localite 
    ON enseignement_etablissement.localite_id=enseignement_localite.id
INNER JOIN 	
	enseignement_typeetablissement 	
    ON enseignement_etablissement.type_etablissement_id=enseignement_typeetablissement.id
INNER JOIN 
	enseignement_statutetablissement 		
    ON enseignement_etablissement.statut_etablissement_id=enseignement_statutetablissement.id
ORDER BY Etablissement;
```

## 2- Le nombre d’UFR, de filières, de spécialité par université 