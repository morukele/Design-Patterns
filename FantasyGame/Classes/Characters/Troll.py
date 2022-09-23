from Classes.Characters.Character import Character
from Classes.Weapons.BowAndArrowBehavior import BowAndArrowBehavior


class Troll(Character):
    def __init__(self):
        super().__init__()
        self.weapon = BowAndArrowBehavior()