import time
import discord
from discord.ext import commands
from discord import Member
import json
import asyncio



# ----------------------------------------------------------------------------------------------------
with open('info.json', "r") as file:
    info = json.load(file)
footer = "https://cdn.discordapp.com/attachments/976965183190736897/1046075721992372346/devby.png"
local_time = time.ctime()
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='+', intents=intents)
bot.remove_command('help')
warnings = {}
# ----------------------------------------------------------------------------------------------------


@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="+help"))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="v1.0"))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="🫀🌍"))
        await asyncio.sleep(3)

# event join
@bot.event
async def on_member_join(member):
    channel_id = bot.get_channel(1030919491066015836)
    embed = discord.Embed(colour=discord.Colour.red())
    embed.add_field(name="Bienvenu à toi :v::anatomical_heart:", value=f"\u200bBienvenu à {member.mention} au sein du {member.guild.name} ! On est {member.guild.member_count} maintenant !:anatomical_heart::earth_africa:", inline=False)
    embed.set_image(url = f"https://i.pinimg.com/originals/54/f1/95/54f195521671388a32fc45f7266923b7.gif")
    embed.set_footer(icon_url=footer,text="Dev par Le M.#6855 et The V#8584")    
    await channel_id.send(embed=embed)  # type: ignore

# event leave
@bot.event
async def on_member_remove(member):
    embed = discord.Embed(colour=discord.Colour.red())
    channel = bot.get_channel(1030919491066015836)
    embed.add_field(name="Aurevoir:v::wave:", value=f"{member.mention} viens de quitter le serveur. On est {member.guild.member_count} maintenant")
    embed.set_image(url="https://i.pinimg.com/originals/23/11/5b/23115b81864a7b2375cc9b464b2e3117.gif")
    embed.set_footer(icon_url=footer,text="Dev par Le M.#6855 et The V#8584")
    await channel.send(embed=embed) #type: ignore

# commande photo pour obtenir la pp d'un membre
@bot.command()
async def pp(ctx, *, member: discord.Member = None): # type: ignore
    embed = discord.Embed(colour=discord.Colour.red())
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar
    embed.add_field(name=member, value=f"Photo de profil de {member}")
    embed.set_image(url=userAvatar)
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/976965183190736897/1046075721992372346/devby.png", text="Dev par Le M.#6855 et The V#8584")
    await ctx.send(embed=embed)

# commande pour inviter le bot sur son propre serveur
@bot.command()
async def invite(ctx,member: discord.Member = None ): # type: ignore 
    if ctx.message.author.id == 976939386509873281:
        embed = discord.Embed(colour=discord.Colour.green())
        embed.add_field(name="Invite", value="https://discord.com/api/oauth2/authorize?client_id=1036329692837445632&permissions=8&scope=bot :white_check_mark:", inline=False)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Invite", value="Ce bot est privé :x:\n\n DM **Le M.#6855** ou **The V#8584** pour l'ajouter", inline=False)
        await ctx.send(embed=embed)

# commande qui permet de verifier la latence entre le bot et l'API
@bot.command()
async def ping(ctx):
    if round(bot.latency * 1000) <= 150:
        embed=discord.Embed(title="PING", description=f"Le ping est de **{round(bot.latency *1000)}** ms", color=0x44ff44)
    elif round(bot.latency * 1000) <= 250:
        embed=discord.Embed(title="PING", description=f"Le ping est de **{round(bot.latency *1000)}** ms", color=0xffd000)
    elif round(bot.latency * 1000) <= 251:
        embed=discord.Embed(title="PING", description=f"Le ping est de **{round(bot.latency *1000)}** ms", color=0xff6600)
    else:
        embed=discord.Embed(title="PING", description=f"Le ping est de **{round(bot.latency *1000)}** ms", color=0x990000)
    await ctx.send(embed=embed)

# commande qui permet de kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member,*, reason=None):
    embed = discord.Embed(colour=discord.Colour.red())
    private_embed = discord.Embed(colour=discord.Colour.red())
    embed.add_field(name=f"{member} est kick :white_check_mark:", value=f"Raison : {reason}")
    private_message = private_embed.add_field(name=f"Tu es kick du {member.guild.name}", value=f"Raison : {reason}")
    await member.send(embed=private_message)
    await ctx.send(embed=embed)
    await member.kick(reason=reason)
    with open('logs.txt', "a") as file:
        logs = file.write(f"{local_time} {member}/kick : {str(reason)}\n")
@kick.error
async def on_command_error(ctx, error): # type: ignore
    if isinstance(error, commands.MissingRequiredArgument):
        embed =discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Erreur", value="Tu dois faire +kick [Mention] [raison]", inline=False)
        await ctx.send(embed = embed)
    if isinstance(error, commands.MissingPermissions):
        embed =discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Erreur", value="Tu n'as pas la permission de faire ça :x:", inline=False)
        await ctx.send(embed=embed)

# commande pour ban
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member,*, reason=None):
    embed = discord.Embed(colour=discord.Colour.red())
    private_embed = discord.Embed(colour=discord.Colour.red())
    embed.add_field(name=f"{member} est ban :white_check_mark:", value=f"Raison : {reason}")
    private_message = private_embed.add_field(name=f"Tu es ban du {member.guild.name}", value=f"Raison : {reason}")
    await member.send(embed=private_message)
    await ctx.send(embed=embed)
    await member.ban(reason=reason)
    with open('logs.txt', "a") as file:
        logs = file.write(f"{local_time} {member}/ban : {str(reason)}\n")

@ban.error
async def on_command_error(ctx, error): # type: ignore
    if isinstance(error, commands.MissingRequiredArgument):
        embed =discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Erreur", value="Tu dois faire +ban [Mention]", inline=False)
        await ctx.send(embed = embed)
    if isinstance(error, commands.MissingPermissions):
        embed =discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Erreur", value="Tu n'as pas la permission de faire ça :x:", inline=False)
        await ctx.send(embed=embed)

# commande pour clear
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"{amount} messages sont supprimés")
    time.sleep(0.4)
    await ctx.channel.purge(limit=1)
    with open('logs.txt', "a") as file:
        logs = file.write(f"{local_time} messages supprimé: {str(amount)}\n")    
@clear.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed =discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Erreur", value="Tu dois faire +clear [valeur]", inline=False)
        await ctx.send(embed = embed)
    if isinstance(error, commands.MissingPermissions):
        embed =discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Erreur", value="Tu n'as pas la permission de faire ça :x:", inline=False)
        await ctx.send(embed=embed)
# commande help
@bot.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name='Liste des commandes')
    # commandes
    embed.add_field(name="+kick" ,value="*+kick [Mention] [raison]*", inline=False)
    embed.add_field(name="+ban", value="*+ban [Mention] [raison]*", inline=False)
    embed.add_field(name="+pp", value="*+pp [Mention]*", inline=False)
    embed.add_field(name="+clear", value="*+clear [valeur]*", inline=False) 
    embed.add_field(name="+ping" , value="Affiche les ping du bot", inline=False)
    embed.add_field(name="+invite", value="Envoie un lien pour inviter le bot sur ton serveur")
    embed.set_image(url="https://i.pinimg.com/originals/81/56/fb/8156fb580959577a185c5bb7c3c8a659.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/976965183190736897/1046030154213904444/qlf.png")
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/976965183190736897/1046075721992372346/devby.png", text="Dev par Le M.#6855 et The V#8584")

    await ctx.send(embed=embed)
    


bot.run(info["token"])
