l = "NAAEF BQDYUF FKBUOMX DQNGUXP"
for i in range(26):
    print(f"{i = }")
    print("".join([(chr((ord(c) + i - 65) % 26 + 65) if c != " " else " ") for c in l]))
    print()


with open("register.py.txt", "w") as f:
    i = +3
    for i in range(26):
        f.write("\n")
        f.write("".join([(chr((ord(c) + i - 65) % 26 + 65) if c != " " else " ") for c in l]))