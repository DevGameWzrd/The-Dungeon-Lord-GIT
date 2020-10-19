import discord
from discord.ext import commands
import json
import os
import random
from discord import DMChannel

print ("Loading Econemy Bot...")

os.chdir("C:\\Users\\DevCo\\Documents\\Python Files\\EconemyDiscordBot")

client = commands.Bot(command_prefix = "!")

import getpass
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

add_to_startup()

print("Loading Econemy...")

@client.event
async def on_ready():
    print("Bot loaded")

print("Done, gathering commands...")

@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    
    em = discord.Embed(title = f"~{ctx.author.name}'s balance~",color = discord.Color.gold())
    em.add_field(name = ":moneybag: Coins",value = balance_val)
    await ctx.send(embed = em)

@client.command()
async def calculate_balance(ctx, **kwargs):
    kwargs_1 = kills
    kwargs_2 = coins
    kwargs_3 = user
    await open_account(user)
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    balance = wallet_amt + bank_amt
    k = kills
    c = coins
    b = k * k * k + c + balance
    balance_val = b
    users[str(user.id)]["wallet"] == balance_val



@client.command(pass_context=True)
async def gift_free_coins(user, coins):
    
    await open_account(ctx.author)

    users = await get_bank_data()
    
    coins = random.randint(-55, 55)

    earnings = int(coins)
    
    users[str(user.id)]["wallet"] += earnings

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    if bank_amt <= 0:
        await ctx.send("You can't do that!")
        users[str(user.id)]["wallet"] -= earnings
        
    if wallet_amt <= 0:
        await ctx.send("You can't do that!")
        users[str(user.id)]["wallet"] -= earnings

    with open("MainBank.json","w") as f:
        json.dump(users,f)
        return True

    
    

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 25
        users[str(user.id)]["bank"] = 1

    with open("Bank.json","w") as f:
        json.dump(users,f)
        return True

async def get_bank_data():
    with open("Bank.json", "r") as f:
        users = json.load(f)
    return users

async def get_item_data():
    with open("ShopItems.json","r") as f:
        users = json.load(f)
    return users

@client.event
async def on_raw_reaction_add(payload):
    payload = playload
    message_id =  payload.message_id
    if message_id == 766440342949593098:
        user_id =  payload.user_id
        user = await client.fetch_user("705438836406091847")
        await DMChannel.send(user, f"{str(user_id)} just bought something!")

@client.event
async def on_raw_reaction_remove(playload):
    pass

print("Running bot...")
client.run("NzY1NzAyMjkyMjIxMTk4MzQ2.X4Yp1A.ZN31OabRMH2ymXbdhiIisIIVFwk")
