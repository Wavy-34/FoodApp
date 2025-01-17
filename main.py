from food_app.Database.main import shw_databases
from food_app.consts import DATABASE_PASSWORD
from random import random

class ConnardVa(Exception):
    pass

def pile_ou_face() -> bool:
    n = random()
    if n > 0.5:
        print("Pile !")
        return True
    elif n < 0.5:
        print("Face !")
        return False
    else:
        print("WTF C'EST LA TRANCHE")
        raise ConnardVa("D'ou tu tombe sur la tranche mdrrrrr")
def main() -> None:
    pile_ou_face()
        

if __name__ == '__main__':
    main()