from Interfaces.QuackBehaviour import QuackBehaviour


class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<< Silence >>")
