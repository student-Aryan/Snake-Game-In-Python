import pygame
import pygame_gui
import random
import os

# Pre-initialize the mixer with desired settings
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
pygame.mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced Snake Game")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Snake settings
snake_block = 20
initial_snake_speed = 10

# Sound effects
EAT_SOUND = pygame.mixer.Sound("eat.wav")
GAME_OVER_SOUND = pygame.mixer.Sound("gameover.wav")

# Background music
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # Loop indefinitely

# High score file
HIGH_SCORE_FILE = "high_score.txt"

def load_high_score():
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    with open(HIGH_SCORE_FILE, "r") as f:
        return int(f.read())

def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

def Your_score(score):
    value = score_font.render("Score: " + str(score), True, YELLOW)
    screen.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        screen.blit(snake_segment_image, (x[0], x[1]))


def show_message(message, color, y_offset=0):
    mesg = font.render(message, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3 + y_offset])

    # Load and scale the food image
try:
    food_image = pygame.image.load("Food.png").convert_alpha()
    food_image = pygame.transform.scale(food_image, (snake_block, snake_block))
except pygame.error as e:
    print(f"Unable to load image: {e}")
    pygame.quit()
    exit()


    # Load and scale the snake segment image
try:
    snake_segment_image = pygame.image.load("snake.png").convert_alpha()
    snake_segment_image = pygame.transform.scale(snake_segment_image, (snake_block, snake_block))
except pygame.error as e:
    print(f"Unable to load image: {e}")
    pygame.quit()
    exit()

def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    snake_speed = initial_snake_speed

    foodx = round(random.randrange(0, WIDTH - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, HEIGHT - snake_block) / snake_block) * snake_block

    high_score = load_high_score()

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            screen.fill(BLUE)
            show_message("You Lost! Press C-Play Again or Q-Quit", RED)
            final_score = length_of_snake - 1
            score_surface = score_font.render(f"Final Score: {final_score}", True, YELLOW)
            screen.blit(score_surface, [WIDTH // 2 - 100, HEIGHT // 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            GAME_OVER_SOUND.play()
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)
        screen.blit(food_image, (foodx, foody))
       
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                GAME_OVER_SOUND.play()
                game_close = True

        draw_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            while True:
                foodx = round(random.randrange(0, WIDTH - snake_block) / snake_block) * snake_block
                foody = round(random.randrange(0, HEIGHT - snake_block) / snake_block) * snake_block
                if [foodx, foody] not in snake_list:
                    break
            length_of_snake += 1
            snake_speed += 1
            EAT_SOUND.play()

        clock.tick(snake_speed)

    final_score = length_of_snake - 1
    if final_score > high_score:
        save_high_score(final_score)

    pygame.quit()
    quit()

def main():
    running = True
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH//2 - 75, HEIGHT//2 - 25), (150, 50)),
                                                text='Start Game',
                                                manager=manager)

    while running:
        time_delta = clock.tick(60) / 1000.0
        screen.fill(WHITE)

        title_font = pygame.font.SysFont("comicsansms", 48)
        title_surface = title_font.render("Snake Game", True, BLUE)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 4))

        high_score = load_high_score()
        score_surface = font.render(f"High Score: {high_score}", True, BLACK)
        screen.blit(score_surface, (WIDTH // 2 - score_surface.get_width() // 2, HEIGHT // 4 + 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        game_loop()

            manager.process_events(event)

        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.update()

main()