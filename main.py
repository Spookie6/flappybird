# Example file showing a basic pg "game loop"
import pygame as pg
import numpy as np

resolution = (1280,720)

# pygame setup
pg.init()
screen = pg.display.set_mode(resolution, pg.NOFRAME)
clock = pg.time.Clock()
running = True
dt = 0

class Constants:
	def __init__(self) -> None:
		self.jumpSpeed = -200
		self.fallingConstant = -600
		self.font = pg.font.SysFont("default", 64, bold=False, italic=False)

constants = Constants()

class Pos:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y

	def getTuple(self) -> tuple:
		return (self.x, self.y)

class Game:
	def __init__(self, players=None, ball=None,) -> None:
		self.player = None
		self.hasStarted = False
	
	def setPlayer(self, player) -> None:
		self.player = player

class Player:
	def	__init__(self,) -> None:
		self.pos = Pos(100,100)	
		self.rect = pg.Rect(self.pos.x, self.pos.y, 32, 32)
		self.vertSpeed = 0
  
	def move(self, keys) -> None:
		if keys[pg.K_SPACE]: self.vertSpeed = constants.jumpSpeed;
		self.pos.y += self.vertSpeed * dt;
		self.vertSpeed -= constants.fallingConstant * dt;
		self.rect[1] = self.pos.y
	
	def draw(self, screen) -> None:
		pg.draw.rect(screen, "white", self.rect)

game = Game()
player = Player()
game.setPlayer(player)

while running:
	# poll for events
	# pg.QUIT event means the user clicked X to close your window
	for event in pg.event.get():
		keys = pg.key.get_pressed()
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if keys[pg.K_ESCAPE]:
				pg.quit()
	
	# fill the screen with a color to wipe away anything from last frame
	screen.fill("black")
 
	# RENDER YOUR GAME HERE
	game.player.move(keys)
	game.player.draw(screen)

	# flip() the display to put your work on screen
	pg.display.flip()

	dt = clock.tick(60) / 1000  # limits FPS to 60

pg.quit()
