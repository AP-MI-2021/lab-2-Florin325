def is_prime(n):
    """

    :param n:  numar natural
    :return: True daca numarul n este prim si False daca numarul n nu este prim
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, n // 2, 2):
        if n % d == 0:
            return False
    return True
    # algoritmul pentru determinarea faptului ca n este prim consta in a verifica daca acesta are divizori
    # deoarece n este numar natural divizorii pot fi numai intre 2 si n//2
    # pentru a face algoritmul mai eficient am adaugat conditia ca n sa fie impar


def get_goldbach(n):
    """

    :param n: n numar natural
    :return: scrierea numarului n ca suma de 2 numere prime
    """

    for i in range(2, n):
        if is_prime(i):
            if is_prime(n - i):
                return i, n - i
    return False
    # gasim ce numere i mai mici decat n sunt prime
    # verificam apoi daca n-i este si el prim
    # returnam false daca nu exista o astfel de scriere


def test_get_goldbach():
    assert get_goldbach(8) == (3, 5)
    assert get_goldbach(16) == (3, 13)
    assert get_goldbach(15) == (2, 13)
    assert get_goldbach(27) is False
    # daca n este par vom gasi intotdeauna o scriere a lui n ca suma de 2 numere prime
    # daca n este impar de forma nr prim+2 vom gasi o scriere
    # acestea sunt singurele cazuri in care algoritmul va gasi o scriere


def is_palindrome(n):
    tmp = n
    inv = 0
    while tmp != 0:
        inv = 10 * inv + tmp % 10
        tmp = tmp//10
    if inv == n:
        return True
    return False
    # pentru a putea compara la sfarsit n si inversul sau a calculat inversul dintr-o copie a lui n
    # algoritmul din while aranjeaza cifrele lui n in sens invers


def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(1331) is True
    assert is_palindrome(134) is False


def main():
    test_is_palindrome()
    test_get_goldbach()


if __name__ == "__main__":
    main()
