from nextcord.ext import commands
from nextcord import Embed, Color
import requests, json, random, datetime, asyncio

links = json.load(open("gifs.json"))
bot = commands.Bot(command_prefix=["!", "/dog-"])
# If user says '!hi' then bot should respond w/ 'Hello'
# If user says '!about' then the bot should respond w/ its introduction


@commands.cooldown(1,2.5, commands.BucketType.user)

# The Hi command
@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send("Hello!")
    
@bot.command(name="gm")
async def SendMessage(ctx):
     await ctx.send(":coffee:")
     
@bot.command(name="gn")
async def SendMessage(ctx):
     await ctx.send(":crescent_moon:")

# About the bot command

@commands.cooldown(1,2.5, commands.BucketType.user)
@bot.command(name="about")
async def SendMessage(ctx):
    await ctx.send("Hello person from the universe! My name is DE BOT and I like pizza. I am a BOT and I might send memes if you ask me! (Coming in the next update!) Some of my friends are a high school. (Ok that might be tmi)")
    
#dog-pics command
@commands.cooldown(1,2.5, commands.BucketType.user)
@bot.command(name="dog-pic")
async def Dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)

@commands.cooldown(1,2.5, commands.BucketType.user)
@bot.command(name="gif", aliases=["feed", "play", "sleep"])
async def Gif(ctx): 
     await ctx.send(random.choice(links[ctx.invoked_with]))
    
# Scheduled Msgs
async def schedule_daily_message():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days=1)
    then.replace(hour=8, minute=0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)
    
    channel = bot.get_channel(771203652836655107) 
    
    await channel.send("Good Morning y'all!")
    await channel.send(random.choice(links["play"]))
    

async def schedule_nightly_message():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days=1)
    then.replace(hour=0, minute=0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)
    
    channel = bot.get_channel(771203652836655107) 
    
    await channel.send("It's High Night")
    
async def schedule_noon_message():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days=1)
    then.replace(hour=12, minute=0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)
    
    channel = bot.get_channel(771203652836655107) 
    
    await channel.send("It's High Noon!")

# When bot is alive, displayed in console


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await schedule_daily_message()
    await schedule_nightly_message()
    await schedule_noon_message()
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = Embed(title=f"Slow it down bro.", description=f"Try again in {error.retry_after:.2f}s", color=Color.red())
        await ctx.send(embed=em)
        


# Launching the bot
if __name__ == '__main__':
    bot.run("OTI3Mjc4OTU5MDc3NDkwNjg5.YdH50w.2TbKAqZY6i0iRfNzPWs8-B_D2Mg")
