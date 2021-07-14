import pygame, sys

class Settings():
	"""Основные настройки экрана и т.д"""
	def __init__(self):
		#Параметры экрана
		self.screen_width = 700#ширина игровой поверхности
		self.screen_height = 700#высота игровой поверхности
		self.bg_color=(150, 150, 150)#цвет поверхности
		#Настройки корабля
		self.ship_speed_factor = 1.5
		
		

class Ship():
	def __init__(self, sett, screen):
		self.sett = Settings()
		self.screen = screen#эта строка тут нужна
		self.image = pygame.image.load('images/new_object.bmp')#вызов для загрузки изображения
		self.rect = self.image.get_rect()#под изображение "кладется" прямоугольник, который двигается по поверхности
		self.screen_rect = screen.get_rect()#сам экран предстсавляется как прямоугольник
		#Обновляемое изображение корабля будте появляться в этих координатах
		self.rect.centerx = self.screen_rect.centerx#координата х прямоугольника корабля "кладется" (совмещается)на координату х поверхности
		self.rect.centery = self.screen_rect.centery#аналогично с выше
		self.rect.center = self.screen_rect.center#совмещаются нижние части прямоугольников экрана и изображения корабля
		#Флаги перемещения
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		#Сохранение вещественной координаты корабля.
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

	
	def update(self):
		"""Обновляет позицию с учетом флага"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.sett.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.sett.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.rect.centery -= self.sett.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.sett.ship_speed_factor
		#Обновление атрибута rect на основании self.center.
		self.rect.centerx = self.centerx
			
	def blitme(self):
		"""Создает корабль в данной позиции"""
		self.screen.blit(self.image, self.rect)#вызов выводит изображение на экран в заданной позиции  self.rect
		

def check_events(ship):
	"""Обработка нажатий клавиш"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					ship.moving_right=True#перемещение корабля вправо
				if event.key == pygame.K_LEFT:
					ship.moving_left = True#перемещение влево
				if event.key == pygame.K_UP:
					ship.moving_up = True#перемещение вверх
				if event.key == pygame.K_DOWN:
					ship.moving_down = True#перемещение вниз
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = False
				if event.key == pygame.K_LEFT:
					ship.moving_left = False
				if event.key == pygame.K_UP:
					ship.moving_up = False
				if event.key == pygame.K_DOWN:
					ship.moving_down = False

def update_screen(Settings, screen, ship):
	"""Обновляет изображение на экране и отображает новый экран."""
	#При каждом проходе цикла перерисовыветеся экран
	screen.fill(Settings.bg_color)
	ship.blitme()
