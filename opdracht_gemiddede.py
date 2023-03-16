# Importeer de benodigde libraries
import random

# Definieer een functie om een lijst met 10 willekeurige positieve getallen te maken
def create_list():
    lst = []
    for i in range(10):
        lst.append(random.randint(1, 100))
    return lst

# Definieer een functie om het gemiddelde van de getallen in een lijst te berekenen
def calculate_mean(lst):
    return sum(lst) / len(lst)

# Definieer een functie om het getal en de positie in de lijst te vinden dat het meeste afwijkt van het gemiddelde
def find_most_deviant(lst, mean):
    deviants = [(i, abs(x - mean)) for i, x in enumerate(lst)]
    return max(deviants, key=lambda x: x[1])

# Definieer een functie om een getal +/- 10% van zijn eigen waarde richting het gemiddelde te veranderen
def change_number(number, mean):
    if number > mean:
        return round(number * 0.9 + mean * 0.1)
    else:
        return round(number * 1.1 - mean * 0.1)

# Maak een lijst met 10 willekeurige positieve getallen
lst = create_list()

# Bepaal het gemiddelde van de getallen in de lijst
mean = calculate_mean(lst)

# Bepaal het getal en de positie in de lijst dat het meeste afwijkt van het gemiddelde
deviant_index, deviant_value = find_most_deviant(lst, mean)

# Verander dit getal +/- 10% van zijn eigen waarde richting het gemiddelde, totdat alle getallen binnen 20% van het gemiddelde vallen
while abs(deviant_value - mean) > mean * 0.2:
    lst[deviant_index] = change_number(lst[deviant_index], mean)
    mean = calculate_mean(lst)
    deviant_index, deviant_value = find_most_deviant(lst, mean)

# Print de resulterende lijst en het gemiddelde
print("Lijst:", lst)
print("Gemiddelde:", mean)
