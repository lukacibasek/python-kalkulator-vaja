def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deljenje(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Deljenje z 0 je nemogoče."
    
zgodovina = []

def dodaj_v_zgodovino(zgodovina, zapis):
    zgodovina.append(zapis)

    if len(zgodovina) > 3:
        zgodovina.pop(0)

def izpisi_zgodovino(zgodovina):
    print("Zadnji izračuni:")

    if len(zgodovina) == 0:
        print("Ni še izračunov.")
    else:
        for z in zgodovina:
            print(z)

while True:
    
    print("Pozdrav! Mini kalkulator")
    print("0 = izhod")
    print("1 = seštevanje")
    print("2 = odštevanje")
    print("3 = množenje")
    print("4 = deljenje")

    izbira = input("Kaj želiš narediti? (1 ali 2): ")

    if izbira == "1":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        rez = sestej(x, y)
        print(f"Rezultat: {rez}")

        zapis = f"{x} + {y} = {rez}"
        dodaj_v_zgodovino(zgodovina, zapis)

        izpisi_zgodovino(zgodovina)
    elif izbira == "2":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        rez = odstej(x, y)
        print(f"Rezultat: {rez}")

        zapis = f"{x} - {y} = {rez}"
        dodaj_v_zgodovino(zgodovina, zapis)

        izpisi_zgodovino(zgodovina)

    elif izbira == "3":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        rez = pomnozi(x, y)
        print(f"Rezultat: {rez}")

        zapis = f"{x} * {y} = {rez}"
        dodaj_v_zgodovino(zgodovina, zapis)

        izpisi_zgodovino(zgodovina)

    elif izbira == "4":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        rez = deljenje(x, y)
        print(f"Rezultat: {rez}")

        zapis = f"{x} / {y} = {rez}"
        dodaj_v_zgodovino(zgodovina, zapis)

        izpisi_zgodovino(zgodovina)

    elif izbira == "0":
        break

    else:
        print("Neveljavna izbira!")