import pygame
import sys
import random
import pygame
import sys
import random


# Initialize Pygame
pygame.init()
pygame.font.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris Start Up Page")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Fonts
font_title = pygame.font.Font(None, 48)
font_text = pygame.font.Font(None, 24)

# Texts
title_text = font_title.render("Tetris", True, black)
year_course_text = font_text.render("Year: 2023", True, black)
students_text = font_text.render("Producer: Dawn", True, black)
play_text = font_text.render("Play", True, white)
configure_text = font_text.render("Configure", True, white)
score_text = font_text.render("Top Scores", True, white)
exit_text = font_text.render("Exit", True, white)

# Buttons
button_width, button_height = 200, 50
play_button = pygame.Rect((screen_width - button_width) / 2, 290, button_width, button_height)
configure_button = pygame.Rect((screen_width - button_width) / 2, 360, button_width, button_height)
score_button = pygame.Rect((screen_width - button_width) / 2, 430, button_width, button_height)
exit_button = pygame.Rect((screen_width - button_width) / 2, 500, button_width, button_height)

def show_top_scores(screen):
    top_scores = [
        ("Player1", 500),
        ("Player2", 400),
        ("Player3", 300),
        ("Player4", 200),
        ("Player5", 100),
        ("Player6", 90),
        ("Player7", 80),
        ("Player8", 70),
        ("Player9", 60),
        ("Player10", 50)
    ]

    running_top_scores = True
    while running_top_scores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_top_scores = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    running_top_scores = False

        screen.fill(white)

        title_text = font_title.render("Top Scores", True, black)
        screen.blit(title_text, ((screen_width - title_text.get_width()) / 2, 50))

        y_offset = 150
        for rank, (player, score) in enumerate(top_scores, start=1):
            score_text = font_text.render(f"{rank}. {player}: {score}", True, black)
            screen.blit(score_text, ((screen_width - score_text.get_width()) / 2, y_offset))
            y_offset += 30

        pygame.draw.rect(screen, black, exit_button)
        screen.blit(exit_text,
                    (exit_button.centerx - exit_text.get_width() / 2, exit_button.centery - exit_text.get_height() / 2))

        pygame.display.flip()

    return  # Return control to the startup page loop

def show_configure_page(screen):
    configure_settings = {
        "Size of the field": "Normal",
        "Game level": "Medium",
        "Game type": "Normal",
        "Game mode": "Player"
    }

    running_configure = True
    while running_configure:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_configure = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    running_configure = False

        screen.fill(white)

        title_text = font_title.render("Configure", True, black)
        screen.blit(title_text, ((screen_width - title_text.get_width()) / 2, 50))

        y_offset = 150
        for setting, value in configure_settings.items():
            setting_text = font_text.render(f"{setting}: {value}", True, black)
            screen.blit(setting_text, ((screen_width - setting_text.get_width()) / 2, y_offset))
            y_offset += 30

        pygame.draw.rect(screen, black, exit_button)
        screen.blit(exit_text,
                    (exit_button.centerx - exit_text.get_width() / 2, exit_button.centery - exit_text.get_height() / 2))

        pygame.display.flip()

    return  # Return control to the startup page loop
