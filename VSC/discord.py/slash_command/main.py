from discord import app_command
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=intents)
token = "YourBotToken" 

@bot.tree.command(name='hello', description='testing')  
@app_commands.describe(text1='쓸 내용', text2 = '번호')
async def hello(interaction: discord.Interaction, text1:str, text2:int):    
    await interaction.response.send_message(f'{interaction.user.mention} : {text1} : {text2}', ephemeral=True)

bot.run(token) 

