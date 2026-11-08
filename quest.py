from xp import xp_pour_rang

quetes = [
    {"nom" : "running_4km", "type" : "daily", "rang" : "B"},
    {"nom" : "homework", "type" : "daily", "rang" : "C"},
    {"nom" : "the dishes", "type" : "daily", "rang" : "D"}
]

if __name__ == "__main__":
    for line in quetes :
        rang_quest = line["rang"]
        time = line["type"]
        gain = xp_pour_rang(rang_quest)
        print(f"Goal : {line["nom"]}, type : {time}, reward : {gain} XP")