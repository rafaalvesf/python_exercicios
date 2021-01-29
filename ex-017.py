import sys, pygame

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
musica = pygame.mixer.Sound('radio.mp3')
pygame.mixer.Sound.play(musica)
while(pygame.mixer.music.get_busy()): pass