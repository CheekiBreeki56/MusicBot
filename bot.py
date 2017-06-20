from discord.ext import commands
import json

"""First file for the bot, this handles most functionality for now"""

bot = commands.Bot(command_prefix="!")


# all extensions loaded on startup
on_startup_extensions = [
    'modules.definitions'
]


def load_credentials():
    with open('config/config.json') as config_file:
        return json.load(config_file)

running = None  # Not sure if i need this honestly, keeping it just in case i need it later


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')


@bot.event
async def on_resume():
    # Currently doesnt do anything. It will sometime, maybe.
    bot.running = True
    await bot.say('Resumed :D')


@bot.event
async def on_pause():
    # Currently doesnt do anything. It will sometime, maybe.
    bot.running = False
    await bot.say('Paused :c')


if __name__ == '__main__':
    config = load_credentials()

    # clientID = config["clientID"]
    token = config["token"]

    # loads all of the extensions in on_startup_extensions
    for extension in on_startup_extensions:
        bot.load_extension(extension)
    bot.change_presence(game="CHEEKI BREEKI", status="None", afk="False")
    bot.run(token)

