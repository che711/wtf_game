import pygame
import del_game_function as dgf
from del_game_function import Settings, Ship

# python3 del_game.py

def runGame():
	pygame.init()
	sett = Settings()
	screen = pygame.display.set_mode((sett.screen_width, sett.screen_height))
	pygame.display.set_caption("WTF!")
	ship = Ship(sett, screen)
	while True:
		dgf.check_events(ship)
		ship.update()
		dgf.update_screen(sett, screen, ship)
		screen.fill(sett.bg_color)
		ship.blitme()
		pygame.display.flip()
	
	
runGame()
