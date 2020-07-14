import discord
import asyncio
import datetime
from profiles import Profile

# Minigame setup
gamechannel = None 
gameinterval = 60
valid = False

Token = open('../Token.txt', 'r') # The token of the bot

# log file opening 
try:
    logfile = open(f'../logs/log{datetime.datetime.now().month}/{datetime.datetime.now().year}.txt', 'a')
except:
    logfile = open(f'../logs/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'w')

prefix = '*' # the command prefix


class Bot(discord.Client):


    async def scheduled(self):
        global gamechannel # The Minigame channel
        global valid # The stats of game
        global gameinterval
        while True:
            if datetime.datetime.today().day == 1:
                pass # temp
            else:
                # TEMP TEST
                if gamechannel == None:
                    await asyncio.sleep(10)
                else:
                    if valid:
                        await asyncio.sleep(gameinterval) # if the game keeps valid
                    else:
                    # Minigame 
                        await asyncio.sleep(gameinterval)
                        await gamechannel.send('test message')
                        valid = True


    async def on_ready(self):
        print(f'Logged on as {self.user}')
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

        if message.content == f'{prefix}setup' and  perm.administrator:
            gamechannel = message.channel
            await message.channel.send('Set up! In one hour the game starts!')
            

init = Bot()
init.loop.create_task(init.scheduled())
init.run(Token.read())
