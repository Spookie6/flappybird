# Example file showing a basic pg "game loop"
import pygame as pg
import random

resolution = (1280,720)

# pygame setup
pg.init()
screen = pg.display.set_mode(resolution, pg.NOFRAME)
clock = pg.time.Clock()
running = True
dt = 0

class Constants:
	def __init__(self) -> None:
		self.font = pg.font.SysFont("default", 64, bold=False, italic=False)

		self.jumpSpeed = -200
		self.fallingConstant = 800
	
		self.pipeGap = 135
		self.pipeWidth = 100
		self.pipeDistance = 600
		self.pipeSpeed = 200

constants = Constants()

class Pos:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y

	def getTuple(self) -> tuple:
		return (self.x, self.y)

class Game:
	def __init__(self, ) -> None:
		self.player = None
		self.hasStarted = False
		self.gameOver = False
		self.pipes = []
		self.possiblePipes = list
	
	def setPlayer(self, player) -> None:
		self.player = player
	def addPipe(self, pipe) -> None:
		self.pipes.append(pipe)

class Player:
	def	__init__(self,) -> None:
		self.pos = Pos(250,100)	
		self.rect = pg.Rect(self.pos.x, self.pos.y, 32, 32)
		self.vertSpeed = 0
		self.dead = False

	def move(self, keys) -> None:
		if game.gameOver: return
  
		self.checkCollisions()

		if keys[pg.K_SPACE] and not self.dead: self.vertSpeed = constants.jumpSpeed;
		self.pos.y += self.vertSpeed * dt;
		if not game.gameOver: self.vertSpeed += constants.fallingConstant * dt;
		self.rect[1] = self.pos.y
		
		if self.pos.y + self.rect[3] >= resolution[1]:
			self.dead = True
			game.gameOver = True
			self.pos.y = resolution[1] - self.rect[3]
	
	def checkCollisions(self) -> None:
		for pipe in game.pipes:
			if self.rect.colliderect(pipe.rects[0]) or self.rect.colliderect(pipe.rects[1]):
				self.dead = True
   
	def draw(self, screen) -> None:
		pg.draw.rect(screen, "white", self.rect)

class Pipe:
	possiblePipes = [80, 160, 240, 320, 400, 480]
	def __init__(self, gap) -> None:
		self.pos = Pos(resolution[0], 0)
		self.gapPosY = gap
		self.pipeGap = constants.pipeGap
		self.rects = [
			pg.Rect(self.pos.x, 0, constants.pipeWidth, gap),
			pg.Rect(self.pos.x, gap + self.pipeGap, constants.pipeWidth, 1920 - (gap + self.pipeGap))
		]
  
	def move(self) -> None:
		self.pos.x -= constants.pipeSpeed * dt
		self.rects[0][0], self.rects[1][0] = (self.pos.x, self.pos.x)
	def draw(self, screen) -> None:
		for rect in self.rects:
			pg.draw.rect(screen, "Red", rect)

	def random() -> object:
		return Pipe(random.choice(Pipe.possiblePipes))

game = Game()
player = Player()
game.setPlayer(player)
game.addPipe(Pipe.random())

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
	# print(resolution[0] - game.pipes[len(game.pipes) - 1].rects[0][0] + constants.pipeWidth >= constants.pipeDistance)
	# print(resolution[0] - game.pipes[len(game.pipes) - 1].rects[0][0] + constants.pipeWidth)
	if resolution[0] - game.pipes[len(game.pipes) - 1].rects[0][0] + constants.pipeWidth >= constants.pipeDistance:
		# if len(game.pipes) < 2:
		game.addPipe(Pipe.random())

	for pipe in game.pipes:
		if not game.player.dead: pipe.move()
		pipe.draw(screen)
 
	game.player.move(keys)
	game.player.draw(screen)
 
	if game.gameOver:
		title = constants.font.render("Game Over", False, "White",)
		screen.blit(title, (resolution[0]/2 - title.get_rect()[2]/2, resolution[1]/2 - title.get_rect()[3]/2))

	# flip() the display to put your work on screen
	pg.display.flip()

	dt = clock.tick(60) / 1000  # limits FPS to 60

pg.quit()
