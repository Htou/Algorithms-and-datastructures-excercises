""" coding=utf-8

Analytical Skills
Practicum 4: algoritmiek

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Naam: Hichem Touati
Klas: V1A
Studentnummer: 1771690


Opdracht: beantwoord onderstaande vragen en werk onderstaande functies uit.

Je kunt je functies testen met het gegeven raamwerk door het bestand uit te voeren (of met behulp
van pytest, als je weet hoe dat werkt). Lever je werk in op Canvas als alle tests slagen.

Let op! Je mag voor deze opdracht geen extra modules importeren met 'import'.
"""
"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die de lijst aanneemt bij álle tussenstappen bij
        toepassing van bovenstaand sorteeralgoritme.

        [antwoord]
        
        [4, 3, 1, 2]
        [3, 4, 1, 2]
        [3, 1, 4, 2]
        [3, 1, 2, 4]
        [1, 3, 2, 4]
        [1, 2, 3, 4]


    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie genaamd  my_sort(lst).


    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het snelste klaar (best-case scenario)? Hoeveel vergelijkingen (zoals beschreven
            in stap 1. van de pseudocode) zijn nodig geweest?
            

        [antwoord]
        [1, 2, 3]
        3 vergelijkingen
        

        -   Bij welke volgorde van de waarden in de lijst is het sorteeralgoritme het minst snel klaar
            (worst-case scenario)? Hoeveel vergelijkingen zijn nodig geweest?

        [antwoord]
        [3, 2, 1]
        3 vergelijkingen
        
        

        

        -   Stel je hebt een lijst met de waarden 1 tot en met 4. Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario? Hoeveel vergelijkingen zijn er nodig?

        [antwoord]
        best-case scenario: als de lijst al gesorteerd is [1, 2, 3, 4], dan zijn er 6 vergelijkingen
        worst-case scenario: als de lijst met waarde [4, 3, 2, 1] is, dan zijn er ook 6 vergelijkingen

        -   Stel je hebt een lijst met de waarden 1 tot en met n (je weet nu dus niet precies hoeveel waarden er in de
            lijst zitten, het zijn er 'n'). Wat is nu het best-case scenario? Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario? Hoeveel vergelijkingen zijn er nodig?

        [antwoord]
        De best-case senario is dat de lijst al gesorteerd is, Dan zijn er N aantal vegelijkingen nodig, waar N de aantal elementen in is in de lijst: dus [1, 2, 3, 4, 5, 6, 7 ... enzovoort]
        De worst-case scenario is dat de lijst in tegenovergestelde volgorde is gesorteerd van de bestcase scenario, dan zijn er N^2  vergelijkingen nodig.
        
        



2.  Recursie

    2a. Lineair zoeken
        Implementeer het lineair zoekalgoritme in Python op een *recursieve* manier. Maak hiervoor de functie genaamd
        linear_search_recursive(lst, target).


    2b. Binair zoeken
        Implementeer het binair zoekalgoritme in Python op een *recursieve* manier. Maak hiervoor de functie genaamd
        binary_search_recursive(lst, target).
"""


def my_sort(lst):
    """
    Sorteert gegeven lijst lst volgens het algoritme zoals beschreven in de pseudocode bij 1. hierboven.
    De sortering vind 'in place' plaats, met andere woorden: de gegeven lijst lst wordt *zelf* gemuteerd. Er is
    geen return-waarde.
    """
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                continue
    return None


def linear_search_recursive(lst, target):
    """
    Zoekt een element in gegeven lijst door middel van recursief lineair zoeken.

    Argumenten:
    lst -- de lijst waarin gezocht wordt (list)
    target -- het element dat gezocht wordt

    Retourneert of het element in de lijst voorkomt (bool)
    """
    if len(lst) == 0:
        return False
    if lst[0] == target:
        return True
    else:
        lst.pop(0)
    return linear_search_recursive(lst, target)


def binary_search_recursive(lst, target):
    """
    Zoekt een element in gegeven lijst door middel van recursief binair zoeken.

    Argumenten:
    lst -- de lijst waarin gezocht wordt (list)
    target -- het element dat gezocht wordt

    Retourneert of het element in de lijst voorkomt (bool)
    """
    if len(lst) == 0:
        return False

    lst.sort()

    mini = 0
    maxi = len(lst)
    index = (mini + maxi) // 2

    if target == lst[index]:
        return True
    elif target > lst[index]:
        lst = lst[index + 1:maxi]
    else:
        lst = lst[0:index]
    return linear_search_recursive(lst, target)


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_my_sort():
    lst_test = random.sample(range(-99, 100), 6)
    lst_copy = lst_test.copy()
    my_sort(lst_test)
    assert lst_test == sorted(lst_copy), f"Fout: my_sort({lst_copy}) geeft {lst_test} in plaats van {sorted(lst_copy)}"


def test_linear_search_recursive():
    for i in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        outcome = linear_search_recursive(lst_test, target)
        assert outcome == (target in lst_test), \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {target in lst_test}"


def test_binary_search_recursive():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        print(lst_test)
        outcome = binary_search_recursive(lst_test, target)
        assert outcome == (target in lst_test), \
            f"Fout: binary_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {target in lst_test}"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        print("Je functie linear_search_recursive() werkt goed!")

        test_binary_search_recursive()
        print("Je functie binary_search_recursive() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken! Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)
