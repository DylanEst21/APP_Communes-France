import math
import csv
import sys


# 1. Lecture du CSV
liste_communes = []
with open("Liste_Communes.csv", newline="") as fichier:
    tab = csv.reader(fichier, delimiter=";")
    csv_header = next(tab)  # Lecture de l'en-tête
    for ligne in tab:
        liste_communes.append(ligne)


# 2. Recherche de la commune de référence
ville_ref = input("Indiquez votre ville de référence : ").upper()
found = False

for index in range(len(liste_communes)):
    if ville_ref in liste_communes[index]:
        coords_ref = liste_communes[index][-1]
        if coords_ref.strip() != "":
            liste_coords = coords_ref.split(",")

            try:
                latitude1 = float(liste_coords[0])
                longitude1 = float(liste_coords[-1])

            except ValueError:
                print(f"Impossible de convertir les coordonnées GPS pour {ville_ref}.")
                sys.exit(1)

            found = True
            break


if not found:
    print("Commune de référence introuvable dans le CSV. Veuillez vérifier l'orthographe.")
    sys.exit(1)



# 3. Formule de Haversine
def formule_haversine(latitudeA, longitudeA, latitudeB, longitudeB):        #le point A est celui de référence

    convertDegrees = math.pi / 180.0        # Conversion degrés -> radians
    angle1A = (90.0 - latitudeA) * convertDegrees
    angle1B = (90.0 - latitudeB) * convertDegrees
    angle2A = float(longitudeA) * convertDegrees
    angle2B = float(longitudeB) * convertDegrees
    cosinus = (math.sin(angle1A)*math.sin(angle1B)*math.cos(angle2A - angle2B)
               + math.cos(angle1A)*math.cos(angle1B))
    arc = math.acos(cosinus) * 6371     # 6371 km = rayon approximatif de la Terre
    return arc


# 4. Calcul de la distance pour chaque commune
def calcul_distances(liste_communes):
    liste_noms_distances = []
    for ligne in liste_communes:
        coords = ligne[-1].split(",")
        if coords[0].strip() == "" or coords[-1].strip() == "":
            continue        # On ignore les lignes sans coordonnées

        try:
            latitude2 = float(coords[0])
            longitude2 = float(coords[-1])

        except ValueError:
            continue        # Si conversion impossible, on ignore

        nom_commune = ligne[1]
        distance = formule_haversine(latitude1, longitude1, latitude2, longitude2)
        liste_noms_distances.append({"Nom": nom_commune, "Distance": distance})

    return liste_noms_distances




# 5. Différents Tris
def fusion(liste1, liste2):
    liste_fusionnee = []
    i, j = 0, 0
    while i < len(liste1) and j < len(liste2):
        if liste1[i]["Distance"] <= liste2[j]["Distance"]:
            liste_fusionnee.append(liste1[i])
            i += 1
        else:
            liste_fusionnee.append(liste2[j])
            j += 1
    while i < len(liste1):
        liste_fusionnee.append(liste1[i])
        i += 1
    while j < len(liste2):
        liste_fusionnee.append(liste2[j])
        j += 1

    return liste_fusionnee



def tri_fusion(liste):

    if len(liste) < 2:

        return liste[:]

    else:
        milieu = len(liste) // 2
        partie_gauche = tri_fusion(liste[:milieu])
        partie_droite = tri_fusion(liste[milieu:])

        return fusion(partie_gauche, partie_droite)



def tri_bulle(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tab[j]["Distance"] > tab[j+1]["Distance"]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab



def tri_selection(liste):
    n = len(liste)
    for i in range(0, n-1):
        minpos = i
        for j in range(i+1, n):
            if liste[j]["Distance"] < liste[minpos]["Distance"]:
                minpos = j
        liste[i], liste[minpos] = liste[minpos], liste[i]

    return liste




# 6. On calcule les distances
liste_distance = calcul_distances(liste_communes)


# 7. Choix du tri
choix_tri = input("Choisissez le type de tri désiré (fusion, selection ou bulle) : ").lower()

while choix_tri not in ["fusion", "bulle", "selection"]:
    choix_tri = input("Choisissez le type de tri désiré (fusion, selection ou bulle) : ").lower()


if choix_tri == "fusion":
    liste_triee = tri_fusion(liste_distance)

elif choix_tri == "bulle":
    liste_triee = tri_bulle(liste_distance)

elif choix_tri == "selection":
    liste_triee = tri_selection(liste_distance)



# 8. Affichage des statistiques
if len(liste_triee) < 2:
    print("Il n'y a pas assez de communes pour afficher des statistiques.")
    sys.exit(0)

print("--------------------------------------------------")
print(f"La ville la plus proche est {liste_triee[1]['Nom']} à {liste_triee[1]['Distance']:.2f} km.")

# Médiane = élément central dans la liste triée
milieu = len(liste_triee) // 2
print(f"La distance médiane est {liste_triee[milieu]['Nom']} à {liste_triee[milieu]['Distance']:.2f} km.")

# Premier quartile (environ 25 % de la liste)
q1_index = int(len(liste_triee) * 0.25)
print(f"Le premier quartile est {liste_triee[q1_index]['Nom']} à {liste_triee[q1_index]['Distance']:.2f} km.")

# Troisième quartile (environ 75 % de la liste)
q3_index = int(len(liste_triee) * 0.75)
print(f"Le troisième quartile est {liste_triee[q3_index]['Nom']} à {liste_triee[q3_index]['Distance']:.2f} km.")

# Plus lointaine = dernier élément
print(f"La ville la plus lointaine est {liste_triee[-1]['Nom']} à {liste_triee[-1]['Distance']:.2f} km.")
print("--------------------------------------------------")