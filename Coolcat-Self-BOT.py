import time
import datetime
from time import sleep
import json
import random
import string
from os import system, name
import os
from discord.ext import commands
import colorama
import asyncio
import re
import urllib.parse 
import io
import aiohttp
import discord
import requests
from colorama import Fore
colorama.init()

bot = commands.Bot(command_prefix=("your prefix"), self_bot=True)

token = 'your toke' #ваш токен это важно без него не будет работать смена хайпа
@bot.event
async def on_message(message):
  await bot.process_commands(message)

@bot.event
async def on_ready():
  print(f'''
                                                                   
                                                                   
   SSSSSSSSSSSSSSS                    lllllll    ffffffffffffffff  
 SS:::::::::::::::S                   l:::::l   f::::::::::::::::f 
S:::::SSSSSS::::::S                   l:::::l  f::::::::::::::::::f
S:::::S     SSSSSSS                   l:::::l  f::::::fffffff:::::f
S:::::S                eeeeeeeeeeee    l::::l  f:::::f       ffffff
S:::::S              ee::::::::::::ee  l::::l  f:::::f             
 S::::SSSS          e::::::eeeee:::::eel::::l f:::::::ffffff       
  SS::::::SSSSS    e::::::e     e:::::el::::l f::::::::::::f       
    SSS::::::::SS  e:::::::eeeee::::::el::::l f::::::::::::f       
       SSSSSS::::S e:::::::::::::::::e l::::l f:::::::ffffff       
            S:::::Se::::::eeeeeeeeeee  l::::l  f:::::f             
            S:::::Se:::::::e           l::::l  f:::::f             
SSSSSSS     S:::::Se::::::::e         l::::::lf:::::::f            
S::::::SSSSSS:::::S e::::::::eeeeeeee l::::::lf:::::::f            
S:::::::::::::::SS   ee:::::::::::::e l::::::lf:::::::f            
 SSSSSSSSSSSSSSS       eeeeeeeeeeeeee llllllllfffffffff            
          
                 BBBBBBBBBBBBBBBBB                             tttt          
                 B::::::::::::::::B                         ttt:::t          
                 B::::::BBBBBB:::::B                        t:::::t          
                 BB:::::B     B:::::B                       t:::::t          
                   B::::B     B:::::B   ooooooooooo   ttttttt:::::ttttttt    
                   B::::B     B:::::B oo:::::::::::oo t:::::::::::::::::t    
                   B::::BBBBBB:::::B o:::::::::::::::ot:::::::::::::::::t    
                   B:::::::::::::BB  o:::::ooooo:::::otttttt:::::::tttttt    
                   B::::BBBBBB:::::B o::::o     o::::o      t:::::t          
                   B::::B     B:::::Bo::::o     o::::o      t:::::t          
                   B::::B     B:::::Bo::::o     o::::o      t:::::t          
                   B::::B     B:::::Bo::::o     o::::o      t:::::t    tttttt
                 BB:::::BBBBBB::::::Bo:::::ooooo:::::o      t::::::tttt:::::t
                 B:::::::::::::::::B o:::::::::::::::o      tt::::::::::::::t
                 B::::::::::::::::B   oo:::::::::::oo         tt:::::::::::tt
                 BBBBBBBBBBBBBBBBB      ooooooooooo             ttttttttttt  
   
                        1111111            222222222222222    
                       1::::::1           2:::::::::::::::22  
                      1:::::::1           2::::::222222:::::2 
                      111:::::1           2222222     2:::::2 
vvvvvvv           vvvvvvv1::::1                       2:::::2 
 v:::::v         v:::::v 1::::1                       2:::::2 
  v:::::v       v:::::v  1::::1                    2222::::2  
   v:::::v     v:::::v   1::::l               22222::::::22   
    v:::::v   v:::::v    1::::l             22::::::::222     
     v:::::v v:::::v     1::::l            2:::::22222        
      v:::::v:::::v      1::::l           2:::::2             
       v:::::::::v       1::::l           2:::::2             
        v:::::::v     111::::::111        2:::::2       222222
         v:::::v      1::::::::::1 ...... 2::::::2222222:::::2
          v:::v       1::::::::::1 .::::. 2::::::::::::::::::2
           vvv        111111111111 ...... 22222222222222222222  
    ''')
  print(f"{Fore.YELLOW}бот запущен под аккаунтом {Fore.BLUE}{bot.user}")

bot.remove_command("help")

@bot.command()
async def hype(ctx, house):
  await ctx.message.delete()
  request = requests.session()
  headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
  }

  global payload

  if house == "purple": #HypeSquad Bravery
    payload = {'house_id': 1}
  elif house == "red": #HypeSquad Brilliance
    payload = {'house_id': 2}
  elif house == "blue": #HypeSquad Balance
    payload = {'house_id': 3}

  try:
    requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)
    print(f"{Fore.GREEN}цвет хайпа успешно изменен на {house}")
  except:
    print(f"{Fore.RED}Такого хайпа не существует{house}")

@bot.command(pass_context=True) #спам пример => *spam (число сообщений) (текст)
async def spam(ctx, arg1, *, arg2):
    arg = int(arg1)
    i = 1
    arg3 = arg2
    while i<= arg:
        await ctx.send(f'{arg2}')
        i+=1


@bot.command() #игровая активность пример => *game (и текст активности который вы хотите)
async def game(ctx, *, arg):
  game = arg
  await ctx.message.delete()
  await bot.change_presence(activity=discord.Game(name=f'{game}'))
  print(f"{Fore.YELLOW}успешная операцыя {Fore.BLUE}{bot.user}")
  print(f'{Fore.RED}https://discord.gg/XyPF4xRfCN заходи на наш дс сервер')

@bot.command() #игровая активность пример => *song (и текст активности который вы хотите)
async def song(ctx, *, arg):
  await ctx.message.delete()
  listen = arg
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{listen}'))
  print(f"{Fore.YELLOW}успешная операцыя {Fore.BLUE}{bot.user}")
  print(f'{Fore.RED}https://discord.gg/XyPF4xRfCN заходи на наш дс сервер')

@bot.command() #игровая активность пример => *watch (и текст активности который вы хотите)
async def watch(ctx, *, arg):
  await ctx.message.delete()
  wath = arg
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{wath}'))
  print(f"{Fore.YELLOW}успешная операцыя {Fore.BLUE}{bot.user}")
  print(f'{Fore.RED}https://discord.gg/XyPF4xRfCN заходи на наш дс сервер')

@bot.command() #игровая активность пример => *stream (и текст активности который вы хотите)
async def stream(ctx, *, arg):
  await ctx.message.delete()
  streamm = arg
  #urlld = arg2
  await bot.change_presence(activity=discord.Streaming(name=f'{streamm}', url='https://twich.tv/unknowpage'))
  print(f"{Fore.YELLOW}успешная операцыя {Fore.BLUE}{bot.user}")
  print(f'{Fore.RED}https://discord.gg/XyPF4xRfCN заходи на наш дс сервер')

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  print(f'{Fore.GREEN}*spam, *hype (purple, red, blue), *game, *watch, *song, *stream')
  print(f'{Fore.RED}https://discord.gg/XyPF4xRfCN заходи на наш дс сервер')
  


  
  
bot.run("your token", bot = False)
