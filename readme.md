<p align="center"><img width=30% src="https://github.com/daniel10027/learning/blob/master/static/enseignement/img/core-img/logo.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.7.6-blue.svg)
![Django](https://img.shields.io/badge/Djanvo-v3.0.5-orange.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![License](https://img.shields.io/badge/license-MIB-blue.svg)](https://analyst123.herokuapp.com)
![Contributors](https://img.shields.io/badge/contributors-@daniel10027-blue.svg)
![issues](https://img.shields.io/badge/issues-0%20open-brightgreen.svg)

## PRÉSENTATION

```console
EduVroom est mon projet de fin de cycle réalisé avec le framwork django.
```
### OBJECTIF DU PROJET

```console
De manière générale, le projet collectif tutoré (PCT) permet aux étudiants de licence 3 de
réinvestir leurs connaissances acquises depuis le semestre 1 jusqu’au semestre 5 dans la
réalisation d’un projet. Il développe en eux les compétence suivantes :
● Initiation à la gestion de projet en Informatique et Sciences du Numérique ;
● Travail collaboratif ;
● Travail autonome ;
● Recherche et synthétiser de l’information ;
● Acquisition d’une expérience professionnelle ;
● Acquisition et développement des savoirs ;
● Leadership.
```

### LES EXIGEANCES DU PROJET 

_*Module 1 : Gestion des enseignements des établissements publics supérieurs de Côte d’Ivoire*._

```console
Il s’agit, dans ce projet de développer une base de données qui permettra de répertorier toutes
les universités et grandes écoles publiques de Côte d’Ivoire et les enseignements qu’elles
proposent aux publics.
 Créer une base de données de toutes les universités publiques et grandes écoles de Côte
d’Ivoire, les UFR qui composent chacune d’elles, les filières enseignées dans chacune de ces
UFR, les spécialités enseignées dans chacune de ces filières et les ECUE enseignés dans
chacune de ces spécialités. Il s’agit des établissements suivants :
- Université Félix Houphouët Boigny (UFHB) de Cocody ;
- Université Alassane Ouattara (UAO) de Bouaké ;
- Université Nagui Abrogoua (UNA) d’Abidjan ;
- Université Jean Lorougnon Guédé (UJLoG) de Daloa ;
- Université Péléforo Gon (UPGC) de Korhogo ;
- Université de Man (UMan)
- École Supérieure Africaine des Techniques de l'Information et de la Communication
(ESATIC) ;
- Institut National Polytechnique Houphouët Boigny (INPHB) de Yamoussoukro ;
- Ecole Normale Supérieure (ENS) d’Abidjan ;
- École Nationale de Statistiques et d’Économie Appliquée (ENSEA) ;
- Centre de Bureautique de Communication et de Gestion (CBCG) de Cocody ;
- Centre de Bureautique de Communication et de Gestion (CBCG) de Treichville ;
- Centre de Bureautique de Communication et de Gestion (CBCG) de Bouaké ;
- Centre de Bureautique de Communication et de Gestion (CBCG) de Daloa.
Pour chaque ECUE, les informations suivantes sont demandées :
- L’intitulé de l’ECUE (cours) ;
- Le code de l’ECUE
- L’objectif général ;
- Les objectifs spécifiques ;
- Le niveau : Licence 1, Licence 2, Licence 3, Master 1, Master 2, Doctorat ;
- Le semestre dans lequel est enseigné cet ECUE ;
- Le volume horaire ;
- La répartition (temps CM, temps TD, temps TP) ;
- Le nombre de crédit ;
- Les compétences visées ;
- Le matériel pédagogique à utiliser (Logiciel, autre matériel)
- Les identifiants de l’enseignant (Nom et prénom; téléphone; adresse; e-mail; grade;
discipline; structure de formation dans laquelle il enseigne, etc.);
Cette base de données permettra par exemple de ressortir les informations suivantes :
- La cartographie des universités et grandes écoles publiques de Côte d’Ivoire ;
- Le nombre d’UFR, de filières, de spécialité par université ;
- Le nombre d’ECUE enseignés dans chaque établissement et le nombre d’EUCE
enseignés dans tous les établissements publics de Côte d’Ivoire.
- Pour un ECUE donné, on devrait savoir quels sont les établissements qui l’enseigne et
dans quelle UFR de quel établissement il est enseigné, et aussi le nom du ou des
enseignant(s) qui l’enseigne.
- etc
```
_*Module 2 : Recrutement des Enseignants et des tuteurs*_

```console

 Développer une application de recrutement et de gestion des enseignants désireux de dispenser
des cours dans ladite structure. Cette application devra permettre également de recruter et de
gérer des tuteurs spécialisés dans des disciplines et qui désirent accompagner les auditeurs dans
des cours dans ladite structure.
Ce module de cette application devra permettre de :
Lancer l’appel à recrutement avec les éléments suivants :
- objet de recrutement ;
- date d’ouverture et de fermeture de l’appel ;
- public cible ;
- modalité d’évaluation ;
- date de passage devant un jury ;
- date de publication des résultats.
Réceptionner les dossiers :
- remplissage de formulaire (nom, prénoms, date de naissance, ...) ;
- attachement de fichiers (diplôme, certificats, pièce d’identité, lettre de motivation, photo
d’identité) ;
NB : La taille maximale de chaque pièce jointe ne doit pas dépasser 500Ko.
Constitution des jurys :
- enregistrement des membres des différents jurys :
° remplissage de formulaire (nom, prénoms, date de naissance, ...) ;
° attachement de fichiers (diplômes, certificats, pièces d’identité,
 lettre de motivation, photos d’identité) ;
NB : La taille maximale de chaque pièce jointe ne doit pas dépasser
500Ko ;
- affectation de chaque membre à un jury donné ;
Constituer les jurys de recrutement :
- Chaque membre du jury se connecte à l’application ;
- Chaque membre de jury peut consulter le dossier d’un candidat qui est affecté à son jury
- À partir d’une grille critériée de recrutement, chaque juré note chaque candidat affecté
à son jury ;
- Pour un jury donné, l’application compile les résultats de tous les membres pour chaque
candidat et génère la liste par ordre de mérite des candidats passés devant le jury ;
```
