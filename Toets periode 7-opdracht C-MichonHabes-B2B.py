def MichonHabes_B2B_gemiddelde(Cijfers):
    for naam, Cijferlijst in Cijfers.items():
        totaal = sum(Cijferlijst)
        gemiddelde = totaal / len(Cijferlijst)
        print(f"{naam} heeft de volgende cijfers behaald:\n{Cijferlijst}\nMet een gemiddelde van: {gemiddelde:.2f}\n")

Cijfers = {}
while True:
    naam = input("Enter the student's name (press Enter to stop): ")
    if not naam:
        break
    Cijferlijst = []
    while True:
        cijfer = input("Enter the student's score (0-10) (press Enter to stop): ")
        if not cijfer:
            break
        Cijferlijst.append(float(cijfer))
    Cijfers[naam] = Cijferlijst

if not Cijfers:
    print("Er zijn geen cijfers.")
else:
    MichonHabes_B2B_gemiddelde(Cijfers)
