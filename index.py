import discord
import base64
import os
current_path = os.path.dirname(os.path.realpath(__file__))
import random
import string
import asyncio
import smtplib
import datetime
import sys
from time import sleep
from discord.ext import commands
from email.mime.text import MIMEText
from email.header import Header
from colorama import Fore, init
emails = [ "youremail@gmail.com", "youremail2@gmail.com", "youremail3@gmail.com" ]
init(convert=True)
bot = commands.Bot(command_prefix="$")
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="EuteMuin Commands", color=0x9e64b9)
    # embed.add_field(name="$", value="", inline=True)
    embed.add_field(name="$help", value="Shows this message", inline=True)
    embed.add_field(name="$token", value="Steal some1`s token by User ID ", inline=True)
    embed.add_field(name="$eumu", value="Returns all EuteMuin servers.", inline=True)
    embed.add_field(name="$usneme", value="Get user`s username by User ID", inline=True)
    embed.add_field(name="$tokenmap", value="Token Map", inline=True)

    embed.add_field(name="$encode", value="Encode. Example: $encode base64 hi", inline=True)
    embed.add_field(name="$decode", value="Decode. Example: $decode base64 encoded_text", inline=True)

    embed.add_field(name="$software", value="Example: $software build, category list: build, scripts", inline=True)
    embed.add_field(name="$avat", value="Get user`s avatar by User ID", inline=True)
    embed.add_field(name="$srvi", value="Server info by server invite", inline=True)
    embed.add_field(name="$opens", value="Open Source", inline=True)
    embed.add_field(name="$i", value="Get user`s all info by User ID", inline=True)
    embed.add_field(name="$gmail", value="Gmail spammer (example: $gmail 10 helloworld@gmail.com hello)", inline=True)
    embed.set_footer(text="EuteMuin Team. [ https://discord.gg/E7wt4dr7Pe ]")
    await ctx.send(embed=embed)
@bot.command()
async def eumuapi(ctx):
    await ctx.send("https://github.com/MapleHackersoff/EuMu-API")
@bot.command()
async def opens(ctx):
    await ctx.send("https://github.com/MapleHackersoff/TLT-EuteMuinBot")
@bot.command()
async def ftoken(ctx):
    await ctx.send("This command is deleted!")
@bot.command()
async def software(ctx,*, arg0):
    if(arg0 == "build"):
        embed0=discord.Embed(title="Software Build", description=" ",color=0x9e64b9)
        embed0.add_field(name="Windows 10 Default", value="https://pastebin.com/PD4B7jJG", inline=True)
        embed0.add_field(name="Windows 10 Hacking",value="https://pastebin.com/23d980sB", inline=True)
        embed0.add_field(name="Android 7-11 Hacking",value="https://pastebin.com/t9UL0zp8 ||https://drive.google.com/file/d/1-3pj1u-cyqD77xg0G_wonYpHIXe2xw1-/view||", inline=True)
        embed0.add_field(name="Windows 10 Hacking",value="https://pastebin.com/23d980sB", inline=True)
        await ctx.send(embed=embed0)
    if(arg0 == "scripts"):
        embed2=discord.Embed(title="Scripts", description=" ",color=0x9e64b9)
        embed2.add_field(name="OWOP SilverBot",value="https://pastebin.com/17zDNnAP", inline=True)
        embed2.add_field(name="OWOP J-Bot",value="https://pastebin.com/YPUb8vf9", inline=True)
        embed2.add_field(name="OWOP Chess Tool",value="https://pastebin.com/7bmLHKFJ", inline=True)
        embed2.add_field(name="OWOP Robot Controller",value="https://pastebin.com/xxagqpP9", inline=True)
        embed2.add_field(name="OWOT Command Handler",value="https://pastebin.com/PzeD2yF4", inline=True)
        embed2.add_field(name="OWOT DragonHaxx v5.1",value="https://pastebin.com/euaGRwxx", inline=True)
        embed2.add_field(name="OWOT Dragonhaxx v3.0",value="https://pastebin.com/Fk5dWBVR", inline=True)
        await ctx.send(embed=embed2)
@bot.command()
async def srvi(ctx, *, arg):
	ivapi = "https://discord.com/api/v8/invites/"+arg
	embed6=discord.Embed(title="User Info by User ID", description=arg,color=0x9e64b9)
	embed6.add_field(name="Invite Code API", value=ivapi, inline=True)
	await ctx.send(embed=embed6)
