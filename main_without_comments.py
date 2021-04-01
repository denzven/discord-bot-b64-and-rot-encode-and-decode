from discord.ext import commands
import os
from keep_alive import keep_alive
import base64
import traceback

bot = commands.Bot(command_prefix="./")

@bot.event
async def on_ready():
    print("the bot is ready")
	
@bot.command()
async def ping(ctx):
    await ctx.send(f"ping ---> {round(bot.latency * 1000)} ms")

@bot.command()
async def encb64(ctx,tag,*,inputb64):
    try:
        outputdec=None
        outputenc=None

        if tag in ["-e","--encode"]: 
            encoded_as_bytes = base64.b64encode(inputb64.encode("utf-8"))
            outputenc = str(encoded_as_bytes , "utf-8")

            await ctx.send(f'your encoded b64 output of `{inputb64}`is ---> `{outputenc}`')

        if tag in ["-d","--decode"]:
            decoded_as_bytes = base64.b64decode(inputb64.encode("utf-8"))
            outputdec = str(decoded_as_bytes , "utf-8")

            await ctx.send(f'your decoded b64 output of `{inputb64}`is ---> `{outputdec}`')

        if outputdec == None and outputenc == None:
            print(f"{outputdec} and {outputenc}")

            await ctx.send("pls check the tag and try again (-e/-d)")

        else:
            print('')

    except Exception:
            traceback.print_exc()
            print("errormsgtrigger")
            await ctx.send('error! pls check the command again!')

@bot.command()
async def rot(ctx,tag:str,num:int,*,inputstr:str):
    try:
        outputstr=None
        inputstr = inputstr
        d = {}
        if tag in ["-e","--encode"]: 
            d = {}
            for c in (65, 97):
                for i in range(26):
                    d[chr(i+c)] = chr((i-num) % 26 + c)
            outputstr = ("".join([d.get(c, c) for c in inputstr]))
            msg = f"your rot{num} encoded is --->"
            await ctx.send(f"{msg} `{outputstr}`")

        if tag in ["-d","--decode"]:
            d = {}
            for c in (65, 97):
                for i in range(26):
                    d[chr(i+c)] = chr((i+num) % 26 + c)
            outputstr = ("".join([d.get(c, c) for c in inputstr]))

            msg = f"your rot{num} decoded is --->"
            await ctx.send(f"{msg} `{outputstr}`")

        if outputstr == None and inputstr == None:
            print(f"{inputstr} and {outputstr}")
            await ctx.send("pls check the tag and try again (-e/-d)")

        else:
            print('')
            print(f"{inputstr} and {outputstr}")

    except Exception:
        traceback.print_exc()
        print(f"{inputstr} and {outputstr} and {tag}")

keep_alive()
bot.run(os.getenv("BOTTOKEN"))