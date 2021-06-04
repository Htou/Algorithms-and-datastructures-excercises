import random


def linear_search(lst, target):
    """ Bepaalt of *target* voorkomt in lijst *lst* door middel van lineair zoeken. """
    for i in lst:
        if target == i:
            return True
    return False


def linear_search_index(lst, target):
    """ Geeft de positie (m.a.w. index) van *target* in lijst *lst* d.m.v. lineair zoeken. """
    index = 0
    for i in lst:
        index += 1
        if target == i:
            return index - 1
    return -1


def linear_search_index_steps(lst, target):
    """
    Geeft de positie (m.a.w. index) van *target* in lijst *lst*
    d.m.v. lineair zoeken, en het aantal benodigde stappen.
    """
    # begin situatie: lst, target, index = 0, steps = 0
    #
    # door list itereren:
    # zolang i im lst < lengte lst:
    #   i +1
    #   steps +1

    # voor elke iteratie +1 op index && +1 op steps
    # Einddoel: functie retourneert postie van de index en aantal stappen

    index = 0
    steps = 0
    for i in lst:
        index += 1
        steps += 1
    return -1, steps
    # ik krijg hier geen testfeedback


def binary_search(lst, target):
    """ Bepaalt of *target* voorkomt in lijst *lst* door middel van binair zoeken. """
    # stap 1
    mini = 0
    maxi = len(lst)
    sortedlist = sorted(lst)

    # stap 6(!)
    while mini <= maxi:    # hoelang ga je door met zoeken?
        middle = int((mini + maxi) / 2)
        if lst[middle] == target:
            return True
        elif sortedlist[middle] < target:
            mini = middle + 1
        else:
            maxi = middle - 1
    return False


def binary_search_index(lst, target):
    """ Geeft de positie (m.a.w. index) van *target* in lijst *lst* d.m.v. binair zoeken. """
    mini = 0
    maxi = len(lst) - 1

    while mini <= maxi:
        index = (mini + maxi) // 2
        if lst[index] == target:
            return index
        if lst[index] < target:
            mini = index + 1
        if lst[index] > target:            
            maxi = index - 1
    return -1

def binary_search_index_steps(lst, target):
    """
    Geeft de positie (m.a.w. index) van *target* in lijst *lst* d.m.v. binair zoeken,
    en het aantal benodigde stappen.
    """
    steps = 0
    mini = 0
    maxi = len(lst) - 1
    
    while mini <= maxi:
        steps += 1
        index = (mini + maxi) // 2
        if lst[index] == target:
            mini = index + 1
        if lst[index] > target:
            maxi = index - 1
    return (-1, steps)


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def test_linear_search():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.randrange(20)
        assert linear_search(lst_test, target) == (target in lst_test), "Fout: linear_search({}, {}) geeft {} in plaats van {}".format(
            lst_test, target, linear_search(lst_test, target), target in lst_test)


def test_linear_search_index():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.choice(lst_test)
        assert linear_search_index(lst_test, target) == lst_test.index(target), "Fout: linear_search_index({}, {}) geeft {} in plaats van {}".format(
            lst_test, target, linear_search_index(lst_test, target), lst_test.index(target))

        lst_test = [0, 1, 2]
        assert linear_search_index(lst_test, 3) == -1, "Fout: linear_search_index({}, {}) geeft {} in plaats van {}".format(
            lst_test, 3, linear_search_index(lst_test, 3), -1)


def test_linear_search_index_steps():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.choice(lst_test)
        assert linear_search_index_steps(lst_test, target)[0] == lst_test.index(target), "Fout: linear_search_index_steps({}, {}) geeft {} in plaats van {}".format(
            lst_test, target, linear_search_index_steps(lst_test, target)[0], lst_test.index(target))


def test_binary_search():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.randrange(20)
        assert binary_search(lst_test, target) == (target in lst_test), "Fout: binary_search({}, {}) geeft {} in plaats van {}".format(
            lst_test, target, binary_search(lst_test, target), target in lst_test)


def test_binary_search_index():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.choice(lst_test)
        assert binary_search_index(lst_test, target) == lst_test.index(target), "Fout: binary_search_index({}, {}) geeft {} in plaats van {}".format(
            lst_test, target, binary_search_index(lst_test, target), lst_test.index(target))

        lst_test = [0, 1, 2]
        assert binary_search_index(lst_test, 3) == -1, "Fout: binary_search_index({}, {}) geeft {} in plaats van {}".format(
            lst_test, 3, binary_search_index(lst_test, 3), -1)


def test_binary_search_index_steps():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.choice(lst_test)
        assert binary_search_index_steps(lst_test, target)[0] == lst_test.index(target), "Fout: binary_search_index_steps({}, {}) geeft {} in plaats van {}".format(
            lst_test, target, binary_search_index_steps(lst_test, target)[0], lst_test.index(target))


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_linear_search()
        print("Je functie linear_search() werkt goed!")

        test_linear_search_index()
        print("Je functie linear_search_index() werkt goed!")

        test_binary_search()
        print("Je functie binary_search() werkt goed!")

        test_binary_search_index()
        print("Je functie binary_search_index() werkt goed!")

        test_linear_search_index_steps()
        print("Je functie linear_search_index_steps() werkt goed!")

        test_binary_search_index_steps()
        print("Je functie binary_search_index_steps() werkt goed!")

        print("\x1b[0;30m")
        size = int(input("Geef een grootte voor de lijst: "))
        lst_test = list(range(size))
        print("Ik ga zoeken in:", lst_test)
        tgt = int(input("Geef een getal: "))

        (idx, cnt) = linear_search_index_steps(lst_test, tgt)
        print("Het lineair zoekalgoritme vond '" + str(tgt) +
              "' op positie '" + str(idx) + "' na " + str(cnt) + " stappen.")

        (idx, cnt) = binary_search_index_steps(lst_test, tgt)
        print("Het binair zoekalgoritme vond '" + str(tgt) +
              "' op positie '" + str(idx) + "' na " + str(cnt) + " stappen.")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(str(ae))
