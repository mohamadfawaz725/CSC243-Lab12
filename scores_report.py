
records = []

try:
    with open("scores.txt", "r") as file:

        for line in file:
            name, score = line.split(",")

            try:
                score = int(score)
                records.append([name, score])

            except ValueError:
                continue

except FileNotFoundError:
    print("File not found.")



for record in records:
    if record[0] == "Karim":
        print(record[1])

print(len(records))




updated_records = []

for record in records:

    name = record[0]
    score = record[1]

    if name == "Nour":
        continue

    if name == "Maya":
        score = 88

    updated_records.append([name, score])



with open("scores.txt", "w") as file:

    for record in updated_records:
        file.write(f"{record[0]},{record[1]}\n")



with open("pass.txt", "w") as file:

    for record in updated_records:
        if record[1] >= 60:
            file.write(record[0] + "\n")