def show_quit_dialog(screen):
    font = pygame.font.Font(None, 36)
    dialog_text = font.render("Do you want to end the game?", True, black)
    yes_text = font.render("Yes", True, white)
    no_text = font.render("No", True, white)

    dialog_rect = dialog_text.get_rect(center=(screen_width // 2, screen_height // 2))
    yes_button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 40, 100, 40)
    no_button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 90, 100, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button_rect.collidepoint(event.pos):
                    return True  # End the game
                elif no_button_rect.collidepoint(event.pos):
                    return False  # Continue the game

        screen.fill(white)
        pygame.draw.rect(screen, black, dialog_rect, border_radius=10)
        screen.blit(dialog_text, dialog_rect.topleft)
        pygame.draw.rect(screen, black, yes_button_rect)
        pygame.draw.rect(screen, black, no_button_rect)
        screen.blit(yes_text, yes_button_rect.topleft)
        screen.blit(no_text, no_button_rect.topleft)
        pygame.display.flip()

def startGame():
    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0

    pressing_down = False

    while not done:
        # Create a new block if there is no moving block
        if game.block is None:
            game.new_block()
        if game.nextBlock is None:
            game.next_block()
        counter += 1  # Keeping track if the time
        if counter > 100000:
            counter = 0

        # Moving the block continuously with time or when down key is pressed
        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.moveDown()
                # Checking which key is pressed and running corresponding function
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            game.rotate()
                        if event.key == pygame.K_DOWN:
                            game.moveDown()
                        if event.key == pygame.K_LEFT:
                            game.moveHoriz(-1)
                        if event.key == pygame.K_RIGHT:
                            game.moveHoriz(1)
                        if event.key == pygame.K_SPACE:
                            game.moveBottom()
                        if event.key == pygame.K_ESCAPE:
                            response = show_quit_dialog(screen)
                            if response:
                                game.__init__(20, 10)  # Reset the game
                                return
                            else:
                                continue  # Continue the game

        screen.fill('#FFFFFF')

        # Updating the game board regularly
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, '#B2BEB5',
                                 [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, shapeColors[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2,
                                      game.zoom - 1])

        # Updating the board with the moving block
        if game.block is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.block.image():
                        pygame.draw.rect(screen, shapeColors[game.block.color],
                                         [game.x + game.zoom * (j + game.block.x) + 1,
                                          game.y + game.zoom * (i + game.block.y) + 1,
                                          game.zoom - 2, game.zoom - 2])

        # Showing the score
        font = pygame.font.SysFont('Calibri', 40, True, False)
        font1 = pygame.font.SysFont('Calibri', 25, True, False)
        student_group = font.render("Group Number : 21", True, '#000000')

        lines_eliminated = font.render("Lines eliminated :", True, '#000000')
        current_level = font.render("Current Level: 1", True, '#000000')
        game_mode = font.render("Game mode : Normal", True, '#000000')
        play_mode = font.render("Play mode : Player", True, '#000000')

        text = font.render("Current Score: " + str(game.score), True, '#000000')
        text_game_over = font.render("Game Over", True, '#000000')
        text_game_over1 = font.render("Press ESC", True, '#000000')

        # Position the text vertically
        text_group_rect = student_group.get_rect(center=(width // 1.4, 30))
        text_score_rect = text.get_rect(center=(width // 1.4, 60))
        lines_eliminated_rect = lines_eliminated.get_rect(center=(width // 1.4, 90))
        current_level_rect = current_level.get_rect(center=(width // 1.4, 120))

        game_mode_rect = game_mode.get_rect(center=(width // 1.4, 150))
        play_mode_rect = play_mode.get_rect(center=(width // 1.4, 180))

        #render the current Information on right side
        screen.blit(student_group, text_group_rect)
        screen.blit(text, text_score_rect)
        screen.blit(lines_eliminated, lines_eliminated_rect)
        screen.blit(current_level, current_level_rect)
        screen.blit(game_mode, game_mode_rect)
        screen.blit(play_mode, play_mode_rect)

        # Ending the game if state is gameover
        if game.state == "gameover":
            screen.blit(text_game_over, [300, 200])
            screen.blit(text_game_over1, [300, 265])

        game.draw_next_block(screen)

        pygame.display.flip()
        clock.tick(fps)

# ... (Your Tetris game code)
# Shapes of the blocks
shapes = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[4, 5, 9, 10], [2, 6, 5, 9]],
    [[6, 7, 9, 10], [1, 5, 6, 10]],
    [[2, 1, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
]
# Colors of the blocks
shapeColors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# GLOBALS VARS
width = 700
height = 600
gameWidth = 100  # meaning 300 // 10 = 30 width per block
gameHeight = 400  # meaning 600 // 20 = 20 height per blo ck
blockSize = 20

topLeft_x = (width - gameWidth) // 2
topLeft_y = height - gameHeight - 50


class Block:
    x = 0
    y = 0
    n = 0

    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.type = n
        self.color = n
        self.rotation = 0

    def image(self):
        return shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(shapes[self.type])


class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    zoom = 20
    x = 100
    y = 60
    block = None
    nextBlock = None

    # Sets the properties of the board
    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    # Creates a new block
    def new_block(self):
        self.block = Block(3, 0, random.randint(0, len(shapes) - 1))

    def next_block(self):
        self.nextBlock = Block(3, 0, random.randint(0, len(shapes) - 1))

    # Checks if the blocks touch the top of the board
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    if i + self.block.y > self.height - 1 or \
                            j + self.block.x > self.width - 1 or \
                            j + self.block.x < 0 or \
                            self.field[i + self.block.y][j + self.block.x] > 0:
                        intersection = True
        return intersection

    # Checks if a row is formed and destroys that line
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def draw_next_block(self, screen):

        font = pygame.font.SysFont("Calibri", 30)
        label = font.render("Next Shape", 1, (128, 128, 128))

        sx = topLeft_x + gameWidth + 50
        sy = topLeft_y + gameHeight / 2 - 100
        format = self.nextBlock.image()
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.nextBlock.image():
                    pygame.draw.rect(screen, shapeColors[self.nextBlock.color], (sx + j * 30, sy + i * 30, 30, 30), 0)

    # Moves the block to the bottom
    def moveBottom(self):
        while not self.intersects():
            self.block.y += 1
        self.block.y -= 1
        self.freeze()

    # Moves the block down by a unit
    def moveDown(self):
        self.block.y += 1
        if self.intersects():
            self.block.y -= 1
            self.freeze()

    # This function runs once the block reaches the bottom.
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    self.field[i + self.block.y][j + self.block.x] = self.block.color
        self.break_lines()  # Checking if any row is formed
        self.block = self.nextBlock
        self.next_block()  # Creating a new block
        if self.intersects():  # If blocks touch the top of the board, then ending the game by setting status as gameover
            self.state = "gameover"

    # This function moves the block horizontally
    def moveHoriz(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.intersects():
            self.block.x = old_x

    # This function rotates the block
    def rotate(self):
        old_rotation = self.block.rotation
        self.block.rotate()
        if self.intersects():
            self.block.rotation = old_rotation


pygame.font.init()

# Main loop
running_startup = True
while running_startup:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_startup = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                running_startup = False  # Exit the startup page loop to start the game
                startGame()  # Call the startGame function to begin the game
            elif score_button.collidepoint(event.pos):
                show_top_scores(screen)  # Show the top score page
            elif configure_button.collidepoint(event.pos):
                show_configure_page(screen)  # Show the configure page
            elif exit_button.collidepoint(event.pos):
                pygame.quit()  # Close the entire program when Exit button is clicked
                sys.exit()  # Exit the Python script






    screen.fill(white)

    screen.blit(title_text, ((screen_width - title_text.get_width()) / 2, 100))
    screen.blit(year_course_text, ((screen_width - year_course_text.get_width()) / 2, 180))
    screen.blit(students_text, ((screen_width - students_text.get_width()) / 2, 230))

    pygame.draw.rect(screen, black, play_button)
    pygame.draw.rect(screen, black, configure_button)
    pygame.draw.rect(screen, black, score_button)
    pygame.draw.rect(screen, black, exit_button)

    screen.blit(play_text,
                (play_button.centerx - play_text.get_width() / 2, play_button.centery - play_text.get_height() / 2))
    screen.blit(configure_text, (configure_button.centerx - configure_text.get_width() / 2,
                                 configure_button.centery - configure_text.get_height() / 2))
    screen.blit(score_text,
                (score_button.centerx - score_text.get_width() / 2, score_button.centery - score_text.get_height() / 2))
    screen.blit(exit_text,
                (exit_button.centerx - exit_text.get_width() / 2, exit_button.centery - exit_text.get_height() / 2))

    pygame.display.flip()


pygame.quit()






screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris by Dawn")
run = True
while run:
    screen.fill((16, 57, 34))
    font = pygame.font.SysFont("Calibri", 70, bold=True)
    label = font.render("Press any key to begin!", True, '#FFFFFF')

    screen.blit(label, (10, 300))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            startGame()
pygame.quit()