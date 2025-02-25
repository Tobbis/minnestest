import pygame, random, time
from helpers import draw_text, show_instructions, BLACK, RED, BLUE, GREEN, YELLOW, WHITE

def objekt_matching(screen):
    if not show_instructions(screen, [
        "Objektmatchning:",
        "Avgör om två objekt är likadana.",
        "Tryck på mellanslag om de matchar."
    ]):
        return 0

    all_shapes = ["cirkel", "fyrkant", "triangel", "stjärna", "romb", "oval", "rektangel", "parallelltrapets", "trapez", "hexagon", "pentagon"]
    all_colors = [ RED, BLUE, GREEN, YELLOW, WHITE]
    num_shapes = len(all_shapes)
    num_colors = len(all_colors)
    
    score = 0
    num_levels = 5
    for level in range(1, num_levels + 1):
        # Calculate counts: 2 for level 1, increasing linearly to num_shapes/num_colors for level 6.
        shapes_count = round(2 + (level - 1) * (num_shapes - 2) / num_levels)
        colors_count = round(2 + (level - 1) * (num_colors - 2) / num_levels)
        shapes = random.choices(all_shapes, k=shapes_count)
        colors = random.choices(all_colors, k=colors_count)
        print(shapes)
        print(colors)
        

        # shapes = ["cirkel", "fyrkant", "triangel"]
        # colors = [RED, BLUE, GREEN, YELLOW]

        for _ in range(5):
            shape1, shape2 = random.choices(shapes, k=2)
            color1, color2 = random.choices(colors, k=2)

            def draw_shape(shape, color, x, y):
                if shape == "cirkel":
                    pygame.draw.circle(screen, color, (x, y), 50)
                elif shape == "fyrkant":
                    pygame.draw.rect(screen, color, (x - 50, y - 50, 100, 100))
                elif shape == "triangel":
                    pygame.draw.polygon(screen, color, [(x, y - 50), (x - 50, y + 50), (x + 50, y + 50)])
                elif shape == "stjärna":
                    pygame.draw.polygon(screen, color, [(x, y - 50), (x + 20, y - 20), (x + 50, y - 20), (x + 30, y + 20), (x + 40, y + 50), (x, y + 30), (x - 40, y + 50), (x - 30, y + 20), (x - 50, y - 20), (x - 20, y - 20)])
                elif shape == "romb":
                    pygame.draw.polygon(screen, color, [(x, y - 50), (x + 50, y), (x, y + 50), (x - 50, y)])
                elif shape == "oval":
                    pygame.draw.ellipse(screen, color, (x - 50, y - 30, 100, 60))
                elif shape == "rektangel":
                    pygame.draw.rect(screen, color, (x - 60, y - 40, 120, 80))
                elif shape == "parallelltrapets":
                    pygame.draw.polygon(screen, color, [(x - 50, y - 40), (x + 50, y - 40), (x + 30, y + 40), (x - 30, y + 40)])
                elif shape == "trapez":
                    pygame.draw.polygon(screen, color, [(x - 50, y - 40), (x + 50, y - 40), (x + 30, y + 40), (x - 30, y + 40)])
                elif shape == "hexagon":
                    pygame.draw.polygon(screen, color, [(x - 40, y - 50), (x + 40, y - 50), (x + 60, y), (x + 40, y + 50), (x - 40, y + 50), (x - 60, y)])
                elif shape == "pentagon":
                    pygame.draw.polygon(screen, color, [(x, y - 50), (x + 50, y - 20), (x + 30, y + 40), (x - 30, y + 40), (x - 50, y - 20)])
                
            screen.fill(BLACK)
            draw_shape(shape1, color1, 300, 300)
            pygame.display.flip()
            time.sleep(max(1 - (level * 0.2), 0.2))

            screen.fill(BLACK)
            draw_shape(shape2, color2, 500, 300)
            pygame.display.flip()

            match = (shape1 == shape2 and color1 == color2)

            start_time = time.time()
            user_pressed = False
            while time.time() - start_time < max(2 - (level * 0.3), 0.5):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return score
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not user_pressed:
                        user_pressed = True
                        if match:
                            score += 1
            # End the level only if there was a match and no space press was detected in time
            if match and not user_pressed:
                return score
        # Level passed: show message and wait for Enter key.
        screen.fill(BLACK)
        draw_text(screen, f"Level {level} passed. Press Enter for next level", 200, 200, WHITE)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return score
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
    return score
