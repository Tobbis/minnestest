import pygame, random, time
from helpers import draw_text, show_instructions, BLACK

def sifferspan(screen):
    if not show_instructions(screen, [
        "Sifferspan:",
        "Minns siffersekvensen och skriv in den.",
        "Använd tangentbordet och tryck Enter för att bekräfta."
    ]):
        return 0

    score = 0
    number = ''.join(str(random.randint(0, 9)) for _ in range(4))
    screen.fill(BLACK)
    draw_text(screen, number, 350, 250)
    pygame.display.flip()
    time.sleep(2)
    screen.fill(BLACK)
    draw_text(screen, "Skriv in siffrorna:", 250, 250)
    pygame.display.flip()
    user_input = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input == number:
                        score = len(number)
                    return score
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
        screen.fill(BLACK)
        draw_text(screen, "Skriv: " + user_input, 250, 300)
        pygame.display.flip()
