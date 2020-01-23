# TP Paradigme Objet - DIU Enseigner NSI

### Partie 1 - Étude guidée du projet 

Cette partie est conçu sur la base de 2 principes :
 
 - principe de l'instruction par les exemples.
 - principe du "think-paire-share".
 
 Le projet est riche, il mérite donc une présentation détaillée par le formateur.
 Les points importants à présenter sont :
 
 - la structure générique : séparation du code principal, du code de test. Le message cible ici est
 qu'une bonne pratique est la séparation du code principal du code de test.
 - la structure du code principal : distinction claire entre les objets que l'on manipule, que l'on simule (le modèle)
 avec les objets responsables de la présentation des objets du modèles et des interactions de l'utilisateur (la vue). 
 C'est une bonne pratique (le pattern de conception MVC) pour faciliter la compréhension, les évolutions et la 
 maintenance du programme.
 - l'indication de typage dans les déclarations de méthodes : ce n'est pas obligatoire en Python (pourquoi on fait du python :-(?),
 mais c'est indispensable pour clarifier le code, faciliter sa maintenance, etc.
 - les tests : la manière dont ils sont écrits, la manière dont ils sont utilisés avec PyCharm.
    
    - chaque test est découpé en cas de succès et cas d'erreur
    - les tests sont conçus comme outil pour la vérification mais aussi comme 
   spécification détaillée du comportement des objets sous test. Cette idée devrait être
   plus claire pour la deuxième partie ou le test sur Abeille leur permettra de définir 
   précisément la classe Abeille attendue.
   
 -le détail du model : on s'intéresse pour l'instant à la cartographie de fleurs pouvant libérer du
 pollen. Oui, c'est plus dans l'air du temps que les voitures :-). Un parcours des classes rapides 
 est à prévoir.
 - focus sur le journal : facilité pour afficher les résultats de ce que font les objets
 - focus sur la vue : les objets vues ont des comportements identiques, on pourra en profiter pour
 évoquer le polymorhisme comme moyen d'optimiser la vue si cela s'y prête dans la 3ème phase de l'exercice.
 
La 3ème phase justement (le share) est l'opportunité de repondre mais aussi de laisser les autres
stagiaires répondre aux questions qui se poseront.

### Partie 2 - Des abeilles sur la carte

#### Exercice 1 
L'objectif ici est de montrer ce que peut apporter une approche guidée par les tests :

- spécification détaillée de classe
- travail en autonomie
- feedback automatique

#### Exercice 2

Approche plus traditionnelle, plus libre pour développer l'application
cliente de l'ensemble du modèle, abeilles comprises :-).
Les stagiaires les plus chauds pourront essayer d'écrire les tests relatifs à
la classe Carte qui doit être modifiée. 