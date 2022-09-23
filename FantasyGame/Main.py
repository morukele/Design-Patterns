from Classes.Characters.King import King
from Classes.Characters.Troll import Troll

from Classes.Weapons.AxeBehavior import AxeBehavior


def main():
    king = King()
    king.fight()
    king.setWeapon(w=AxeBehavior())
    king.fight()

    troll = Troll()
    troll.fight()


if __name__ == "__main__":
    main()
