import discord
from discord.ext import commands
import json


"""First file for the bot, this handles most functionality for now"""


def load_credentials():
    with open('config/config.json') as config_file:
        return json.load(config_file)

config = load_credentials()
clientID = config["clientID"]
token = config["token"]

bot = commands.Bot(command_prefix="!")

running = None


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')


@bot.event
async def on_resume():
    bot.running = True
    print('Resumed :D')


@bot.event
async def on_pause():
    bot.running = False
    print('Paused :c')


@bot.command()
async def add(left : int, right : int):
    await bot.say(left + right)


bot.run(token)

