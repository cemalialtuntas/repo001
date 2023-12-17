class window_opt:
    def __init__(self, cell_size, grid_size, bg_color, grid_color, font_color):
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.width = self.height = cell_size * grid_size
        self.bg_color = bg_color
        self.grid_color = grid_color
        self.font_color = font_color

class gridobj:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class player:
    def __init__(self, last_grid, current_grid, current_number):
        self.last_grid = last_grid
        self.current_grid = current_grid
        self.current_number = current_number