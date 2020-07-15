import discord
import asyncio
import datetime
from profiles import Profile
import shelve
from copy import copy


# Minigame setup
gamechannel = None 
gameinterval = 10
valid = False
winnerPoints = 3

Token = open('../Token.txt', 'r') # The token of the bot

# log file and db opening 
try:
    logfile = open(f'../logs/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'a')
except:
    logfile = open(f'../logs/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'w')


prefix = '*' # the command prefix


class Bot(discord.Client):


    async def monthly(self):
        while True:
            # monthly results
                if datetime.datetime.today().day == 16:
                    # reseting points
                    playersinfo = shelve.open('players.info', 'c', writeback=True)
                    for key in playersinfo.keys():
                        playersinfo[key].resetmonth()
                    playersinfo.close()
                await asyncio.sleep(84500)


    async def scheduled(self):
        global gamechannel # The Minigame channel
        global valid # The stats of game
        global gameinterval
        while True:
            # TEMP TEST
            if gamechannel == None:
                await asyncio.sleep(10)
            else:
                if valid:
                    await asyncio.sleep(gameinterval) # if the game keeps valid
                else:
                # Minigame 
                    await asyncio.sleep(gameinterval)
                    await gamechannel.send('minigame temp message')
                    valid = True


    async def on_ready(self):
        print(f'Logged on as {self.user} at {datetime.datetime.today()}')
        await self.change_presence(status=discord.Status.online, activity= discord.Game('Made with ❤️ by faelbreseghello#3092'))


    async def on_message(self, message):
        global gamechannel

        perm = message.author.guild_permissions # author permissions

        # log message that will be stored in a file, and printed in console
        log = f'[{datetime.datetime.now()}]Message from {message.author}: "{message.content}"'
        logfile.write(log + '\n')
        print(log)

        if message.content == f'{prefix}close' and perm.administrator: # close command - end the bot process (only for admins)
            await message.channel.send('Bye monsters! See you soon...🧟‍♂️😞')
            await init.close()
            exit()

        if message.content == f'{prefix}policy': #policy command - our think way
            await message.channel.send("""We're a transparent and free4all bot, so at the end of every month, search for the transparency channels and see the audit logs and messages logs.🧐🧐🧐""")

        if message.content == f'{prefix}setup' and  perm.administrator: # sets up the minigame - the channel will be where this command was sent
            gamechannel = message.channel
            await message.channel.send('Set up! In one hour the game starts!')
            

    async def on_reaction_add(self, reaction, user):
        global gamechannel 
        global valid # game status
        global winnerPoints

        if reaction.message.channel == gamechannel != None and valid and reaction.message.content == 'minigame temp message': # checks if the reaction is from a valid minigame session
            playersinfo = shelve.open('players.info', 'c', writeback=True) # db open
            # finishing the actual open game
            await gamechannel.send(f'The member {user.name} won the challenge.')
            valid = False

            # checks if the player profile already exists
            try:
                data = playersinfo[f'{user.id}']
            except:
                playersinfo[f'{user.id}'] = Profile(user.id)

            # point computation    
            playersinfo[f'{user.id}'].addPoint(winnerPoints)
            playersinfo.close() # db close


init = Bot()
init.loop.create_task(init.monthly())
init.loop.create_task(init.scheduled())
init.run(Token.read())
