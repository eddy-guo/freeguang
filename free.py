import os, discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    global guild
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'\n{bot.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )
    global free
    free = guild.get_member(386687850025844749)
    await free.move_to(None)

@bot.event
async def on_voice_state_update(member, before, after):
    if member.id == 386687850025844749:
        await member.move_to(None)

# @bot.command()
# async def gift(ctx):
#     await ctx.send("<@386687850025844749>, please check your dms :3")
#     await free.create_dm()
#     await free.dm_channel.send("Happy birthday froguang, please claim your RP card - **XXX XXX XXXX**")
#     await free.dm_channel.send("See you tomorrow <3")

bot.run(TOKEN)