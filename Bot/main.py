from bot_commands import *


init = Bot()
init.loop.create_task(init.monthly())
init.loop.create_task(init.scheduled())
init.run(Token)
