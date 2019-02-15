class Player:
    def __init__(self):
        self.life = 0
        self.nickname = ''
        self.value = 0

    def set_nickname(self):
        self.nickname = input("veuillez rentrer votre pseudo : ")

    def set_life(self):
        self.life = int(input("entrez un nombre de vie : "))

    def set_value(self):
        self.value = int(input("Entrez un chiffre entre 0 et 100 : "))


if __name__ == '__main__':
    player1 = Player()
    player1.set_nickname()
    player1.set_life()

