# Подключаем библиотеки
import pygame
from pygame.locals import *
from control import Control
from plane import Plane

# Задаем разрешение экрана
win = pygame.display.set_mode((1440, 900), FULLSCREEN)
# Задаем название окна
pygame.display.set_caption("Plane Game")

# Переменная типа Control
control = Control()
# Переменные типа Plane
plane1 = Plane("yellow")
plane2 = Plane("green")


while control.flag_game: 
	control.Control()
	control.DrawBackground(win)
	plane1.Animation(win)
	plane1.Shoot(win, plane2)

	plane2.Animation(win)
	plane2.Shoot(win, plane1)

exit()