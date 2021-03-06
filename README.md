# Data Pipeline pour le traitement de données médicales



## Introduction
Ce projet est un exercice de data processing sur des données médicales, conçu pour le déploiment dans un data pipeline avec possibilité d'être intégré dans un orchestrateur de jobs type DAG.



## Méthodologies
### Objectif de l'exercice
Concevoir un data pipeline pour le nettoyage, la standardisation et le filtrage des données afin de produire en sortie un unique fichier JSON qui représente un graphe de liaison entre les différents médicaments et leurs mentions respectives dans les différentes publications PubMed, les différentes publications scientifiques et enfin les journaux avec la date associée à chacune de ces mentions.



### Etapes de data processing
Pour ce faire, le data pipeline est découpé en 2 étapes:
  * Etape 1: Restitution de données pubmed dans un seul fichier .csv
  * Etape 2: Génération d’une représentation de graphes des 3 tables drugs, clinical trials et pubmed dans un seul fichier .json



### Organisation des fichiers 
  * ***data/***
     * ***drugs.csv***: contenant les noms de drugs (des médicaments) avec un id (atccode) et un nom (drug)
     * ***clinical_trials.csv***: contenant des publications scientifiques avec un titre (scientific_title), un id (id), un journal (journal) et une date (date)
     * ***pubmed.csv***: contenant des titres d’articles PubMed (title) associés à un journal (journal) à une date donnée (date) ainsi qu’un id (id)
     * ***pubmed.json*** : même structure que pubmed.csv mais en format JSON
     
  * ***pubmed_restitution.py***: exécutable principal appelé pour effectuer l'Etape 1, produira en sortie **data/pubmed_restit.csv** utilisé par l'Etape 2
  
  * ***components.py***: contenant les classes customisées pour créer la structures de données, appelé par main.py afin d'accomplir l'Etape 2
  
  * ***processing_fct.py***: contenant les function de nettoyage et transformation des données, appelé par main.py afin d'accomplir l'Etape 2
      
  * ***main.py***: exécutable principal appélé pour effectuer l'Etape 2, produira en sortie fichier final **data/complete_data.json**
      
  * ***data_extraction.py***: exécutable de traitement ad-hoc afin de confirmer notre structure de données, dans le but de répondre à la question suivante: depuis complete_data.json, extraire le nom du journal qui mentionne le plus de médicaments différents? 
  L'exécutable produira **data/analyse_ad_hoc.csv**
  
  * ***pubmed_restit.sh***: utilisé sur Jenkins pour l'Etape 1 (en savoir plus: consulter Mode d'emploi - Data pipeline.pdf)
  
  * ***main.sh***: utilisé sur Jenkins pour l'Etape 2 (en savoir plus: consulter Mode d'emploi - Data pipeline.pdf)
  
  * ***Mode d'emploi - Data pipeline.pdf***: documentation de l'implémentation du code dans le répertoire Github sur Jenkins



### Déploiement du data pipeline sur Jenkins
Afin de confirmer nos hypothèses de travail pour s'assurer que les étapes de data processing s'intégrent facilement dans un orchestrateurs de jobs, nous avons fait appel à Jenkins, un outil d'intégration continue open-source.
Vous trouverez plus de détails dans le fichier **Mode d'emploi - Data pipeline.pdf**.

  



 
