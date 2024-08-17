# Bike Share Data Analysis

## Description

Ce projet utilise Python pour explorer les données des systèmes de vélos en libre-service pour trois grandes villes des États-Unis : Chicago, New York et Washington. L'objectif est de calculer diverses statistiques descriptives sur les trajets en vélo et de créer une expérience interactive en terminal pour présenter ces statistiques.



1. **Préparer les Données**

   Téléchargement du fichier ZIP `Bike_raw_data.zip` contenant les fichiers CSV des données brutes. Décompression du fichier dans un répertoire nommé `DataEngineer/Junior` pour que le script puisse accéder aux fichiers CSV.

## Utilisation

2. **Exécution du Script Principal**

    Le script principal d'analyse est excécuté comme suit :

   ```bash
   python bike_investigation.py
   ```

   Vous serez invité à entrer les informations suivantes :
   - **Ville** : Choisissez parmi `chicago`, `new york city`, ou `washington`.
   - **Mois** : Choisissez parmi `all`, `january`, `february`, ..., `june`. Utilisez `all` pour ne pas filtrer par mois.
   - **Jour** : Choisissez parmi `all`, `monday`, `tuesday`, ..., `sunday`. Utilisez `all` pour ne pas filtrer par jour.

   Le script affichera les statistiques suivantes :
   - **Périodes de voyage populaires** :
     - Mois le plus courant
     - Jour le plus courant de la semaine
     - Heure la plus courante de la journée
   - **Gares populaires et trajets** :
     - Station de départ la plus courante
     - Station d'arrivée la plus courante
     - Trajet le plus fréquent (combinaison la plus courante de la station de départ et de la station d'arrivée)
   - **Durée du voyage** :
     - Temps total de déplacement
     - Temps de trajet moyen
   - **Infos utilisateur** :
     - Nombre de chaque type d'utilisateur
     - Nombre de chaque sexe 
     - Année de naissance la plus ancienne, la plus récente, et la plus courante 

2. **Exécution des Tests**

   Pour exécuter les tests unitaires, utilisez la commande suivante :

   ```bash
   python -m unittest test_bike_investigation.py
   ```

   Les tests vérifieront que les fonctions principales produisent les résultats attendus avec des données choisies.


## Documentation des Fonctions

- **`get_filters()`** : Spécifie la ville, le mois, et le jour pour l'analyse.
- **`load_data(city, month, day)`** : Charge les données pour la ville spécifiée et applique les filtres pour le mois et le jour.
- **`time_stats(df)`** : Affiche les périodes les plus fréquentes pour les trajets (mois, jour de la semaine, heure de début).
- **`station_stats(df)`** : Affiche les stations de départ et d'arrivée les plus populaires ainsi que les trajets les plus fréquents.
- **`trip_duration_stats(df)`** : Affiche la durée totale et moyenne des trajets.
- **`user_stats(df)`** : Affiche les statistiques sur les types d'utilisateurs, le genre, et les années de naissance.

## Tests

Le fichier de tests `test_bike_investigation.py` vérifie les résultats des fonctions suivantes :

- **`time_stats(df)`** : Vérifie les périodes les plus fréquentes (mois, jour de la semaine, heure de début).
- **`station_stats(df)`** : Vérifie les stations et trajets les plus populaires.
- **`trip_duration_stats(df)`** : Vérifie la durée totale et moyenne des trajets.
- **`user_stats(df)`** : Vérifie les statistiques sur les utilisateurs (types, genre, années de naissance).


