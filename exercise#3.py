#Créer une fonction prenant 1 ou 2 nombres et effectuer l'addition de leur carré. Si un seul nombre est passé en paramètre, assumez que sa valeur est 1.
def calcul_carree_no1(no1):
    carree_no1 = no1 * no1
    return carree_no1
def calcul_carree_no2(no2):
    carree_no2 = no2 * no2
    return carree_no2
def calcul_sommes_carrees(carree_no1, carree_no2):
    calcul_final = carree_no1 + carree_no2
    return calcul_final
print (calcul_carree_no1(2))
print (calcul_carree_no2(3))
print (calcul_sommes_carrees(4,9))