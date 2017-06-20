from discord.ext import commands
import json

"""First file for the bot, this handles most functionality for now"""

bot = commands.Bot(command_prefix="!")

# all extensions loaded on startup
on_startup_extensions = [

]


def load_credentials():
    with open('config/config.json') as config_file:
        return json.load(config_file)




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')


@bot.event
async def on_resume():
    # Will be put into the music module at a later date
    await bot.say('Resumed :D')


@bot.event
async def on_pause():
    # Will be put into the music module at a later date
    await bot.say('Paused :c')


if __name__ == '__main__':
    config = load_credentials()

    # clientID = config["clientID"]
    token = config["token"]

    # loads all of the extensions in on_startup_extensions
    for extension in on_startup_extensions:
        bot.load_extension(extension)

    bot.run(token)

