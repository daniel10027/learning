SELECT dossier_id, sum(critere1) c1, sum(critere2) c2,  sum(critere3) c3,  sum(critere4) c4,  sum(critere5) c5 
FROM recrutement_resultat
GROUP BY dossier_id;

########################################
########################################

SELECT dossier_id, avg(critere1+critere2+critere3+critere4+critere5)/5 
FROM recrutement_resultat
GROUP BY dossier_id;

##########################################
 moyenne = Resultat.objects.values('dossier').order_by('dossier').annotate(moy=Avg('critere1'))
######################################################"

 moyenne = Resultat.objects.values('dossier').order_by('dossier').annotate(moy=((Avg('critere1'))+ (Avg('critere2'))+ (Avg('critere3'))+ (Avg('critere4'))+ (Avg('critere5')))/5)
###
################################################################"
SELECT nom, prenom, email, avg(critere1+critere2+critere3+critere4+critere5)/5 Moyenne
FROM [recrutement_dossierrecrutement] 
INNER JOIN recrutement_resultat
ON [recrutement_dossierrecrutement].id = recrutement_resultat.dossier_id
