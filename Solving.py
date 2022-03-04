Disks = int(input("Disks: "))
Moves = 0
AllMoves = 1
Length = Disks * 2 + 4

Towers = {
    "A": [],
    "B": [],
    "C": [],
}

def PossibleMoves():
    PossibleMoves = 1
    for _ in range(Disks - 1): PossibleMoves = PossibleMoves * 2 + 1
    return PossibleMoves

def PrintShape():
    FinalText = ""
    for i in reversed(range(Disks + 2)):
        if i > len(Towers["A"]) - 1: FinalText += "\n" + ("||").center(Length) + " "
        else: FinalText += "\n" + ("==" * Towers["A"][i]).center(Length) + " "
        
        if i > len(Towers["B"]) - 1: FinalText += ("||").center(Length) + " "
        else: FinalText += ("==" * Towers["B"][i]).center(Length) + " "
        
        if i > len(Towers["C"]) - 1: FinalText += ("||").center(Length)
        else: FinalText += ("==" * Towers["C"][i]).center(Length)

    print(
        f"{FinalText}"
        f"\n{('-' * Length)} {('-' * Length)} {('-' * Length)}"
        f"\n{Moves}/{AllMoves} - {round(Moves * 100 / AllMoves, 3)} %", end="\r"
    )

def ChangeShape(FromTower, ToTower):
    global Moves
    Towers[ToTower].append(Towers[FromTower].pop())
    Moves += 1
    PrintShape()

def Hanoi(Disks, FromTower, ToTower, TargetTower):
    if Disks == 1:
        ChangeShape(FromTower, ToTower)
        return
    Hanoi(Disks - 1, FromTower, TargetTower, ToTower)
    ChangeShape(FromTower, ToTower)
    Hanoi(Disks - 1, TargetTower, ToTower, FromTower)


for i in range(Disks): Towers["A"].append(Disks - i)
PrintShape()
AllMoves = PossibleMoves()
Hanoi(Disks, "A", "C", "B")
