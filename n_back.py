import pygame, random, time
from helpers import draw_text, show_instructions, BLACK

def n_back(screen):
    total_score = 0
    level = 1

    # show initial instructions for level 1
    instructions = [
        f"N-Back (nivå {level}):",
        f"Kom ihåg vad som visas {level} steg tidigare.",
        "Tryck på mellanslag om det matchar.",
        "Du får göra fel 1 gång per nivå. Lycka till!"
    ]
    if not show_instructions(screen, instructions):
        return 0

    # main loop: each iteration is one level
    while True:
        error_occurred = False
        rounds_in_level = 2  # två rundor per nivå
        level_score = 0

        for round_num in range(rounds_in_level):
            # generera en längre sekvens (12 siffror)
            sequence = [random.randint(0, 6) for _ in range(12)]
            round_score = 0

            for i in range(len(sequence)):
                screen.fill(BLACK)
                draw_text(screen, str(sequence[i]), 380, 250)
                pygame.display.flip()
                time.sleep(1)
                # Lägg till fördröjning med blank skärm
                screen.fill(BLACK)
                pygame.display.flip()
                time.sleep(0.5)

                # detect user input for current number
                user_pressed = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return total_score
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        user_pressed = True

                if i >= level:
                    is_match = (sequence[i] == sequence[i - level])
                    if user_pressed:
                        if is_match:
                            round_score += 1
                        else:
                            error_occurred = True
                            break
                    else:
                        if is_match:
                            error_occurred = True
                            break

                if level_score + round_score >= 2:
                    break
            level_score += round_score
            if error_occurred or level_score >= 2:
                break

        total_score += level_score

        if error_occurred:
            # Display failure message and wait for Enter before exiting this game
            screen.fill(BLACK)
            draw_text(screen, "Ingen match tyvärr!", 200, 250)
            draw_text(screen, f"Poäng: {total_score}", 200, 300)
            draw_text(screen, "Tryck på Enter för nästa spel.", 200, 350)
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return total_score
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        waiting = False
            break

        # level completed successfully; show transition message
        screen.fill(BLACK)
        draw_text(screen, f"Grattis! Du har klarat nivå {level}!", 200, 250)
        draw_text(screen, "Nu går vi vidare till nästa nivå.", 200, 300)
        # draw_text(screen, f"Regler: Kom ihåg vad som visas {level+1} steg tidigare.", 200, 350)
        # draw_text(screen, "Tryck på mellanslag om det matchar.", 200, 400)
        pygame.display.flip()

        # wait for the Enter key to continue
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return total_score
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False

        level += 1

        # show new level instructions before starting next level
        instructions = [
            f"N-Back (nivå {level}):",
            f"Kom ihåg vad som visas {level} steg tidigare.",
            "Tryck på mellanslag om det matchar.",
            "Du får göra fel 1 gång per nivå. Lycka till!"
        ]
        if not show_instructions(screen, instructions):
            return total_score

    return total_score