@bot.command()
async def token(ctx, *, arg):
    stoken = base64.b64encode(str(arg).encode()).decode()
    await ctx.send(stoken)
@bot.command()
async def usneme(ctx, *, arg):
    user = await bot.fetch_user(arg)
    await ctx.send(user.name)
@bot.command()
async def tokenmap(ctx):
    await ctx.send("https://i.imgur.com/7WdehGn.png")
@bot.command()
async def avat(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
@bot.command()
async def i(ctx, *,arg):
    user = await bot.fetch_user(arg)
    stoken1 = base64.b64encode(str(arg).encode()).decode()
    av4 = "https://discord.com/api/v8/users/" + arg
    sleep(1)
    embed1=discord.Embed(title="User Info by User ID", description=arg,color=0x9e64b9)
    embed1.add_field(name="Username", value=user.name, inline=True)
    embed1.add_field(name="User ID", value=arg, inline=True)
    embed1.add_field(name="Token", value=stoken1, inline=True)
    embed1.add_field(name="Users API", value=av4, inline=True)
    await ctx.send(embed=embed1)
@bot.command()
async def eumu(ctx):
    await ctx.send("https://discord.gg/2jC8h2Bacx\nhttps://discord.gg/xHAnUZZcw2\nhttps://discord.gg/BXgwgHpBva\nhttps://discord.gg/GAFwZU4MBT")
@bot.command()
async def gmail(ctx,count=None,bomb_email=None,*,message=None):
    if count == None or bomb_email == None or message == None:
        pass
    else:
        x = int(count)
    if x > 25:
        await ctx.send("`That's a lot of spam. Do 25 or less!`")
    else:
        currentDT = datetime.datetime.now()
        hour = str(currentDT.hour)
        minute = str(currentDT.minute)
        second = str(currentDT.second)
        print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} [Command used] - {ctx.author.name}#{ctx.author.discriminator}:{Fore.RESET} !email {count} {bomb_email} {message}")
        counting = int(0)
        embed=discord.Embed(title=f"{counting}/{count}", color=0xff0000)
        embed.set_author(name="Email sent!")
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
        embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        msg = await ctx.send(embed=embed)
        for i in range(x):
            emailsch = random.choice(emails)
            if(emailsch == "youremail@gmail.com"):
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.starttls()
                mail.login('youremail@gmail.com', '123')
                mail_recipient = bomb_email
                mail_body = message
                msget = MIMEText(mail_body, 'plain', 'utf-8')
                msget['Subject'] = Header(" ", 'utf-8')
                mail.sendmail('eumuhakkerz@gmail.com', mail_recipient, message)
                mail.close()
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Message Sent:{Fore.RESET} {message} {Fore.GREEN}To {Fore.RESET}{bomb_email}")
                counting = counting + 1
                embed=discord.Embed(title=f"{counting}/{count}", color=0xff0000)
                embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
                embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
                await msg.edit(embed=embed)
            if(emailsch == "youremail@gmail.com"):
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.starttls()
                mail.login('youremail@gmail.com', '123')
                mail_recipient = bomb_email
                mail_body = message
                msget = MIMEText(mail_body, 'plain', 'utf-8')
                msget['Subject'] = Header(" ", 'utf-8')
                mail.sendmail('eumuhakkerz@gmail.com', mail_recipient, message)
                mail.close()
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Message Sent:{Fore.RESET} {message} {Fore.GREEN}To {Fore.RESET}{bomb_email}")
                counting = counting + 1
                embed=discord.Embed(title=f"{counting}/{count}", color=0xff0000)
                embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
                embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
                await msg.edit(embed=embed)
            if(emailsch == "youremail@gmail.com"):
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.starttls()
                mail.login('youremail@gmail.com', '123')
                mail_recipient = bomb_email
                mail_body = message
                msget = MIMEText(mail_body, 'plain', 'utf-8')
                msget['Subject'] = Header(" ", 'utf-8')
                mail.sendmail('eumuhakkerz@gmail.com', mail_recipient, message)
                mail.close()
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Message Sent:{Fore.RESET} {message} {Fore.GREEN}To {Fore.RESET}{bomb_email}")
                counting = counting + 1
                embed=discord.Embed(title=f"{counting}/{count}", color=0xff0000)
                embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
                embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
                await msg.edit(embed=embed)

        embed=discord.Embed(title="Succes!", color=0x00ff00)
        embed.set_author(name="Done spamming!")
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
        await msg.edit(embed=embed)

bot.run("token")
