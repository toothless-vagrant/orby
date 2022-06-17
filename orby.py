#bot.py
import os
import discord
import time
import asyncio

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!")
allow_orb = True

@bot.command(
    help="Example: !orby blue 12"
)

async def orb(ctx, arg1,arg2):
    global allow_orb
    if allow_orb == False:
        await ctx.send("I'm already tracking an orb")
        return
    else:
        try:
            color = arg1
            initialTime = int(arg2)
            if color not in ("green", "blue", "purple", "gold"):
                await ctx.send("Skill issue: Must input green, blue, purple or gold as valid orb colors.")
                return
            if initialTime > 60:
                await ctx.send("Skill issue: I can\'t do timers over 60 minutes long.")
                return
            if initialTime <= 0:
                await ctx.send("Skill issue: Timers don\'t go into negatives, ape.")
                return
            
            # checks passed, set a variable to track single orb only
            allow_orb = False
            time = initialTime
            await ctx.channel.send("Starting timer for {} orb spawning in {} minutes".format(color, initialTime))
            while time > 1:
                try:
                    await ctx.send("in loop for {} {}".format(time,color))
                    if time == 30:
                        await ctx.send("{} minutes until {} orb in Southgrove Escarp".format(time,color))
                    elif time == 20:
                        await ctx.send("{} minutes until {} orb in Southgrove Escarp".format(time,color))
                    elif time == 15:
                        await ctx.send("{} minutes until {} orb in Southgrove Escarp".format(time,color))
                    elif time == 5:
                        await ctx.send("{} minutes until {} orb in Southgrove Escarp".format(time,color))
                    elif time >= 1 and time < 2:
                        await ctx.send("{} minute until {} orb in Southgrove Escarp".format(time,color))
                    time -= 1
                    await asyncio.sleep(60)
                except:
                    break
            allow_orb = True
            await ctx.send("{} orb in Southgrove Escarp is now active".format(color))
        except ValueError:
            await ctx.send("Skill issue: Try including a number value (1-60).")


bot.run(TOKEN)