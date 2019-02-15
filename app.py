from game import Game

if __name__ == '__main__':

    game = Game()
    game.set_random_value()
    game.play()
    game.save_game()
    game.sql_high_score()
