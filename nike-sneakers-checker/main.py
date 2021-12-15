from browser import chrome

from login import login


def main():
    with chrome:
        login(chrome)


main()
