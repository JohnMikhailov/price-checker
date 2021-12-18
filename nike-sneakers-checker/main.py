from browser import chrome

from login import login
from draw import play


def main():
    with chrome:
        login(chrome)
        play(chrome)


main()
