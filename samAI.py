import requests
import json
import discord
import asyncio
intents = discord.Intents.all()
from discord.ext import commands

bot = commands.Bot(command_prefix='?', intents=intents)
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	await bot.process_commands(message)
     
@bot.command(aliases=['a1'])
async def ai(ctx, *, message=None):
    if message is None:
        await ctx.send('Enter a prompt')
        value = await bot.wait_for('message', timeout=60)
    else:
         value = message

    if value.content == 'quit':
            print(f'if quit loop')
            await ctx.send('Quitting calculator program.')
            return
    try:
        # Extract necessary information from the message
        author_name = value.author.name
        author_id = value.author.id
        channel_name = value.channel.name
        channel_id = value.channel.id
        message_content = value.content
        # Create a dictionary with the extracted information
        message_data = {
            "author_name": author_name,
            "author_id": author_id,
            "channel_name": channel_name,
            "channel_id": channel_id,
            "content": message_content
        }

        # Convert the dictionary to a JSON string Send it to API as JSON
        jsonValue = json.dumps(message_content, indent=0)

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                    "Authorization": "Bearer OPENROUTER_TOKEN_HERE",
                    "Content-Type": "application/json",
                },
            json=({
                    "model": "moonshotai/moonlight-16b-a3b-instruct:free",
                    "messages": [
                         {
                         "role": "user",
                         "content": jsonValue
                         }
                    ],   
            })
        )
        data =response.json() #needs to be called data and json no idea
        #print(f'data {data}')
        info = data["choices"][0]["message"]["content"]
        json_string = json.dumps(info, indent=4)
        #print(f'At the json_string {json_string}')
        await ctx.send(f'the answer is {info}')
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
bot.run('DISCORD_BOT_TOKEN_HERE')
