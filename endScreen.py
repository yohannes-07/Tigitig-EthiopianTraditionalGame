import random as rand
import string
from startScreen import *
from globals import *

# game end screen function


def game_end(screen, clock, background_color, player_name):

    celeb_text = pygame.font.Font('AbyssinicaSIL-Regular.ttf', 140)
    large_text = pygame.font.Font('AbyssinicaSIL-Regular.ttf', 45)
    small_text = pygame.font.Font('AbyssinicaSIL-Regular.ttf', 30)

    while True:

        # to smoothly shine winning message
        delay = 0

        screen.fill(background_color)

        # set flashing colors
        color_x = rand.randint(0, 4)
        color_y = rand.randint(0, 1)

        # Get inputs
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            # Press R to reset game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return 1
            # Press M to go to menu
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                return 2
            # Press esc or Q to quit
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        
        if player_name == 'Player 1':
            winner  = 'አቤ'
        else:
            winner  = 'ከቤ'
        if delay == 0:
            disp_text(screen, "{0} ጀግና".format(winner), (width / 2, height / 2 - 150),
                      celeb_text, colors[color_x][color_y])
        # Drawing buttons for reset, menu and exit.
        # Reset button
        if abs(mouse_pos[0] - 200) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[0][0], (200, 470), "አዲስ ጨዋታ", large_text, (255, 255, 255),
                          (width / 2 - 400, height / 2 + 170))
            if mouse_press[0] == 1:
                return 1

        else:
            button_circle(screen, colors[0][0], (200, 470), "አዲስ ጨዋታ", small_text, (255, 255, 255),
                          (width / 2 - 400, height / 2 + 170))

        # Menu button
        if abs(mouse_pos[0] - 600) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[4][1], (600, 470), "አማራጭ", large_text, (255, 255, 255),
                          (width / 2, height / 2 + 170))
            if mouse_press[0] == 1:
                return 2

        else:
            button_circle(screen, colors[4][1], (600, 470), "አማራጭ", small_text, (255, 255, 255),
                          (width / 2, height / 2 + 170))

        # quit button
        if abs(mouse_pos[0] - 1000) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[1][1], (1000, 470), "ውጣ", large_text, (255, 255, 255),
                          (width / 2 + 400, height / 2 + 170))
            if mouse_press[0] == 1:
                pygame.quit()        
                return 3
        else:
            button_circle(screen, colors[1][0], (1000, 470), "ውጣ", small_text, (255, 255, 255),
                          (width / 2 + 400, height / 2 + 170))

        pygame.display.update()
        clock.tick(10)
