Disks = int(input("Disks: "))

Moves = 1

for i in range(Disks - 1):
    Moves = Moves * 2 + 1

print("Moves:", Moves)