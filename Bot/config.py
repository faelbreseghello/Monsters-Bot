import datetime
import os


# General
Token = open('../Token.txt', 'r') # The token of the bot

prefix = '*' # the command prefix

lang = 'en-us' # 'en-us' or 'pt-br'

memes = os.listdir('../Assets/monsters_memes') # memes db load

# Minigame setup
gamechannel = None # You can set here or with the command "*setup"
gameinterval = 5 #interval between the sessions #TEMP VALUE
winnerPoints = 3 # points for who win the minigame
valid = False # DO NOT edit this
end_day = 30 # The day of the end off the minigame - will verify at the start time


# log file 
try:
    logfile = open(f'../logs/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'a')
except:
    logfile = open(f'../logs/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'w')

# Language import
if lang == 'en-us':
    from en_us import *
elif lang == 'pt-br':
    from pt_br import *
else:
    raise Exception(f'There are no lang option called {lang}')
