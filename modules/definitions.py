from discord.ext import commands
import requests
from bs4 import BeautifulSoup


class Define:
    """Definitions from Urban diction. I honestly have no idea how i would make unit tests for this."""
    # TODO: Learn how to make unit tests for this hot mess

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, query, *args):
        j = ''
        # Parses html of urban dictionary
        definition_query = ' '.join([query, *args])

        # Cancels definition request if exception occurs
        try:
            urban_definition = requests.get(
                "http://www.urbandictionary.com/define.php?term={}".format(definition_query))

            soup = BeautifulSoup(urban_definition.content, "html.parser")

            await self.bot.say(" ``` Definition of " + j.join(definition_query).strip(",.'") + "```")
            await self.bot.say("```" + soup.find("div", attrs={"class": "meaning"}).text.strip(",.'") + "```")
            await self.bot.say("```Example```")
            await self.bot.say("```" + soup.find("div", attrs={"class": "example"}).text.strip(",.'") + "```")

        except UserWarning as e:
            await self.bot.say('Invalid search term or website is down ¯\_(ツ)_/¯')
            pass


def setup(bot):
    bot.add_cog(Define(bot))
