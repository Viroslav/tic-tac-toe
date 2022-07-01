from enum import Enum
import pygame


refresh_rate = 60
CELL_SIZE = 50


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Класс игрока, содержащий тип значков и имя
    """
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]


class GameFieldView:
    """
    Виджет игрового поля, который выясняет место клика, отображает поле на экране
    """
    def __init__(self, field):
        # загрузить значки, отобразить состяние клеток
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True  # TODO self._height = field.height * CELL_SIZE учесть

    def get_coords(self, x, y):
        return 0, 0  # TODO реально вычислить клетку клика


class GameRoundManager:
    """
    Манагер запускающий все процессы
    """
    def __init__(self, player_1: Player, player_2: Player):
        self._players = [player_1, player_2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        player = self._players[self._current_player]
        # игрок делает клик на поле
        print("Click handled", i, j)


class GameWindow:
    """
    Содержит виджет поля, а также менеджер игрового раунда.
    """

    def __init__(self):
        # инициализация pygame
        pygame.init()

        #Window
        self._height = 800
        self._width = 600
        self._title = " Cross-tie"
        self.screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        # Timer
        clock = pygame.time.Clock()
        refresh_rate = 60

        player_1 = Player("Петя", Cell.CROSS)
        player_2 = Player("Вася", Cell.ZERO)
        self._game_manager = GameRoundManager(player_1, player_2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def mainloop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)
            pygame.display.flip()

            clock.tick(refresh_rate)



def main():
    Window = GameWindow()
    Window.mainloop()
    print("game over")


if __name__ == "__main__":
    main()
