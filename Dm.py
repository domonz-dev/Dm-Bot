import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import time
import colorsys
import aiohttp
import json
import random
import datetime
import os
from discord import Game, Embed, Color, Status, ChannelType


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="Bot prefix is p!", command_prefix=commands.when_mentioned_or("p!" ), pm_help = True)
client.remove_command('help')


GIPHY_API_KEY = "dc6zaTOxFJmzC"

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='for p!dm @user message', type=2))
        await asyncio.sleep(5)
      



        await client.change_presence(game=discord.Game(name=str(len(set(client.get_all_members())))+' users', type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=str(len(client.servers))+' servers', type=3))
        await asyncio.sleep(5)
        


@client.event
async def on_ready():
     print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
     print('the bot is ready')

     print('created by Mr.Kumar')
     client.loop.create_task(status_task())

def is_owner(ctx):
     return ctx.message.author.id in ["47134234158941195"]

@client.command(pass_context = True)
async def dm(ctx, user: discord.Member, *, msg: str):
   if user is None or msg is None:
       await client.say('Invalid args. Use this command like: ``p!dm @user message``')
   if ctx.message.author.server_permissions.kick_members == False:
       await client.say('**You do not have permission to use this command**')
       return
   else:
       await client.send_message(user, msg)
       await client.delete_message(ctx.message)
       await client.say("DM has sent! :white_check_mark: ")
       
client.run(os.getenv('Token'))
