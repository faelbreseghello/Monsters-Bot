import discord
import asyncio
import datetime
import requests
import shelve
import json
from profiles import Profile
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
                sorteddb = sorted(playersinfo.items(), key=lambda x: x[1].month_points, reverse=True) # Sort the playersinfo by monthly points, in the reverse order
                allstr = 'Rank: \n'
                for player in sorteddb:
                    c += 1
                    if c == 1: # The first one always will be the winner
                        winner = deepcopy(player[1])
                    try:
                        allstr += f'{self.get_user(player[1].id).mention} : {player[1].month_points}\n'
                    except:
                        pass
                    playersinfo[str(player[1].id)].resetmonth()

                playersinfo.close()
                # sending results
                await gamechannel.send(f'The winner was {self.get_user(winner.id)}, with {winner.month_points} pts! 🎉🎉🎉🎉🎉') if lang == 'en-us' else await gamechannel.send(f'O vencedor foi {self.get_user(winner.id)}, com {winner.month_points} pts! 🎉🎉🎉🎉🎉')
                await gamechannel.send(allstr)
                
            await asyncio.sleep(86400)


    async def scheduled(self):
        global gamechannel # The Minigame channel
        global valid # The stats of game
        global gameinterval # the time between one game session and another
        global color

        while True:
            # Scare Floor
            try:
                if gamechannel == None:
                    await asyncio.sleep(10)
                else:
                    await self.change_presence(status=discord.Status.online, activity= discord.Game(choice(statusmsg)))
                    chance = randint(0,5)
                    print(chance)
                    if valid or chance != 1:
                        await asyncio.sleep(gameinterval) # if the game keeps valid or not choosen
                    else:
                    # Minigame 
                        color = choice(list(emojis.keys()))
                        await gamechannel.send(file= discord.File(open(f'../Assets/monsters_memes/{choice(memes)}', 'rb')))

                        msg = await gamechannel.send(startmsg + react + f' {color}' + '.')
                        for emoji in emojis.values():
                            await msg.add_reaction(emoji)
                        valid = True
                        await asyncio.sleep(gameinterval)
            except:
                pass


    async def on_ready(self):
        global valid
        # logging
        try:
            logfile = open(f'{logpath}/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'a')   
        except:
            logfile = open(f'{logpath}/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'w')
        print(f'Logged on as {self.user} at {datetime.datetime.today()}')
        logfile.write(f'Logged on as {self.user} at {datetime.datetime.today()}\n')
        logfile.close()
        await self.change_presence(status=discord.Status.online, activity= discord.Game(choice(statusmsg)))
        valid = False # do not EDIT this


    async def on_resumed(self):
        # logging
        try:
            logfile = open(f'{logpath}/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'a')   
        except:
            logfile = open(f'{logpath}/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'w')
        
        print(f'Reconnected at {datetime.datetime.today()}')
        logfile.write(f'Reconnected at {datetime.datetime.today()}\n')
        logfile.close()

    async def on_message(self, message):
        # log opening
        try:
            logfile = open(f'{logpath}/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'a')   
        except:
            logfile = open(f'{logpath}/log{datetime.datetime.now().month}-{datetime.datetime.now().year}.txt', 'w')


        global gamechannel
        try:
            perm = message.author.guild_permissions # author permissions
        except:
            pass
        
        # log message that will be stored in a file, and printed in console
        log = f'[{datetime.datetime.now()}]Message from {message.author}: "{message.content}"'
        logfile.write(log + '\n')
        print(log)

        # COMMANDS
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

        if message.content == f'{prefix}meme': # memes
            await message.channel.send('LOL!', file=discord.File(open(f'../Assets/monsters_memes/{choice(memes)}', 'rb')))
        
        if message.content.startswith(f'{prefix}pts'): # Dm message for points
            playersinfo = shelve.open('players.info', 'c') # db open
            # dm validation
            dm = message.author.dm_channel 
            if dm == None:
                await message.author.create_dm()
                dm = message.author.dm_channel
            # message sending
            try:
                await dm.send(f'{message.mentions[0].name} {ptsmsg}:\n total:{playersinfo[str(message.mentions[0].id)].points}, {month}:{playersinfo[str(message.mentions[0].id)].month_points} pts')
            except IndexError:
                try:
                    await dm.send(f'{message.author.name} {ptsmsg}:\n total:{playersinfo[str(message.author.id)].points}, {month}:{playersinfo[str(message.author.id)].month_points} pts')
                except:
                    await dm.send(ptserror)
            except Exception as e:
                print(e)
                await dm.send(ptserror)
            playersinfo.close()
        
        if message.content == f'{prefix}trakinas': # Help trakinas limao
            await message.channel.send(trakinas, file=discord.File(open('../Assets/Trakinas.jpg', 'rb')))
        
        if message.content == f'{prefix}help': # help command
            await message.channel.send(embed=helpmsg)

        if message.content == f'{prefix}cringegif': # random trending gif
            response = requests.get(f'https://api.tenor.com/v1/trending?key=3XHLX8TSY37T') 
            response = json.loads(response.text) # load the json
            if response.status_code != 200 or 202:
                await message.channel.send(giferror)
                return
            # select the right key
            response = response["results"] 
            gif = choice(response)
            gif_format = gif["media"][0]["gif"]
            gif_url = gif_format["url"]

            await message.channel.send(gif_url) # sending

        logfile.close()
        
        
    async def on_reaction_add(self, reaction, user):
        global gamechannel 
        global valid # game status
        global winnerPoints
        global color

        # Win Validation
        if reaction.message.channel == gamechannel != None and valid and reaction.message.content == startmsg + react + f' {color}' + '.' and str(reaction) == emojis[color] and user != self.user: # checks if the reaction is from a valid minigame session and if it's the right emoji
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
            del color

    
    async def on_member_join(self, member):
        # Welcome msg
        dm = member.dm_channel # dm verification
        if dm == None:
            # dm creation
            await member.create_dm()
            dm = member.dm_channel
        # msg sending
        await dm.send(welcomemsg)
    
    
    async def on_member_ban(self, guild, user): # ban message        
        channels = guild.channels
        for channel in channels:
            if str(channel) == banchannel:
                await channel.send(file=discord.File(open('../Assets/ban.gif', 'rb')))
