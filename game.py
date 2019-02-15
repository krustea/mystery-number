import random
import sqlite3
from player import Player


class Game:
    def __init__(self):
        self.value = 0
        self.player = Player()
        self.player.set_nickname()
        self.player.set_life()
        print('tu t\'appelles : ', self.player.nickname, ' et tu as :', self.player.life, 'vies')

    def set_random_value(self):
        self.value = random.randint(0, 100)

    def play(self):
        while self.player.value != self.value and self.player.life > 0:
            self.player.set_value()
            if self.player.value > self.value:
                self.player.life -= 1
                print("Trop grand, Try again!")
            elif self.player.value < self.value:
                self.player.life -= 1
                print("trop petit, try again")
            else:
                print("Bravo tu as trouvé")
        if self.player.life == 0:
            print("Tu n'as plus de vies...Game Over Man!!")

    def save_game(self):
        saves = open('high_score.txt', 'a')
        saves.write("Nom du joueur : {0}, score : {1} \n".format(self.player.nickname, self.player.life))
        saves.close

    def high_score(self):
        saves = open('high_score.txt', 'r')
        scores = saves.readlines()
        saves.close()
        for score in scores:
            print(score)

    def sql_high_score(self):
        cx = sqlite3.connect("ma_base_de_données.db3")
        cur = cx.cursor()
        cur.execute(
            "create table if not exists high_score(rowid integer primary key, nickname char(20), score integer )")
        cur.execute("insert into high_score (nickname, score) values(?,?)", (self.player.nickname, self.player.life))
        cx.commit()
        print("High Score:")
        cur.execute("select nickname, score from high_score order by score desc ")
        for row in cur:
            print(row[0], row[1])
        cx.close()
