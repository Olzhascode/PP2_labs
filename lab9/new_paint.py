import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Canvas
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

colors = {"red": RED, "blue": BLUE, "green": GREEN, "erase": WHITE}
color = "red"

# Modes
radius = 10
mouse_down = False
running = True
starting_position = None
last_position = None

mode_draw = "Draw"
mode_rect = "Rect"
mode_circle = "Circle"
mode_square = "Square"
mode_right_triangle = "Right_Triangle"
mode_equilateral_triangle = "Equilateral_Triangle"
mode_rhombus = "Rhombus"
mode = mode_draw  # default mode

# Main Loop
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Colors
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = "red"
            elif event.key == pygame.K_g:
                color = "green"
            elif event.key == pygame.K_b:
                color = "blue"
            elif event.key == pygame.K_e:
                color = "erase"
            elif event.key == pygame.K_c:
                canvas.fill(WHITE)
            elif event.key == pygame.K_1:
                mode = mode_draw
            elif event.key == pygame.K_2:
                mode = mode_circle
            elif event.key == pygame.K_3:
                mode = mode_rect
            elif event.key == pygame.K_4:
                mode = mode_square
            elif event.key == pygame.K_5:
                mode = mode_right_triangle
            elif event.key == pygame.K_6:
                mode = mode_equilateral_triangle
            elif event.key == pygame.K_7:
                mode = mode_rhombus
        # Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            starting_position = event.pos
            last_position = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            if starting_position:
                end_position = event.pos
                width = abs(end_position[0] - starting_position[0])
                height = abs(end_position[1] - starting_position[1])
                
                if mode == mode_rect:
                    rect = pygame.Rect(min(starting_position[0], end_position[0]),
                                       min(starting_position[1], end_position[1]),
                                       width, height)
                    pygame.draw.rect(canvas, colors[color], rect, 2)
                elif mode == mode_circle:
                    rect = pygame.Rect(min(starting_position[0], end_position[0]),
                                       min(starting_position[1], end_position[1]),
                                       width, height)
                    pygame.draw.ellipse(canvas, colors[color], rect, 2)
                elif mode == mode_square:
                    side = min(width, height)
                    rect = pygame.Rect(starting_position[0], starting_position[1], side, side)
                    pygame.draw.rect(canvas, colors[color], rect, 2)
                elif mode == mode_right_triangle:
                    points = [starting_position,
                              (starting_position[0], starting_position[1] + height),
                              (starting_position[0] + width, starting_position[1] + height)]
                    pygame.draw.polygon(canvas, colors[color], points, 2)
                elif mode == mode_equilateral_triangle:
                    points = [starting_position,
                              (starting_position[0] - width // 2, starting_position[1] + height),
                              (starting_position[0] + width // 2, starting_position[1] + height)]
                    pygame.draw.polygon(canvas, colors[color], points, 2)
                elif mode == mode_rhombus:
                    points = [(starting_position[0], starting_position[1] - height // 2),
                              (starting_position[0] - width // 2, starting_position[1]),
                              (starting_position[0], starting_position[1] + height // 2),
                              (starting_position[0] + width // 2, starting_position[1])]
                    pygame.draw.polygon(canvas, colors[color], points, 2)
        elif event.type == pygame.MOUSEMOTION and mouse_down:
            if mode == mode_draw:
                pygame.draw.line(canvas, colors[color], last_position, event.pos, radius * 2)
            last_position = event.pos
    pygame.display.flip()

pygame.quit()