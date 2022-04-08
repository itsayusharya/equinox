
import os
from fnmatch import fnmatch

import discord
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        self.prefix = "!"
        super().__init__(command_prefix=self.prefix, case_insensitive=True)

    def setup(self):
        exts = [
            "bot.cogs." + os.path.basename(files)[:-3]
            for files in os.listdir('./bot/cogs') if fnmatch(files, '*.py')
        ]

        print('loading extentions...')

        for ext in exts:
            self.load_extension(ext)
            print(f'{ext[9:]} loaded')

    async def on_connect(self):
        print('connecting...')
        self.setup()

    async def on_reconnect(self):
        print('reconnecting...')

    async def on_ready(self):  # When the bot is ready
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="Server"))
        print("I'm in")
        print(bot.user)  # Prints the bot's username and identifier

    def run(self):
        super().run(os.getenv('bot_token'), reconnect=True)


bot = Bot()
