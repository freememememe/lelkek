import discord
from discord.ext import commands
import os
import json

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Dev: Free Memes#0001'))

@client.command(name='invite',pass_context=True)
async def invite(ctx, *argument):
    invitelink = await ctx.channel.create_invite(max_uses=100,unique=True)
    await ctx.send(invitelink)

@client.command()
async def pfp(ctx, member: discord.Member):
    embed = discord.Embed(title= member.display_name + "'s" + ' profile picture', description=None, color=0x000000)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def myid(ctx):
    
    await ctx.guild.member_count send



@client.command()
async def servericon(ctx):
    embed = discord.Embed(title='Server Icon for ' + ctx.message.guild.name, description=None, color=0x000000)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


@client.command()
async def botinfo(ctx):

    embed= discord.Embed(title="Developer", description="Free Memes#0001")
    embed.add_field(name="Date Released:", value="February 21th, 2021", inline=False)
    embed.add_field(name="Reason for creation", value="i was bored", inline=False)
    embed.set_footer(text="what")
    embed.set_author(name="Joe Biden Bot")


    await ctx.message.channel.send(embed=embed)


@client.command(name='kick', pass_ctx = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):

    await member.kick()
    await ctx.send('gay nigga ' + member.display_name + ' got kicked lmao')


@client.command(name='ban', pass_ctx=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):

 await member.ban(reason=reason)

 myEmbed= discord.Embed(title="User Banned")
 myEmbed.add_field(name=member.display_name, value="got banned lelkek", inline=False)

 await ctx.message.channel.send(embed=myEmbed)
 
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member, reason=None):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"unbanned the biggest gay: {user.mention}")


client.run(os.environ['TOKEN'])