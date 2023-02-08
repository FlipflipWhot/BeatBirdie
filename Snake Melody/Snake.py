import csv

import pygame
import random
import tkinter as tk
from tkinter import messagebox
from pygame.mixer import Sound

pygame.mixer.init()
#class game:
#This class is used to create the game object.
class Game:
    def __init__(self, width, height, rows, row_colour, background_colour, points):
        #size of the game window in pixels
        self.width = width
        self.height = height

        #points defines the score of the player in the game
        self.points = points

        #rows defines the number of rows and columns in the game.
        self.rows = rows
        #row colour defines the colour of the rows in the game
        self.row_colour = row_colour

        #background_color defines the colour of the background in the game
        self.background_colour = background_colour

        #victory and fail
        self.victory = False
        self.fail = False


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

        self.draw_bar(self.win)

        snake.draw(self.win)

        self.score(self.win)

        self.treble_clef(self.win)

        #draws the notes
        note1.draw(self.win)
        note2.draw(self.win)
        note3.draw(self.win)



        pygame.display.update()
    def score(self, win):

        font = pygame.font.SysFont('comicsans', 30, True)
        #checks if the notes was played in the correct order using the ID of the note


        if note1.notePlayed == True and note2.notePlayed == True and note3.notePlayed == True and self.fail == False:
            self.points += 1
            correct_note = font.render('Correct!', 1, (0, 255, 0))
            win.blit(correct_note, (self.width/4, self.height/2))
            self.victory = True

        elif note2.notePlayed == True and note1.notePlayed == False:
            wrong_note = font.render('Wrong Note', 1, (255, 0, 0))
            win.blit(wrong_note, (self.width/4, self.height/2))
            self.fail = True

        elif note3.notePlayed == True and note2.notePlayed == False:
            wrong_note = font.render('Wrong Note', 1, (255, 0, 0))
            win.blit(wrong_note, (self.width/4, self.height/2))
            self.fail = True

        elif note3.notePlayed == True and note1.notePlayed == False:
            wrong_note = font.render('Wrong Note', 1, (255, 0, 0))
            win.blit(wrong_note, (self.width/4, self.height/2))
            self.fail = True

       # text = font.render('Score: ' + str(self.points), 1, (0, 0, 0))
       # win.blit(text, (self.width/2, 10))

    def draw_bar(self, win):
        #draws the bar at the top of the game window
        pygame.draw.rect(win, self.row_colour, (0, self.height/4, self.width, row_size))

    def treble_clef(self, win):
        #draws a note table at the top of the game window to show the notes in the melody and the notes that have been eaten by the snake
        #the staff is drawn using the pygame.draw.line function and the notes are drawn using the pygame.draw.circle function

        #the staff is smaller than the bar and is placed above the bar in the game window
        #the staff is drawn using the pygame.draw.line function and for loop
        for i in range(5):
            pygame.draw.line(win, (0, 0, 0), (self.width/4, self.height/8 + (i * row_size)), (self.width/4 + self.width/2, self.height/8 + (i * row_size)), 2)

        #the notes are drawn using the pygame.draw.circle function and for loop. The notes are placed on the staff according to the melody and the notes are placed on the right lines
        Got_notes_correct = (0, 255, 0)
        Got_notes_wrong = (255, 0, 0)
        Notes_coloured = (0, 0, 0)

        #draw e on button line
        pygame.draw.circle(win, Notes_coloured, (self.width/2.65 + row_size, self.height/8 + (row_size * 4)), 10)
        #draw C
        pygame.draw.circle(win, Notes_coloured, (self.width/4 + row_size, self.height/16 + (row_size * 8)), 10)
        #draw D
        pygame.draw.circle(win, Notes_coloured, (self.width/3.25 + row_size, self.height/14 + (row_size * 7)), 10)


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
        velocity = row_size
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
        if self.xPos > birdie.width or self.xPos < 0 or self.yPos > birdie.height or self.yPos < 812/4:
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
        self.notePlayed = False

    def play(self):
        pygame.mixer.music.load(f"{self.note}.wav")
        pygame.mixer.music.play(self.ID)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.fadeout(1000)

    def display(self, win):
        #draw rectangle for the note
        note = pygame.draw.rect(win, (255, 255, 255), (self.xPos, self.yPos, row_size, row_size))

        font = pygame.font.SysFont('comicsans', 20, True)
        text = font.render(self.note, 1, (0, 0, 0))
        win.blit(text, (self.xPos, self.yPos))

    def draw(self, win):
        if snake.xPos == self.xPos and snake.yPos == self.yPos and self.collected == 1:
            self.collected += 1

            if self.notePlayed == False:
                self.play()
                self.notePlayed = True
                #birdie.points += 1

        if self.collected == 1:
            self.display(win)



#Creates the game object. Size simulates the size of a iphone 14 pro screen in pixels: 375 x 812
birdie = Game(375, 812, 20, (251, 251, 242), (255, 211, 52),0)

row_size = birdie.width // birdie.rows

snakeY = random.randint(int(812/4), 812) // row_size * row_size
snake = Snake(row_size, row_size, (255, 255, 255), row_size, snakeY, 'right')

#for loop to create random positions for the notes
barline_list = []

borderY = 812/4
for i in range(3):
    barline = {
        "xPos": random.randint(0, 375) // row_size * row_size,
        "yPos": random.randint(int(borderY), 812) // row_size * row_size
    }
    barline_list.append(barline)

#Creates the notes
note1 = Notes('C', 1, barline_list[0].pop("xPos"), barline_list[0].pop("yPos"))
note2 = Notes('D', 2, barline_list[1].pop("xPos"), barline_list[1].pop("yPos"))
note3 = Notes('E', 3, barline_list[2].pop("xPos"), barline_list[2].pop("yPos"))




#Creates the window
birdie.window('Birdie')

#Runs the game
Running = True
while Running:


    #Updates the game window
    birdie.update()


    #draws the restart button
    def draw_restart_button():
        birdie.restart_button = pygame.draw.rect(birdie.win, (255, 255, 255), (birdie.width/2.5, birdie.height/2.5, 100, 50))
        font = pygame.font.SysFont('comicsans', 20, True)
        restart = font.render('Exit', 1, (0, 0, 0))
        birdie.win.blit(restart, (birdie.width/2.5, birdie.height/2.5))

        #detects if the user clicks the restart button
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if birdie.width/2.5 + 100 > mouse[0] > birdie.width/2.5 and birdie.height/2.5 + 50 > mouse[1] > birdie.height/2.5:
            if click[0] == 1:
                pygame.quit()
                quit()


    if birdie.fail == True:

        draw_restart_button()
        pygame.display.update()

    elif birdie.victory == True and birdie.fail == False:
        #write the score to the Scores.cvs file
        with open('Scores.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([birdie.points])



        draw_restart_button()
        pygame.display.update()

    #exit the game when the user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
