table_rangs = [
    {"classification" : "D", "xp" : 10},
    {"classification" : "C", "xp" : 20},
    {"classification" : "B", "xp" : 40},
    {"classification" : "A", "xp" : 80},
    {"classification" : "S", "xp" : 150},
]

def xp_for_level(niveau : int)-> float :
    """donne la quantité d'experiance requis pour chaque niveau"""
    return int(100 * niveau ** 1.5)
    
def  niveau_actuel(xp_total : float)-> int:
    """Fonction ayant pour objectif de déterminer le niveau de l'utilisateur a partir de son experiance"""
    xp_restant = xp_total
    for niveau in range(1,100):
        cout = xp_for_level(niveau)
        if xp_restant < cout :
            return niveau
        xp_restant -= cout
    return 99

def gain_quest(xp_total: int, xp_add: int) -> int:
    """Ajoute l'expérience gagnée pendant une quête et renvoie le nouvel XP total."""
    return xp_total + xp_add

def xp_pour_rang(rang: str) -> int:
    """Renvoie la quantité d'expérience obtenue pour le rang de quête donné en paramètre."""
    for ligne in table_rangs:
        if ligne["classification"] == rang:
            return ligne["xp"]
    return 0


if __name__ == "__main__":
    print("### Software : xp ###\n### Procédure de test en cours ###")

    for niveau in range(1, 21):
        print(f"Niveau {niveau} : {xp_for_level(niveau)} XP")

    xp_total = 756
    print(f"Niveau : {niveau_actuel(xp_total)}")

    xp_total = xp_total + 521
    print(f"Niveau : {niveau_actuel(xp_total)}")

    nom_quete = "Exister..."
    xp_quete = 50
    print(f"Nouvelle quête !!! :\n{nom_quete} récompense : {xp_quete} XP")

    avancement = input("Quête terminée ? O/N : ").strip().upper()
    if avancement == "O":
        xp_total = gain_quest(xp_total, xp_quete)
        print(f"+{xp_quete} XP ! Total : {xp_total} XP, niveau {niveau_actuel(xp_total)}")
    elif avancement == "N":
        print("Quête non terminée, aucun XP gagné.")
    else:
        print("Réponse non reconnue, tape O ou N.")
    
    print(xp_pour_rang("B"))
    print(xp_pour_rang("Z"))