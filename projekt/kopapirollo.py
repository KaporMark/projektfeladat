import random

while True:
    user = input("Válassz! (kő, papír, olló): ")
    lehet_actions = ["kő", "papír", "olló"]
    computer = random.choice(lehet_actions)
    print(f"\nTe választásod {user}, gép választása {computer}.\n")

    if user == computer:
        print(f"Mindkét játékos a {user}-t választotta. Egyenlő!")
    elif user == "kő":
        if computer == "olló":
            print("Kő leveri az ollót! Nyertél!")
        else:
            print("Papír leveri a követ! Vesztettél.")
    elif user == "papír":
        if computer == "kő":
            print("Papír leveri a követ! Nyertél!")
        else:
            print("Olló leveri a papírt! Vesztettél.")
    elif user == "olló":
        if computer == "papír":
            print("Olló leveri a papírt! Nyertél!")
        else:
            print("Kő leveri az ollót! Vesztettél!")

    ujra = input("Újra? (y/n): ")
    if ujra.lower() != "y":
        break