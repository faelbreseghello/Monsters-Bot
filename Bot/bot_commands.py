import discord
import asyncio
import datetime
from profiles import Profile
import shelve
from copy import deepcopy
from config import *
from random import randint, choice


class Bot(discord.Client):


    async def monthly(self):
        global gamechannel
        c = 0
        while True:
            while gamechannel == None:
                await asyncio.sleep(10)
            # monthly result
            if datetime.datetime.today().day == end_day:
                # winner and reseting
                playersinfo = shelve.open('players.info', 'c', writeback=True)
                allstr = 'Rank: \n'
                for k, v in playersinfo.items(): # msg string formation and reseting points
                    allstr += f'{self.get_user(v.id).mention}: {v.month_points} \n'
                    c += 1
                    if c == 1:
                        winner = deepcopy(v)
                    elif v > winner:
                        winner = deepcopy(v)
                    playersinfo[k].resetmonth()
                playersinfo.close()

                # sending results
                await gamechannel.send(f'The winner was {self.get_user(winner.id)}, with {winner.month_points} pts! 🎉🎉🎉🎉🎉') if lang == 'en-us' else await gamechannel.send(f'O vencedor foi {self.get_user(winner.id)}, com {winner.month_points} pts! 🎉🎉🎉🎉🎉')
                await gamechannel.send(allstr)
                
            await asyncio.sleep(84500)


    async def scheduled(self):
        global gamechannel # The Minigame channel
        global valid # The stats of game
        global gameinterval
        while True:
            # Scare Floor
            if gamechannel == None:
                await asyncio.sleep(10)
            else:
                chance = randint(0,5)
                if valid or chance != 1:
                    await asyncio.sleep(gameinterval) # if the game keeps valid
                else:
                # Minigame 
                    await asyncio.sleep(gameinterval)
                    await gamechannel.send(file= discord.File(open(f'../Assets/monsters_memes/{choice(memes)}', 'rb')))
                    await gamechannel.send(startmsg)
                    valid = True


    async def on_ready(self):
        print(f'Logged on as {self.user} at {datetime.datetime.today()}')
        await self.change_presence(status=discord.Status.online, activity= discord.Game(statusmsg))


    async def on_message(self, message):
        global gamechannel
        try:
            perm = message.author.guild_permissions # author permissions
        except:
            pass
        
        # log message that will be stored in a file, and printed in console
        log = f'[{datetime.datetime.now()}]Message from {message.author}: "{message.content}"'
        logfile.write(log + '\n')
        print(log)

        if message.content == f'{prefix}close' and perm.administrator: # close command - end the bot process (only for admins)
            await message.channel.send(close)
            logfile.close()
            await self.close()
            exit()

        if message.content == f'{prefix}policy': # policy command - our think way
            await message.channel.send(policy)

        if message.content == f'{prefix}setup' and  perm.administrator: # sets up the minigame - the channel will be where this command was sent
            gamechannel = message.channel
            await message.channel.send(setup)

        if message.content == f'{prefix}fun': # fun quotes
            quote = choice(quotes)
            await message.channel.send(f'{fun} \n"{quote}"')

        if message.content == f'{prefix}memes': # memes
            await message.channel.send('LOL!', file=discord.File(open(f'../Assets/monsters_memes/{choice(memes)}', 'rb')))
        
        if message.content == f'{prefix}mypts': # Dm message for points
            playersinfo = shelve.open('players.info', 'c') # db open
            # dm validation
            dm = message.author.dm_channel 
            if dm == None:
                await message.author.create_dm()
                dm = message.author.dm_channel
            # message sending
            try:
                await dm.send(f'{mypts}\n total:{playersinfo[str(message.author.id)].points}, {month}:{playersinfo[str(message.author.id)].month_points} pts')
            except Exception as e:
                print(e)
                await dm.send(myptserror)
            playersinfo.close()



    async def on_reaction_add(self, reaction, user):
        global gamechannel 
        global valid # game status
        global winnerPoints

        if reaction.message.channel == gamechannel != None and valid and reaction.message.content == startmsg: # checks if the reaction is from a valid minigame session
            playersinfo = shelve.open('players.info', 'c', writeback=True) # db open
            # finishing the actual open game
            await gamechannel.send(winmsg1 + user.name + winmsg2)
            valid = False

            # checks if the player profile already exists
            try:
                data = playersinfo[f'{user.id}']
                del data
            except:
                playersinfo[f'{user.id}'] = Profile(user.id)

            # point computation    
            playersinfo[f'{user.id}'].addPoint(winnerPoints)
            playersinfo.close() # db close

    
    async def on_member_join(self, member):
        dm = member.dm_channel
        if dm == None:
            await member.create_dm()
            dm = member.dm_channel
        await dm.send(welcomemsg)