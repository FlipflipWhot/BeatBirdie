import pygame
import random
import tkinter as tk
from tkinter import messagebox
from pygame.mixer import Sound

pygame.mixer.init()
#class game:
#This class is used to create the game object.
class Game:
    def __init__(self, width, height, rows, row_colour, background_colour):
        #size of the game window in pixels
        self.width = width
        self.height = height

        #rows defines the number of rows and columns in the game.
        self.rows = rows
        #row colour defines the colour of the rows in the game
        self.row_colour = row_colour

        #background_color defines the colour of the background in the game
        self.background_colour = background_colour


    def window(self, win):
        #Setting up the window
        pygame.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        self.win.fill(self.background_colour)
        win = self.win
        pygame.display.set_caption('Snake Game')
        clock = pygame.time.Clock()



    #updates the window background, draws the grid, and the snake
    def update(self):
        pygame.time.delay(50)
        self.win.fill(self.background_colour)
        self.draw_grid()
        snake.draw(self.win)


        note1.draw(self.win)




        pygame.display.update()

    def score(self, win):
        #score defines the score of the player in the game
        score = 0

    def draw_grid(self):
        #Function to draw the grid in the game window using the pygame module
        size_between = self.width // self.rows

        #Draws the rows in the game window
        x = 0
        y = 0
        for l in range(self.rows):
            x = x + size_between
            y = y + size_between

            pygame.draw.line(self.win, self.row_colour, (x, 0), (x, self.width))
            pygame.draw.line(self.win, self.row_colour, (0, y), (self.height, y))




#class Snake: the snakes starts in the middle of the game window
class Snake:
    def __init__(self, width, height, colour, xPos, yPos, direction):
        #width and height defines the size of the snake in the game window
        self.width = width
        self.height = height

        #colour defines the colour of the snake in the game window
        self.colour = colour

        #position defines the position of the snake in the game window
        self.xPos = xPos
        self.yPos = yPos
        #direction defines the direction of the snake in the game window
        self.direction = direction

    def draw(self, win):
        #draws the snake in the game window
        pygame.draw.rect(win, self.colour, (self.xPos, self.yPos, self.width, self.height))
        self.move()



    def move(self):

        #pygame key events to move the snake. It also makes sure the snake doesn't go off the screen and goes continuously
        velocity = 25
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 'left'
            self.xPos -= velocity
        if keys[pygame.K_RIGHT]:
            self.direction = 'right'
            self.xPos += velocity
        if keys[pygame.K_UP]:
            self.direction = 'up'
            self.yPos -= velocity
        if keys[pygame.K_DOWN]:
            self.direction = 'down'
            self.yPos += velocity

        #if the snake hits the edge of the game window, the game ends
        if self.xPos > 500 or self.xPos < 0 or self.yPos > 500 or self.yPos < 0:
            pygame.quit()
            quit()

#Class Notes
class Notes:
    def __init__(self, note, ID, xPos, yPos ):
        self.note = note
        self.ID = ID
        self.xPos = xPos
        self.yPos = yPos
        self.collected = 1

    def play(self):
        pygame.mixer.music.load(f"{self.note}.wav")
        pygame.mixer.music.play(self.ID)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.fadeout(1000)

    def display(self, win):
        note = pygame.draw.rect(win, (255, 255, 255), (self.xPos, self.yPos, 25, 25))

    def draw(self, win):
        if snake.xPos == self.xPos and snake.yPos == self.yPos:
            self.collected += 1
            self.play()

        if self.collected == 1:
            self.display(win)
        else:
            del self

#Creates the game object
birdie = Game(500, 500, 20, (251, 251, 242), (255, 211, 52))
# Creates the snake and movement
snake = Snake(25, 25, (255, 255, 255), birdie.width / 2, birdie.height / 2, 'right')
#Creates the notes
note1 = Notes('C', 1, 50, 50)



#Creates the window
birdie.window('Birdie')

#Runs the game
Running = True
while Running:

    #Updates the game window
    birdie.update()

    #exit the game when the user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
