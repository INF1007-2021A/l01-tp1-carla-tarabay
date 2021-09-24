
def decomposer(secondes):


    annees = secondes//(60*60*24*365)
    annees_reste= secondes%(60*60*24*365)



    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines= annees_reste//(60*60*24*7)
    semaines_reste= annees_reste%(60*60*24*7)


    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = semaines_reste//(60*60*24)
    jours_reste=semaines_reste%(60*60*24)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = jours_reste//(60*60)
    heures_reste= jours_reste%(60*60)

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = heures_reste//(60)
    minutes_reste= heures_reste%(60)

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes =minutes_reste

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees, "années" ,semaines , "semaines",jours,  "jours",heures, "heures", minutes, "minutes", secondes, "secondes")
    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
