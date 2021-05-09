import sqlite3
import random
import discord
from discord.ext import commands
from discord.utils import get
import datetime
import asyncio
import time
import json
import os

conn = sqlite3.connect('target.db')

c = conn.cursor()

intents = discord.Intents(messages=True, guilds=True)
client = commands.Bot(command_prefix = 'm.', intents=intents)
client.remove_command('help')

def is_it_me(ctx):
	#insert your id
	return ctx.author.id ==

def memify(text):
	new = []
	for c in text:
		r = random.randint(0,1)
		if r:
			new.append(c.upper())

		else:
			new.append(c.lower())

	return ''.join(new)

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.author.id}: {message.content}: {message.guild}: {message.guild.id}")
	c.execute("SELECT * FROM data WHERE server=? AND user=?", (message.guild.id, message.author.id))
	result = c.fetchone()
	if result is None:
		pass

	else:
		await message.channel.send(memify(message.content))
		await message.channel.send("https://cdn.discordapp.com/attachments/651218357747449906/836372980027097168/mockingspongebobbb.jpg")
	await client.process_commands(message)

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('m.help | Mocking Since 2021'))
	print('Bot Is Online')
	await asyncio.sleep(20)

@client.command()
async def calibrate(ctx):
	await ctx.author.send('Calibration Registered')
	print('Calibration Registered')
	return

@client.command()
@commands.has_permissions(administrator=True)
async def target(ctx, *, member : discord.Member):
	try:
		if member.id == 836238260573175839:
			await ctx.send("Nice Try")

		else:
			c.execute("SELECT * FROM data WHERE server=? AND user=?", (ctx.guild.id, ctx.author.id))
			result = c.fetchone()
			if result is None:
				c.execute("SELECT * FROM data WHERE server=?", (ctx.guild.id,))
				result = c.fetchone()
				if result is None:
					c.execute("INSERT INTO data (server, user) values (?, ?)",
				            (ctx.guild.id, member.id))
					conn.commit()
					await ctx.send(f"I'll mock {member.mention} from now on")

				else:
					sql = ("UPDATE data SET user = ? WHERE server = ?")
					val = (str(member.id), str(ctx.guild.id))
					c.execute(sql, val)
					conn.commit()
					await ctx.send(f"I'll mock {member.mention} from now on")
			else:
				await ctx.send("You think you'll be able to stop me from mocking you just because you're an admin? LMAO")

	except:
		await ctx.send("Hmm, there seems to be a problem. Try again or contact my dev.")


@client.command()
async def mock(ctx, *, message, amount=1):
	username = ctx.author.name
	await ctx.channel.purge(limit=amount)
	await ctx.send(memify(message.content))
	await ctx.send(f'-{username}')
	await ctx.send("https://cdn.discordapp.com/attachments/651218357747449906/836372980027097168/mockingspongebobbb.jpg")
	return

@client.command()
async def roast(ctx):
	options = ['You look like something that I would draw with my left hand.', 'I refuse to have a battle of wits with somebody who is unarmed!', 'If I ever said anything to offend you, it was purely intentional.', 'Im not saying that I hate you, but I would unplug your life support to charge my phone.', 'In spite of what it did to you, dont you love nature?', 'Ive seen someone like you before, but I had to pay admission.', 'You have the perfect face for radio!', 'Youre not as bad as people say. Youre a whole lot worse.', 'Im not sure what your problem is, but Id be wiling to bet that its hard to pronounce.', 'Its pretty easy to figure out when youre lying. Your lips are moving.', 'Wow! You look like a before picture!', 'I wanted to give you a nasty look, but you already had one.', 'I dont think youre un-intelligent. You just have bad luck when it comes to thinking.', 'Brains arent everything. And, in your case, theyre nothing.', 'Its looks like your face caught on fire and somebody tried to extinguish it with a hammer.', 'Its really great to see how you dont let your education get in the way of your ignorance.', 'They say that we all sprang from apes. As it stands, you didnt seem to spring far enough.', 'Im really jealous of everyone that hasnt met you!', 'Most people live and learn. Apparently you just live.', 'There is only one problem with your face...I can see it.', 'So a thought crossed your mind? Well, that journey must have been long and lonely.', 'Its amazing what youve done with your hair! How did you manage to grow it out of your nostrils like that?', 'Hey, theres something on your chin. No, no...the third one down.', 'They say that laughter is the medicine. Seems like your face is curing the world!', 'You were born on a highway right? Because that’s where most accidents happen.']
	await ctx.send(f'{random.choice(options)}')
	return

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms. Stupid')
	return

@client.command()
async def time(ctx):
	x = datetime.datetime.now()
	await ctx.send(x)

@client.command()
async def help(ctx):
	embed = discord.Embed(title='Commands', description='Prefix: m.', colour=discord.Color.blue(), url= 'https://www.google.com')
	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/651218357747449906/836372980027097168/mockingspongebobbb.jpg')

	embed.add_field(name='target <user>', value='Select someone to have me mock in the server. (Requires Admin Permissions)')
	embed.add_field(name='mock <message>', value='Mocks the message inputted')
	embed.add_field(name='roast', value='Outputs a roast')
	embed.add_field(name='ping', value='Shows ping')
	embed.add_field(name='time', value='Tells the time')
	await ctx.send(embed=embed)

@client.command()
@commands.check(is_it_me)
async def shutdown(ctx):
	c.close()
	conn.close()
	await client.close()

@client.command()
@commands.check(is_it_me)
async def fshutdown(ctx):
	c.close()
	conn.close()
	await client.close()

#insert your token
client.run("")
