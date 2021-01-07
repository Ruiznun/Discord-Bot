import discord
import youtube_dl
import os
import random
from discord.ext import commands,tasks
from discord.utils import get
from itertools import cycle

client = commands.Bot(command_prefix='.')
status = cycle(['Choosing a Record','Comminting tax fraud','Running from the IRS',
    'Plotting my next crime','Regreting life choices','Casing a bank','Putting on my mask',
    'Wheelman no show','Running from the cops'])

@client.event
async def on_ready():
    change_status.start()
    print("Bot is up")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency *1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    responses = [ 'It is certain','Without a doubt','You may rely on it','Yes definitely',
    'It is decidedly so','As I see it, yes','Most likely','Yes','Outlook good','Signs point to yes',
    'Reply hazy try again','Better not tell you now','Ask again later','Cannot predict now',
    'Concentrate and ask again','Don’t count on it','Outlook not so good','My sources say no',
    'Very doubtful','My reply is no']
    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}')

@client.command(aliases=['clean'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#music portion
@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await channel.connect()

@client.command()
async def leave(ctx):
    if ctx.voice_client is not None:
        return await ctx.voice_client.disconnect()
    else:
        await ctx.send("Not in a channel...can't Leave")

@client.command()
async def play(self,ctx):
    vc = ctx.voice_client
    vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("coffins.mp3")))

@client.command()
async def pause(ctx):
    vc = ctx.voice_client
    vc.pause()

@client.command()
async def resume(ctx):
    vc = ctx.voice_client
    vc.resume()

@client.command()
async def stop(ctx):
    vc = ctx.voice_client
    vc.stop()

@client.command(aliases=['vol'])
async def volume(ctx,num):
    vc = ctx.voice_client
    vol = int(num)
    if vol < 0 or vol > 100:
        return await ctx.send("Enter a volume level between 0 to 100")
    vc.source.volume = vol/100



client.run('[Your Token Here]')
