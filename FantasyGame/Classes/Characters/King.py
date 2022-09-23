from Classes.Characters.Character import Character
from Classes.Weapons.SwordBehavior import SwordBehavior


class King(Character):
    def __init__(self):
        super().__init__()
        self.weapon = SwordBehavior()
