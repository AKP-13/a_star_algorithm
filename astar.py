import pygame
import math
from queue import PriorityQueue

# Setting up the display
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

# Pre-defining colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# For each spot or node on the screen


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # Get position of each spot
    def get_pos(self):
        return self.row, self.col

    # If the spot is closed, i.e. we've already looked at it
    def is_closed(self):
        return self.color == RED

    # If in the open set
    def is_open(self):
        return self.color == GREEN

    # Barrier
    def is_barrier(self):
        return self.color == BLACK

    # Start color
    def is_start(self):
        return self.color == ORANGE

    # End color
    def is_end(self):
        return self.color == TURQUOISE

    # Change color back to white
    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        # Draw a cube
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    # Check neighbours, if not barriers, add to neighbors list
    def update_neighbors(self, grid):
        self.neighbors = []
        # Down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # Up
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # Right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # Left
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


# Manhattan distance for heuristic function
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def algorithm(draw, grid, start, end):
    count = 0

    # PriorityQueue is a efficient way to get the smallest element every time out of it
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    # G Score keeps track of the current shortest distance to get from start to this node
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    # F Score keeps track of our predicted distance from this node to the end node
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            # If you quit window, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        # If we're at the end, we're done
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        # If not at end, calculate neighbors' g scores
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            # If temp g score of neighbors less than g score in table, update g score to new better one
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                    h(neighbor.get_pos(), end.get_pos())

                # Then add to open set hash if not already in there
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


# Make the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


# Draw grid lines
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


# Draw everything
def draw(win, grid, rows, width):
    # Fill entire screen with white, then paint over with lines etc.
    win.fill(WHITE)

    # Draw all spots
    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    # 'Take whatever we've done and update that on the grid'
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


# Main loop, determine all of the checks like spot colour etc.
def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    # Initial start and end position
    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            # Stop running the game if we quit
            if event.type == pygame.QUIT:
                run = False

            # Left mouse click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                # If the spot you click on is not the start or end spot, make it the start spot
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            # Right mouse click
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                # Reset start and spot
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                # If we press space, start algorithm
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, width),
                              grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()


main(WIN, WIDTH)
