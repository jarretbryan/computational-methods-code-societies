sensations = open("sensations.txt")

myLines = []

# for line in sensations:
#     if "i" in line:
#         print("there is no I in team: " + line)
#     else:
#         print("teamwork!:" + line)



for line in sensations:
    if 'MUSIC' in line:
        print(line)
        myLines.append(line.upper())
    else:
        myLines.append(line.lower())

# print(myLines)