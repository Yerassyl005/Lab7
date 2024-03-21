import pygame
import sys
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1200, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Load Mickey Mouse image
mickey_image = pygame.image.load("mickeyclock.jpeg")

def draw_clock(minutes_angle, seconds_angle):
    screen.fill((255, 255, 255))  # Fill the screen with white color
    screen.blit(mickey_image, (WIDTH // 2 - mickey_image.get_width() // 2, HEIGHT // 2 - mickey_image.get_height() // 2))

    # Calculate the position of Mickey's hands
    mickey_center = (WIDTH // 2, HEIGHT // 2)
    minutes_length = 150
    seconds_length = 180

    # Draw Mickey's minute hand
    minutes_x = mickey_center[0] + minutes_length * math.cos(math.radians(minutes_angle))
    minutes_y = mickey_center[1] - minutes_length * math.sin(math.radians(minutes_angle))
    pygame.draw.line(screen, (0, 0, 0), mickey_center, (minutes_x, minutes_y), 5)

    # Draw Mickey's second hand
    seconds_x = mickey_center[0] + seconds_length * math.cos(math.radians(seconds_angle))
    seconds_y = mickey_center[1] - seconds_length * math.sin(math.radians(seconds_angle))
    pygame.draw.line(screen, (255, 0, 0), mickey_center, (seconds_x, seconds_y), 2)

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get the current system time
        current_time = datetime.now().time()

        # Calculate angles for Mickey's hands
        minutes_angle = (current_time.minute / 60) * 360
        seconds_angle = (current_time.second / 60) * 360

        # Clear the screen and draw the clock
        draw_clock(minutes_angle, seconds_angle)

        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate at 60 FPS

if __name__ == "__main__":
    main()
