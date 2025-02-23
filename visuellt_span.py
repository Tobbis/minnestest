import pygame, random, time
from helpers import draw_text, show_instructions, WHITE, BLACK, RED

def visuellt_span(screen):
    if not show_instructions(screen, [
        "Visuellt Span:",
        "Minns ordningen på de röda rutorna.",
        "Klicka på rutorna i samma ordning."
    ]):
        return 0

    score = 0
    sequence = [random.randint(0, 8) for _ in range(3)]
    input_sequence = []

    def draw_grid():
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, WHITE, (200 + j * 100, 200 + i * 100, 80, 80), 2)

    for num in sequence:
        screen.fill(BLACK)
        draw_grid()
        x = 200 + (num % 3) * 100
        y = 200 + (num // 3) * 100
        pygame.draw.rect(screen, RED, (x, y, 80, 80))
        pygame.display.flip()
        time.sleep(1)

    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()

    while len(input_sequence) < len(sequence):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 200 <= x <= 480 and 200 <= y <= 480:
                    col = (x - 200) // 100
                    row = (y - 200) // 100
                    input_sequence.append(row * 3 + col)
        if input_sequence == sequence:
            score = len(sequence)
            return score
        if len(input_sequence) == len(sequence) and input_sequence != sequence:
            return score
