import discord

class Profile():

    def __init__(self, user : int): # Creates a profile object, that stores users info about the minigame
        self.id = user # discord user id
        self.points = 0 # total points  
        self.month_points = 0 # monthly points

    def addPoint(self, points : int): # add 'param:points' to the point attributes 
        self.points += points
        self.month_points += points

    def resetmonth(self): # reset month points
        self.month_points = 0

    def __str__(self): # user and him all-time points
        return f'{self.id} {self.points}'
    

