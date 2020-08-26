import discord

quotes = ["That is the weirdest thing you’ve ever said.",

"What can I say? The camera loves me.",

"Sulley, I am baring my soul here. The least you can do is pay attention.",

"Dodgeball was the best, oh yeah. I was the fastest one out there. Of course I was the ball.",

"I love you, schmoopsie-poo!",

"Nothing is more important than our friendship.",

"Just the other day someone asked who was the most beautiful monster. You know what I said? I said … Sulley?",

"Where are you going? We’ll talk. We’ll have a latte.",

"Scary feet, scary feet, scary feet!",

"Remember to tip your waitresses.",

"You’ve been jealous of my good looks since the fourth grade.",

"You and I are a team.",

"There’s more to life than scaring.",

"Put that thing back where it came from or so help me!",

"Sull, that’s a cube of garbage.",

"Come on, pal. If you start crying, I’m gonna cry, and I’ll never get through this.",

"You’re the boss, you’re the boss. You’re the big, hairy boss.",

"Fight that plaque. Scary monsters don’t have plaque.",

"One, two, three, four, get the kid back through the door!",

"I don’t like big moving things that are moving towards me.",

"I wasn’t scared. I have allergies." ,

"I don’t believe I ordered a wake-up call, Mikey.",

"Hey, may the best monster win.",

"Give it a rest, will ya, butterball?",

"I’m watching you, Wazowski. Always watching. Always.",

"Your stunned silence is very reassuring.",

"Don’t let it happen again.",

"Go get ’em, googly bear.",

"You expect me to believe that pack of lies, Mike Wazowski?",

"You think this is about sushi?!",

"Do you hear that? It’s the winds of change.",

"Do I look abominable to you? Why can’t they call me the Adorable Snowman, or … or the Agreeable Snowman for crying out loud?",

"I’m a nice guy. Snow cone?",

"Wasteland? I think you mean Wonderland!",

"Milking a yak ain’t exactly a picnic.",

"I’m sorry, Wazowski, but Randall said I’m not allowed to fraternize with victims of his evil plot.",

"""- Mike: I think I have a plan here: using mainly spoons, we dig a tunnel under the city and release it into the wild.
- Sulley: Spoons?
- Mike: That's it, I'm out of ideas. We're closed. Hot air balloon? Too expensive. Giant slingshot? Too conspicuous. Enormous wooden horse? Too Greek.""",

"""- Roz: Wazowski! You didn't file your paperwork last night.
- Mike: Oh, that darn paperwork! Wouldn't it be easier if it all just blew away?
- Roz: Don't let it happen again.
- Mike: Yes, well, I'll try to be more careful next time.
- Roz: I'm watching you, Wazowski. Always watching. Always.""",

"I'm trying to be honest, just hear me out. You and I are a team. Nothing is more important than our friendship.",

"""- Mike: I like everything about you. Just the other day someone asked me who I thought the most beautiful was in all of Monstropolis. You know what I said?
- Celia: What did you say?
- Mike: I said... Sulley!
- Celia: Sulley?!""",

"""- Mike: I can't believe it...
- Sulley: Oh, Mike...
- Mike: I was on TV! Ha! Did you see me? I'm a natural.""",

"Roz, my tender, oozing blossom, you're looking fabulous today. Is that a new haircut? Come on, tell me it's a new haircut, isn't it? It's got to be a new haircut. New makeup? You had a lift? You had a tuck? You had something? Something has been inserted in in you that makes you look... Listen, I need a favor.",

"""- Mike: Boo? What's Boo?
- Sulley: That's... what I decided to call her. Is there a problem?
- Mike: Sulley, you're not supposed to name it. Once you name it, you start getting attached to it.""",

"One of these days I am really... gonna let you teach that guy a lesson.",

"""- Sulley: May the best monster win!
- Randall: I plan to.""",

"""- Sulley: What was that?
- Mike: I have no idea. But it would be a really good idea if it didn't do it again.""",

"Kids, these days. They just don't get scared like they used to.",

"I am so romantic, sometimes I think I should just marry myself.",

"There's nothing more toxic or deadly than a human child. A single touch could kill you. Leave a door open, and one can walk right into this factory; right into the monster world.",

"""- Mike: Psst, Fungus. Fungus, you like cars? Because I got a really nice car. You let me go, I'll give you... a ride... in the car.
- Fungus: I'm sorry, Wazowski, but Randall said I'm not allowed to fraternize with victims of his evil plot.""",

"""- Needleman: So I said, If you talk to me like that again, we're through.
- Smitty: Oh! What did she say?
- Needleman: You know my mom. She sent me to my room.""",

"""I am about to revolutionize the scaring industry, and when I do, even the great James P. Sullivan will be working of me. First I need to know where the kid is, and you're gonna tell me.""",

"""- Mike: All we have to do is get rid of that thing, so wait here while I get its cardkey.
- Sulley: But she can't stay here! This is the men's room.
- Mike: That is the weirdest thing you have ever said.""",

"""- Mike: I'm telling you, Big Daddy. You're gonna be seeing this face on TV more often.
- Sulley: Yeah, like on "Monstropolis' Most Wanted?"""]


# var name == command name
close = 'Bye monsters! See you soon...🧟‍♂️😞'
policy = "I'm a transparent and open source bot, so at the end of every month, search for the transparency channels and see the audit logs and messages logs.🧐🧐🧐 \n github repo: https://github.com/faelbreseghello/Monsters-Bot"
setup = 'Set up! The game is close to start!'
fun = 'Look at this one!:'


# minigame msg
winmsg1 = 'The monster ' # pt1
winmsg2 = ' won the challenge\n -------------------------------' # pt2
startmsg = 'It\'s time to scare! The first to react wins!'
mypts = 'You have '
myptserror = 'Probably you dont started at the game yet :('

#help embed
helpmsg = discord.Embed(title='Commands:', colour = discord.Colour.blue())
helpmsg.set_author(name='Help command')
helpmsg.set_thumbnail(url='https://cdn.discordapp.com/avatars/747449463861149737/38b60ffd2fce04ea1e607179acf70a79.png')
helpmsg.add_field(name='*policy', value='Our monstrous think way.', inline=True)
helpmsg.add_field(name='*setup', value='Sets up the minigame channel. It\'s recommended that only me can message there.', inline=False)
helpmsg.add_field(name='*fun', value='Some little monsters quotes.', inline=True)
helpmsg.add_field(name='*meme', value='A random meme from our scary database🧟‍♂️🧟‍♂️.', inline=False)
helpmsg.add_field(name='*mypts', value='I\'ll send you a dm with your points. :)', inline=True)
helpmsg.add_field(name='*trakinas', value='a charity campaing.', inline=False)
helpmsg.add_field(name='Minigame', value='From time to time there\'s a random chance of a message appears. The first monster to react to it will win the round and earn points. At the end of every month the best will receive a prize.', inline=True)
helpmsg.set_footer(text='*all commands need the standard prefix *. but it could be changed at config.py')

react = ' React with'
trakinas = 'SUPPORT, SUPPORT TRAKINAS LEMON.🍪🍪🍪🍪🍪'

# other
statusmsg = ['Made with ❤️ by faelbreseghello#3092', 'Follow me on twitter: @faelbreseghello', 'I\'m open source!', '*help for see the commands']
welcomemsg = 'Welcome! I\' the Monsters Bot. If you want to know more about me go on my github repo : https://github.com/faelbreseghello/Monsters-Bot.\nMy minigame rules are simple. Be the first to scare and earn points. Then be the best monster and win!🧟‍♂️🧟‍♂️🧟‍♂️🧟‍♂️'
month = 'monthly'

