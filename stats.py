class Stats():
    """ Отслеживание статистики """

    def __init__(self):
        """ Инициализирует статистику """
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        """ Cменная статистика """
        self.guns_left = 2
        self.score = 0
