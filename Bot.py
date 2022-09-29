import discord #for the discord bot
from robinhood import bp #for the dictionary of the ticker -> img pairs
from commands import * #!commands
from discord.ext import commands #for the discord bot to work
from signals import * #simple rsi stuff
from paper_buys import * #Where we make practice buys
import threading #for multi processes
import datetime

client = discord.Client()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready(): 
    print('WE have logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild): 
    #Creates a role for members to see the rsi bot channel
    role_perms = discord.Permissions(send_messages=False, read_messages=True)
    #name = channel name, permissions = persmissions user has, https://discordpy.readthedocs.io/en/stable/api.html#permissions
    await guild.create_role(name = 'Bot User', permissions = role_perms)
    newCat = await guild.create_category_channel(name = 'RSI Bot') # saves created category into variable 

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages = True, send_messages = False),
    }

    channel = await guild.create_text_channel('Bot Comamnds', overwrites = overwrites, category = newCat)


async def test_signals():
    await client.wait_until_ready()
    channel = client.get_channel(id = 863202522193592320) # Channel ID it sends the message in
    while not client.is_closed():
        time.sleep(11)
        print("")
        print(datetime.datetime.now())
        for ticker in bp.keys():
            ticker += "usdt"
            vals = RSI_Calc(ticker)
            if(vals != "nothing"):
                #Calls the paper buy
#MAKE A BUY DISABLED FOR NOW
#                if(vals["ticker_rsi"] < 30):
#                    if __name__ == "__main__":
#                        # creating thread target = function, args = params
#                       buy_process = threading.Thread(target = make_a_buy, args = (vals["ticker_name"], vals["ticker_price"]))
#                        # starting thread 1
#                        buy_process.start()
                #Posts the Signal
                the_time = datetime.datetime.now()
                if(vals["ticker_rsi"] > 70):
                    color = discord.Colour.green()
                    img = "https://i.gyazo.com/6fa595239e774dd5de4e1b8660373db8.png"
                    action = "SELL"
                else:
                    color = discord.Colour.red()
                    img = "https://i.gyazo.com/3bb125a1e74ab2285357faddb34b6f0e.png"
                    action = "BUY"
                embed = discord.Embed(
                    title = vals["ticker_name"].upper(),
                    description = action,
                    colour = color
                )
                embed.set_image(url = img)

                

                ticker = ticker[:-4]
                coin_pic = 'https://s2.coinmarketcap.com/static/img/coins/64x64/' + str(bp[ticker]) + '.png'
                embed.set_thumbnail(url = coin_pic)

                embed.set_author(name = "RSI-McBot",
                icon_url = 'https://cdn.discordapp.com/attachments/863202522193592320/863222849665630228/https3A2F2Fd1e00ek4ebabms.png')
                embed.add_field(name='Current Price:', value = vals["ticker_price"], inline=False)
                embed.add_field(name='Current RSI (1min):', value = vals["ticker_rsi"], inline=False)
                embed.set_footer(text = 'All prices from Binance Exchange')
                await channel.send(embed=embed)


client_key = "holder"
client.loop.create_task(test_signals())
client.run('client_key')

