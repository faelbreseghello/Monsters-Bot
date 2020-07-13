import discord
import asyncio
import datetime
Token = open('../Token.txt', 'r') # The token of the bot
# log file opening 

try:
    logfile = open(f'../logs/log{datetime.datetime.now().month}/{datetime.datetime.now().year}.txt', 'a')
except:
    logfile = open(f'../logs/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'w')

prefix = '*' # the command prefix


class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        await self.change_presence(status=discord.Status.online, activity= discord.Game('Made with ❤️ by faelbreseghello#3092'))


    async def on_message(self, message):
        
        # log message that will be stored in a file, and printed in console
        log = f'[{datetime.datetime.now()}]Message from {message.author}: "{message.content}"'
        logfile.write(log + '\n')
        print(log)

        if message.content == f'{prefix}close': # close command - end the bot process (only for admins)
            perm = message.author.guild_permissions
            if perm.administrator:
                await message.channel.send('Bye monsters! See you soon...🧟‍♂️😞')
                await init.close()
                exit()

        if message.content == f'{prefix}policy': #policy command - our think way
            await message.channel.send("""We're a transparent and free4all bot, so at the end of every month, search for the transparency channels and see the audit logs and messages logs.🧐🧐🧐""")

                

init = Bot()
init.run(Token.read())
