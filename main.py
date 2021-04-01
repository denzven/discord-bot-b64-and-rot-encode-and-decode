#hello frens, this is the more elaborate version that explains whats happening inside the code to learn and better debug it
#so first of all telling that this code has been pulsished to github and you can probably find it on my account https://github.com/denzven 
#this bot was made for the base64 encode and decode and for rot-n for the spyboy Bot
#loved to make this and learnt a lot in the process so thanks a lot to sudowhoami and spyboy owner and the server as a whole
#also, thanks a lot to stackoverflow and a lot of blogs that explianed how this all works

##############################
#this block imports all the necceassary modules
from discord.ext import commands #for discord.py
import os #for the env file with tokken
from keep_alive import keep_alive #a repl.it trick to keep the bot alive without paying
import base64 #ezpz way to do b64 encode
import traceback #neater errors in console and the try/except method didnt show any error... so a workaround for that
###################

bot = commands.Bot(command_prefix="./") #defines the bot with prefix

@bot.event #shows in console when the bot is ready
async def on_ready():
    print("the bot is ready")
	
@bot.command() # standard ping command
async def ping(ctx):
    await ctx.send(f"ping ---> {round(bot.latency * 1000)} ms")

@bot.command() #b64encode command
async def encb64(ctx,tag,*,inputb64):#defines usage and variables
    try:
        outputdec=None#sets then to non to avoid the "reference before" error
        outputenc=None

        if tag in ["-e","--encode"]: #makes available two tags
            encoded_as_bytes = base64.b64encode(inputb64.encode("utf-8")) #encodes the strings into b64 but its in bytes form (ex. b'smtg')
            outputenc = str(encoded_as_bytes , "utf-8") #make the bytes form into usable/outputable utf-8 form

            await ctx.send(f'your encoded b64 output of `{inputb64}`is ---> `{outputenc}`') #outputs it **if** the tag is -e or --encode

        if tag in ["-d","--decode"]: #simialr stuff here jus on reverse
            decoded_as_bytes = base64.b64decode(inputb64.encode("utf-8")) #notice how its base64.b64decode not encode
            outputdec = str(decoded_as_bytes , "utf-8")

            await ctx.send(f'your decoded b64 output of `{inputb64}`is ---> `{outputdec}`')# outputs if the tag is -d or --decode

        if outputdec == None and outputenc == None:
            print(f"{outputdec} and {outputenc}") #safety feature to check bot the dec and enc is none or not

            await ctx.send("pls check the tag and try again (-e/-d)")

        else:
            print('') #if shit happens, jus in case

    except Exception:
            traceback.print_exc()
            await ctx.send('error! pls check the command again!')#simialr checks for errors again.. but this time if there is it spams the console..

@bot.command()  #rot command
async def rot(ctx,tag:str,num:int,*,inputstr:str): #defines usage and variables
    try:
        outputstr=None #makes the output none..
        inputstr = inputstr #and input as input
        d = {}
        if tag in ["-e","--encode"]: #simialar stuff as before.. has two tags available
            d = {} #this is an empty set
            for c in (65, 97): #this brings almost the whole ascii list
                for i in range(26):
                    d[chr(i+c)] = chr((i-num) % 26 + c)#iterates the string and adds "num" to each letter in string c
            outputstr = ("".join([d.get(c, c) for c in inputstr]))#well this joins them all and assigns it to outputstr
            msg = f"your rot{num} encoded is --->"#the msg before..
            await ctx.send(f"{msg} `{outputstr}`") #had to do this because the bot was iterating the msg too before.. so yea.. this fixed it

        if tag in ["-d","--decode"]: #similar are before has two tags available
            d = {}
            for c in (65, 97):
                for i in range(26):
                    d[chr(i+c)] = chr((i+num) % 26 + c)#all is the same code except this is i+num to decode...
            outputstr = ("".join([d.get(c, c) for c in inputstr]))

            msg = f"your rot{num} decoded is --->"
            await ctx.send(f"{msg} `{outputstr}`")

        if outputstr == None and inputstr == None:
            print(f"{inputstr} and {outputstr}")
            await ctx.send("pls check the tag and try again (-e/-d)")#these are the two backup stuff if shit happens

        else:
            print('')
            print(f"{inputstr} and {outputstr}")

    except Exception:
        traceback.print_exc()
        print(f"{inputstr} and {outputstr} and {tag}")

keep_alive()#this si the replit code i explained above at import
bot.run(os.getenv("BOTTOKEN"))#using this method so that noone can see my precious bot tokken..and

#thats all folks.. hope yall liked this and understood its mechanism if you really like it pls star this project at my gihub.. love yall for all! thank you!



#cmon.. i had to get it to hundered.. so yea.. #100linecode yaay!