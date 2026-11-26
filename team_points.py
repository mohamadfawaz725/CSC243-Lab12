
def points_by_team(scores, teams):

    result = {}

    for team in teams:

        total = 0

        for player in teams[team]:
            total += scores[player]

        result[team] = total

    return result


scores = {}
teams = {}

with open("players.txt", "r") as file:

    for line in file:

        if line == "":
            continue

        name, point, team = line.split()

        scores[name] = int(point)

        if team not in teams:
            teams[team] = []

        teams[team].append(name)


print("Scores:", scores)
print("Teams:", teams)

print("Points by team:", points_by_team(scores, teams))
