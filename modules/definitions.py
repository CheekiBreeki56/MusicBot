import discord
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

            em = discord.Embed(title="Definition of " + j.join(definition_query).strip(",.'"),
                               description=soup.find("div", attrs={"class": "meaning"}).text.strip(",.'"),
                               colour=0xDEADBF)
            em.add_field(name="Example", value=soup.find("div", attrs={"class": "example"}).text.strip(",.'"))
            em.set_image(url="http://i3.kym-cdn.com/entries/icons/facebook/000/014/754/c360582e8b14c7420990c3e77b3f22ca.jpg")
            em.set_footer(text="Definition from Urban Dictionary, Bot from CHEEKI BREEKI",
                          icon_url="http://i3.kym-cdn.com/entries/icons/facebook/000/014/754/c360582e8b14c7420990c3e77b3f22ca.jpg")
            em.set_thumbnail(url="http://i3.kym-cdn.com/entries/icons/facebook/000/014/754/c360582e8b14c7420990c3e77b3f22ca.jpg")


            await self.bot.say(embed=em)
            # await self.bot.say(soup.find("div", attrs={"class": "meaning"}).text.strip(",.'"))
            # await self.bot.say("Example")
            # await self.bot.say(soup.find("div", attrs={"class": "example"}).text.strip(",.'"))

        except UserWarning as e:
            await self.bot.say('Invalid search term or website is down ¯\_(ツ)_/¯')
            pass


def setup(bot):
    bot.add_cog(Define(bot))


    # await self.bot.say(" ``` Definition of " + j.join(definition_query).strip(",.'") + "```")
    # await self.bot.say("```" + soup.find("div", attrs={"class": "meaning"}).text.strip(",.'") + "```")
    # await self.bot.say("```Example```")
    # await self.bot.say("```" + soup.find("div", attrs={"class": "example"}).text.strip(",.'") + "```")
