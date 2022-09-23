from Interfaces.WeaponBehavior import WeaponBehavior


class Character:
    def __init__(self):
        self.weapon = WeaponBehavior

    def fight(self):
        self.weapon.useWeapon()

    def setWeapon(self, w: WeaponBehavior):
        self.weapon = w

