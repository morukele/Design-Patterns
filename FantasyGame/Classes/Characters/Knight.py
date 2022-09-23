from Classes.Characters.Character import Character
from Classes.Weapons.KnifeBehavior import KnifeBehavior


class Knight(Character):
    def __init__(self):
        super().__init__()
        self.weapon = KnifeBehavior()
