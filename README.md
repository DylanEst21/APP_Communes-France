# APP – Statistiques et tris sur les communes de France

## Description
Ce projet propose un **script Python** permettant de :
1. **Charger** la liste des communes françaises depuis un fichier CSV (coordonnées GPS, noms, etc.).
2. **Demander** à l’utilisateur de saisir une commune de référence.
3. **Calculer** la distance entre la commune de référence et chaque autre commune à l’aide de la **formule de Haversine**.
4. **Trier** les communes par ordre **croissant** de distance grâce à différents **algorithmes de tri manuels**.
5. **Afficher** des statistiques détaillées, dont :
   - La commune la plus proche (min),
   - Le premier quartile,
   - La médiane,
   - Le troisième quartile,
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
  - Distance maximale (commune la plus lointaine).

---

## Prérequis
- **Python 3.x** (version recommandée : 3.6 ou plus).
- Bibliothèques standard (intégrées) : `csv`, `math`.
- **Fichier `Liste_Communes.csv`** à placer dans le **même dossier** que le script Python.
