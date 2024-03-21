import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display (not really needed for this)
screen = pygame.display.set_mode((700, 500))

# Set up music directory
music_directory = "music/"

# Get a list of music files
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

# Initialize music player
current_track_index = 0
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))

# Keyboard mapping
KEY_MAPPING = {
    pygame.K_SPACE: "play_stop",
    pygame.K_RIGHT: "next",
    pygame.K_LEFT: "previous"
}

# Function to play the current track
def play():
    pygame.mixer.music.unpause()

# Function to stop the current track
def stop():
    pygame.mixer.music.pause()

# Function to play the next track
def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
    pygame.mixer.music.play()

# Function to play the previous track
def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
    pygame.mixer.music.play()

# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key in KEY_MAPPING:
                action = KEY_MAPPING[event.key]
                if action == "play_stop":
                    if pygame.mixer.music.get_busy():
                        stop()
                    else:
                        play()
                elif action == "next":
                    next_track()
                elif action == "previous":
                    previous_track()

# Quit Pygame
pygame.quit()
