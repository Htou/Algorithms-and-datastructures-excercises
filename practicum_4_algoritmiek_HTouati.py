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
