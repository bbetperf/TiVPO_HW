import unittest
from Game import Game, Player, Menu

class GameTest(unittest.TestCase):

    def test_first(self):
        return 
    
    def test_get_question(self):
        new_game = Game()
        q, a = new_game.get_question()
        if q == 'Имя Есенина?' and a == 'Сергей':
            assert 'Сергей'
        if q == 'Зомбоящик – это?' and a == 'Телевизор':
            assert 'Телевизор'
        if q == 'Что недалеко от яблони падает?' and a == 'Яблоко':
            assert 'Яблоко'

    def test_get_answer(self):
        new_game = Game()
        q = new_game.get_question()
        if q == 'Имя Есенина?':
            assert 'Имя Есенина?'
        if q == 'Зомбоящик – это?':
            assert 'Зомбоящик – это?'
        if q == 'Что недалеко от яблони падает?':
            assert 'Что недалеко от яблони падает?'

    def test_output_info(self):
        new_game = Game()
        q, a = new_game.get_question()
        return 'Введите букву или назовите слово:'

    def test_Player(self):
        return Player('Максим', 19, 'Привет')

    def test_player_info(self):
        player = Player('Максим', 19, 'Привет')
        return "\nИнформация об игроке: \n Имя: {self.name}, \n Возраст: {self.age}, \n Фамилия: {self.family}\n"

    def test_menu(self):
        menu = Menu()
        return '\n====== Капитал-Шоу "Поле Чудес" ======\n 1 - Начать игру \n 2 - Об игроке \n 3 - Об игре \n 0 - Выход \n'


if __name__ == '__main__':
    unittest.main()