import csv

import pygame
import random
import sys
import os
import time
import psutil
import logging

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

        self.rowsize = self.width // self.rows
        borderY = 812 / 4
        #
        self.bar_xPos = borderY // self.rowsize * self.rowsize
        self.bar_yPos = self.width
        # Creates the notes

    def window(self, win):
        #Setting up the window
        pygame.init()
        self.win = pygame.display.set_mode((self.width, self.height))
        self.win.fill(self.background_colour)
        win = self.win
        pygame.display.set_caption('Snake Game')
        clock = pygame.time.Clock()
        clock.tick(10)

    #updates the window background, draws the grid, and the snake
    def update(self):
        pygame.time.delay(50)
        self.win.fill(self.background_colour)
        self.notes_ID = (note1.ID, note2.ID, note3.ID)

        self.draw_grid(self.win)
        self.draw_bar(self.win)
        #draws rectangle at the top of the game window and ends at the bar
        #pygame.draw.rect(self.win, self.row_colour, (0, 0, self.width, self.height/4))

        snake.draw(self.win)
        self.score(self.win)
        self.draw_staff(self.win)
        self.draw_note(self.win, 0,)
        self.draw_note(self.win, 1)
        self.draw_note(self.win, 2)



        #draws the notes
        note1.draw(self.win)
        note2.draw(self.win)
        note3.draw(self.win)


        pygame.display.update()


    def note_location(self):
        # for loop to create random positions for the notes
        barline_list = []
        barX = self.bar_xPos
        barY = self.bar_yPos
        borderY = 712 / 4
        for i in range(3):
            barline = {
                "xPos": random.randint(0, barX) // row_size * row_size,
                "yPos": random.randint(barY, 712) // row_size * row_size
            }
            barline_list.append(barline)


    def score(self, win):
        font = pygame.font.SysFont('bahnschrift', 30, True)
        #checks if the notes was played in the correct order using the ID of the note

        if note1.notePlayed == True and note2.notePlayed == True and note3.notePlayed == True and self.fail == False:
            self.points += 1
            correct_note = font.render('Correct!', 1, (0, 255, 0))
            win.blit(correct_note, (borderY+ self.width/8, 0 + 2*row_size))
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
        #draws the bar to separate the game window into two parts with the button section being larger
        #bar starts at one of the grid's lines and ends row_size pixels below the grid's lines
        pygame.draw.rect(win, (217, 53, 13), (0, borderY // row_size * row_size, self.width, row_size))


    def draw_grid(self, win):
        #draws the grid in the game window
        #the grid is drawn using the pygame.draw.line function and for loop
        sizeBtwn = self.width // self.rows
        x = 0
        y = 0
        for l in range(self.height):
            x = x + sizeBtwn
            y = y + sizeBtwn

            pygame.draw.line(win, self.row_colour, (x, 0), (x, self.height))
            pygame.draw.line(win, self.row_colour, (0, y), (self.width, y))

    def draw_staff(self, win):
        #Draws a box with start postion in origo and has to same end position as the bar
        pygame.draw.rect(win, (255, 255, 255), (0, 0, self.width, borderY // row_size * row_size))


        #draws a musical staff in top section of the game window.
        self.position = 0 + 2 * row_size, 0 + 2*row_size
        line_length = self.position[0] + row_size * 8, self.position[1]
        pygame.draw.line(win, (0, 0, 0), self.position, line_length, 2)

        #The for loop draws the lines of the staff
        for i in range(5):
            pygame.draw.line(win,(0,0,0), (self.position[0], self.position[1] + row_size* i ), (line_length[0], self.position[1] + row_size * i), 2)

    def draw_note(self, win, i):
        #This function is responsible for drawing the corresponding note to Notes.ID
        notes_collected = [note1.notePlayed, note2.notePlayed, note3.notePlayed]
        if notes_collected[i] == True and self.fail == False:
            colour = (0,255,0)
        elif self.fail == True:
            colour = (255,0,0)
        else:
            colour = (0,0,0)

        staff_notes = ['C','D' ,'E']

        if staff_notes[i] == 'C':
            self.staff_note_pos = self.position[0] + row_size, self.position[1] + row_size * 5
            #draw a horizontal line going through the note to indicate that the note is placed under the staff
            pygame.draw.line(win,  (0,0,0), (self.staff_note_pos[0] - 14, self.staff_note_pos[1]), (self.staff_note_pos[0]+14, self.staff_note_pos[1]), 2)
            #draws the note on the staff
            pygame.draw.circle(win, colour, self.staff_note_pos, 10)
            #draw the note tail
            pygame.draw.line(win,colour, (self.staff_note_pos[0] + row_size / 2, self.staff_note_pos[1]),(self.staff_note_pos[0] + row_size / 2, self.staff_note_pos[1] - self.position[1]), 2)

        elif staff_notes[i] == 'D':
            self.staff_note_pos = self.position[0] + row_size * 3, self.position[1] + row_size * 5 - row_size/3
            #draws the note on the staff
            pygame.draw.circle(win, colour, self.staff_note_pos, 10)
            #draw the note tail
            pygame.draw.line(win, colour, (self.staff_note_pos[0] + row_size / 2, self.staff_note_pos[1]),
                             (self.staff_note_pos[0] + row_size / 2, self.staff_note_pos[1] - self.position[1]), 2)

        elif staff_notes[i] == 'E':
            self.staff_note_pos = self.position[0] + row_size * 5, self.position[1] + row_size * 4
            #draws the note on the staff
            pygame.draw.circle(win, colour, self.staff_note_pos, 10)
            #draw the note tail
            pygame.draw.line(win, colour, (self.staff_note_pos[0] + row_size/2, self.staff_note_pos[1]), (self.staff_note_pos[0]+ row_size/2, self.staff_note_pos[1] - self.position[1]), 2)

    def restart(self):
        os.startfile(sys.argv[0])
        sys.exit(self)




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
        pygame.draw.rect(win, (204, 0, 0), (self.xPos, self.yPos, self.width, self.height))
        pygame.draw.circle(win, self.colour, (self.xPos + self.width/2, self.yPos + self.height/2), 5)
        pygame.draw.circle(win, self.colour, (self.xPos + self.width/2, self.yPos + self.height/2), 5)
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
        if self.xPos > birdie.width or self.xPos < 0 or self.yPos > birdie.height or self.yPos < birdie.height/4:
            birdie.fail = True

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
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(self.ID)
        pygame.mixer.music.fadeout(1000)

    def display(self, win):
        #draw rectangle for the note
        note = pygame.draw.rect(win, (252, 244, 207), (self.xPos, self.yPos, row_size, row_size))

        font = pygame.font.SysFont('bahnschrift', 15, True)
        text = font.render(self.note, 1, (204, 0, 0))
        win.blit(text, (self.xPos + 4 , self.yPos + 2))

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
birdie = Game(375, 712, 20, (204, 0, 0), (251, 251, 242),0)

row_size = birdie.width // birdie.rows

snakeY = random.randint(int(712/4), 712) // row_size * row_size
snake = Snake(row_size, row_size, (255, 211, 52), row_size, snakeY, 'right')

#for loop to create random positions for the notes
barline_list = []
borderY = 712 / 4
def random_location():
    barX = birdie.bar_xPos
    barY = birdie.bar_yPos

    for i in range(3):
        barline = {
            "xPos": random.randint(0, barX) // row_size * row_size,
            "yPos": random.randint(barY, 712) // row_size * row_size
        }
        barline_list.append(barline)

random_location()


#Creates the notes
note1 = Notes('C', 1, barline_list[0].pop("xPos"), barline_list[0].pop("yPos"))
note2 = Notes('D', 2, barline_list[1].pop("xPos"), barline_list[1].pop("yPos"))
note3 = Notes('E', 3, barline_list[2].pop("xPos"), barline_list[2].pop("yPos"))






#Creates the window
birdie.window('Birdie')

#Runs the game
Running = True
while Running:





    #draws the restart button
    def draw_restart_button():
        birdie.restart_button = pygame.draw.rect(birdie.win, (255, 255, 255), (birdie.width/2.5, birdie.height/2.5, 100, 50))
        font = pygame.font.SysFont('bahnschrift', 20, True)
        restart = font.render('New Game', 1, (0, 0, 0))
        birdie.win.blit(restart, (birdie.width/2.5, birdie.height/2.5))

        #detects if the user clicks the restart button
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if birdie.width/2.5 + 100 > mouse[0] > birdie.width/2.5 and birdie.height/2.5 + 50 > mouse[1] > birdie.height/2.5:
            if click[0] == 1:
                birdie.restart()


    if birdie.fail == True or birdie.victory == True:
        draw_restart_button()
        pygame.display.update()
    else:
        #Updates the game window
        birdie.update()


    #exit the game when the user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
