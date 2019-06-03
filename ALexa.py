import os
os.system("cls")


# ALexa Bot v1 by zAn3.

print("ALexa       -  Multi-Purpose Bot by zAn3!!")
print()
print("Facebook    :  https://facebook.com/saimalihere")
print("Twitter     :  https://twitter.com/zanpsd")
print("Instagram   :  https://instagram.com/saimalihere")
print()

          
# Modules

import discord
from discord.ext import commands
import random


# Command Prefix

client = commands.Bot(command_prefix = "YOUR_PREFIX")


# Events

@client.event
async def on_ready():
    print("Ready to Rock!")

@client.event
async def on_member_join(member):
    print(f'{member} has spawned in this server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')


# Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                   'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Dont count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def about(ctx):
    await ctx.send('Hey There! Im ALexa - A Multipurpose bot developed by zAn3.')
    await ctx.send('Contact the Author :  https://twitter.com/zanpsd')

@client.command()
@commands.has_role('YOUR_ADMIN_ROLE')
async def say(ctx, arg):
    await ctx.send(arg)

@client.command()
@commands.has_role('YOUR_ADMIN_ROLE')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_role('YOUR_ADMIN_ROLE')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


# Auth Key

client.run("YOUR_AUTH_TOKEN")

