import nextcord
from nextcord.ext import commands
from bs4 import *
import requests

r = requests.get("https://www.midjourney.com/showcase/recent/")
r = BeautifulSoup(r.text.replace('<!--', '').replace('-->', ''), 'html.parser')
images= r.find('script', {"id": '__NEXT_DATA__'})
images=images.text
images=images.split('"')
a = []
for x in range(0,len(images)):
    if ('https://cdn.midjourney.com' in images[x] and 'image_paths' in images[x-2]):
        a.append(images[x])

bot = commands.Bot(command_prefix='!', intents=nextcord.Intents.all())
@bot.command(name="top")
async def test(ctx):
    for x in range(0,len(a)):
        await ctx.send(a[x])

bot.run("MTA4NjM4NDU1NjE3MDU0NzI4Mg.GozLpO.URjP2J4gsne32508wBeQm5IeEYojl0LgRLu3Bo")























