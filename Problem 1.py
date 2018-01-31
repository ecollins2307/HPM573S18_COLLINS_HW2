# HW 2, Problem 1

#Prompting user for input and checking said input
vision = int(input("Please input HUI3 Vision attribute level: "))
if not (vision in [1,2,3,4,5,6]):
    raise ValueError("HUI3 Vision level can take only 1, 2, 3, 4, 5, or 6")

hearing = int(input("Please input HUI3 Hearing attribute level: "))
if not (hearing in [1,2,3,4,5,6]):
    raise ValueError("HUI3 Hearing levels can take only 1, 2, 3, 4, 5, or 6")

speech = int(input("Please input HUI3 Speech attribute level: "))
if not (speech in [1,2,3,4,5]):
    raise ValueError("HUI3 Speech levels can take only 1, 2, 3, 4, or 5")

ambulation = int(input("Please input HUI3 Ambulation attribute level: "))
if not (ambulation in [1,2,3,4,5,6]):
    raise ValueError("HUI3 Ambulation levels can take only 1, 2, 3, 4, 5, or 6")

dexterity = int(input("Please input HUI3 Dexterity attribute level: "))
if not (dexterity in [1,2,3,4,5,6]):
    raise ValueError("HUI3 Dexterity levels can take only 1, 2, 3, 4, 5, or 6")

emotion = int(input("Please input HUI3 Emotion attribute level: "))
if not (emotion in [1,2,3,4,5]):
    raise ValueError("HUI3 Emotion levels can take only 1, 2, 3, 4, or 5")

cognition = int(input("Please input HUI3 Cognition attribute level: "))
if not (cognition in [1,2,3,4,5,6]):
    raise ValueError("HUI3 Dexterity levels can take only 1, 2, 3, 4, 5, or 6")

pain = int(input("Please input HUI3 Pain attribute level: "))
if not (pain in [1,2,3,4,5]):
    raise ValueError("HUI3 Pain levels can take only 1, 2, 3, 4, or 5")

#Creating attribute coefficient dictionaries
vis_dic = {1:1, 2:0.98, 3:0.89, 4:0.84, 5:0.75, 6:0.61}
hear_dic = {1:1, 2:0.95, 3:0.89, 4:0.8, 5:0.74, 6:0.61}
spe_dic = {1:1, 2:0.94, 3:0.89, 4:0.81, 5:0.68}
amb_dic = {1:1, 2:0.93, 3:0.86, 4:0.73, 5:0.65, 6:0.58}
dex_dic = {1:1, 2:0.95, 3:0.88, 4:0.76, 5:0.65, 6:0.56}
emo_dic = {1:1, 2:0.95, 3:0.85, 4:0.64, 5:0.46}
cog_dic = {1:1, 2:0.92, 3:0.95, 4:0.83, 5:0.6, 6:0.42}
pain_dic = {1:1, 2:0.96, 3:0.9, 4:0.77, 5:0.55}

#Calculating health score
score = (1.371*(vis_dic[vision]*hear_dic[hearing]*spe_dic[speech]*amb_dic[ambulation]*dex_dic[dexterity]*emo_dic[emotion]*cog_dic[cognition]*pain_dic[pain]))-0.371

print("Utility of Health State = ",score)
