# APP – Statistiques et tris sur les communes de France

## Table des Matières
- [Description](#description)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Étapes Clés du Projet](#étapes-clés-du-projet)
- [Fichiers Utilisés](#fichiers-utilisés)
- [Choix Techniques](#choix-techniques)
- [Prérequis](#prérequis)
- [Utilisation](#utilisation)
- [Exemple d’Exécution](#exemple-dexécution)

---

## Description

Ce projet propose un **script Python** permettant de :

1. **Charger** la liste des communes françaises depuis un fichier CSV (`Liste_Communes.csv`).
2. **Demander** à l’utilisateur de saisir une commune de référence.
3. **Calculer** la distance entre la commune de référence et toutes les autres communes en utilisant la **formule de Haversine**.
4. **Trier** les communes par ordre **croissant** de distance, en utilisant différents **algorithmes de tri manuels**.
5. **Afficher** des statistiques sur les distances :
   - La commune la plus proche (min).
   - Le premier quartile.
   - La médiane.
   - Le troisième quartile.
   - La commune la plus éloignée (max).

---

## Fonctionnalités principales

- **Lecture des communes** depuis un CSV (données de [data.gouv.fr](https://www.data.gouv.fr/)).
- **Saisie interactive** de la commune de référence par l’utilisateur.
- **Calcul des distances** via la **formule de Haversine**.
- **Tri des communes** selon trois algorithmes :
  - **Tri à bulles** (Complexité : O(n²))
  - **Tri par sélection** (Complexité : O(n²))
  - **Tri fusion** (Complexité : O(n log n))
- **Affichage de statistiques** : 
  - Distance minimale (commune la plus proche),
  - Quartiles (1er et 3e),
  - Médiane,
  - Distance maximale (commune la plus éloignée).

---

## Étapes Clés du Projet

1. **Chargement des données :**
   - Lecture du fichier CSV contenant les informations des communes (nom, code postal, coordonnées GPS, ...).
   - Stockage des données sous forme de liste.

2. **Sélection de la commune de référence :**
   - L’utilisateur saisit le nom de la commune.
   - Recherche dans la base et récupération des coordonnées GPS.

3. **Calcul des distances :**
   - Application de la **formule de Haversine** pour calculer la distance entre la commune de référence et toutes les autres.

4. **Tri des distances :**
   - Implémentation de **trois algorithmes de tri** :
     - Tri à bulles
     - Tri par sélection
     - Tri fusion
   - Classement des communes par ordre croissant de distance.

5. **Affichage des statistiques :**
   - Extraction des valeurs **minimale, médiane, quartiles et maximale**.
   - Affichage des résultats sous forme textuelle.

---

## Fichiers Utilisés

- **`Liste_Communes.csv`** : Contient les informations sur les communes de France, y compris les coordonnées GPS.

---

## Choix Techniques

- **Formule de Haversine :**
  - Utilisée pour calculer la distance entre deux points à partir de leurs **coordonnées GPS**.
  - Appropriée pour des distances longues sur une sphère (comme la Terre).

- **Algorithmes de tri :**
  - **Tri à bulles** (O(n²)) : Simple mais inefficace sur de grandes données.
  - **Tri par sélection** (O(n²)) : Moins d’échanges, mais toujours inefficace.
  - **Tri fusion** (O(n log n)) : Plus rapide, recommandé pour de grandes listes.

- **Manipulation de fichiers CSV :**
  - Utilisation du module `csv` pour lire les données des communes.

---

## Prérequis

- **Python 3.x** (version recommandée : 3.6 ou plus).
- Bibliothèques Python intégrées :
  - `csv` (pour la lecture du fichier CSV).
  - `math` (pour la formule de Haversine).
- **Fichier `Liste_Communes.csv`** à placer dans le **même dossier** que le script Python.

---

## Utilisation

1. **Exécuter le script Python :**

    ```bash
    python APP_Communes_France.py
    ```

2. **Suivre les instructions à l’écran :**
   - Entrez la commune de référence.
   - Sélectionnez l’algorithme de tri (fusion, sélection ou bulle).
   - Attendez que le script calcule et affiche les résultats.

---

## Exemple d’Exécution

```plaintext
## Exemple d’Exécution

```plaintext
Indiquez votre ville de référence : Monaco
Choisissez le type de tri désiré (fusion, selection ou bulle) : fusion
--------------------------------------------------
La ville la plus proche est BEAUSOLEIL à 1.51 km.
La distance médiane est FRAISSE à 581.35 km.
Le premier quartile est BOR ET BAR à 429.98 km.
Le troisième quartile est ANY MARTIN RIEUX à 725.47 km.
La ville la plus lointaine est RIMATARA à 17051.24 km.
--------------------------------------------------
