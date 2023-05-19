import pygame
import random


pygame.init()

# Creating display
screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')



def main_menu():
    GREEN = (0,255,0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    FPS = 60
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)


    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        screen.blit(screen_text, [x, y])

    exit_menu = False
    menu_background = pygame.image.load('Data/menu_background.jpg')
    while not exit_menu:
        screen.fill(BLACK)
        screen.blit(menu_background, (80,5))
        text_screen('Press Enter to start Game!',GREEN,130,500)
        text_screen('Press Escape to exit Game!',RED,130,550)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_menu = True
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    exit_menu = True
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
        pygame.display.update()
        clock.tick(FPS)
    


#Game loop
def game_loop():
    # Game variables
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    game_over = False
    exit_game = False
    snake_x = 65
    snake_y = 100
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    #Button Block
    up = True # Block the double press
    down = True # Block the double press
    left = True # Block the double press
    right = True # Block the double press
    food_x = random.randint(60, screen_width/2)
    food_y = random.randint(120, screen_height/2)
    

    score = 0
    font = pygame.font.SysFont(None, 55)


    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        screen.blit(screen_text, [x, y])


    
    BACKGROUND = pygame.image.load('Data/background.jpg')
    snk_list = []
    snk_length = 1

    def print_snake(color, snk_list, snake_size):
        for x,y in snk_list:
            pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])

    FPS = 60
    clock = pygame.time.Clock()


    #Main Menu
    
        

    while not exit_game:
        with open('Data/high_score.txt', 'r') as f:
            high_score = f.read()
        screen.fill(WHITE)
        screen.blit(BACKGROUND,(0,0))
        #Line limiter 
        pygame.draw.line(screen,RED,(0,90),(900,90),7)
        pygame.draw.line(screen,RED,(0,90),(0,600),10)
        pygame.draw.line(screen,RED,(0,600),(900,600),10)
        pygame.draw.line(screen,RED,(900,90),(900,600),10)
        text_screen("High Score :" + high_score, RED, 10, 40)
        if snake_x <0 or snake_x > screen_width - 5 or snake_y > 600 or snake_y < 90 :
            game_over = True
        if game_over:
            screen.fill(BLACK)
            text_screen("Game Over! Press Enter to continue", RED , 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        run_game()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                    if right :
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0
                            left = False
                            up = True
                            down = True

                    if left:
                        if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0
                            right = False
                            up = True
                            down = True
                    if down:
                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0
                            up = False
                            right = True
                            left = True
                    if up:
                        if event.key == pygame.K_UP:
                            velocity_y = -init_velocity
                            velocity_x = 0
                            down = False
                            right = True
                            left = True
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                if int(score) > int(high_score) :
                    high_score = score
                    print(high_score)
                    with open('Data/high_score.txt', 'w') as f:
                        f.write(str(high_score))
                food_x = random.randint(60, screen_width/2)
                food_y = random.randint(95, screen_height/2)
                snk_length += 5

            snake_x += velocity_x
            snake_y += velocity_y
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
            
            text_screen("Press Esc to return to main menu",GREEN, 250,7)
            text_screen("Score : " + str(score), RED, 5, 5)
            # pygame.draw.rect(screen, BLACK, [snake_x, snake_y, snake_size, snake_size])
            print_snake(WHITE, snk_list, snake_size)
            pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()





def run_game():
    if main_menu():
        game_loop()
    else :
        exit()

run_game()