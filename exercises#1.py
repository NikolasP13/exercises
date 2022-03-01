#Créer une fonction prenant en paramètre l'année de naissance d'une personne et lui retournant son l'âge qu'elle aura à sa fête en 2022
def age_en_2022(annee_de_naissance):
    age_actuel = 2022 - annee_de_naissance
    return age_actuel
print(age_en_2022(1996))