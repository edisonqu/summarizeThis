import dotenv
import os
import discord
from discord import Option
from summarize import query

# Initialization for the DOTENV file
dotenv.load_dotenv()

# Initialization for the Discord Bot
bot = discord.Bot()

#making sure that the event is ready
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Slash command for this specific guild
@bot.slash_command(description= "Summarize this Text!")
async def summarize(ctx,prompt:Option(str, description="enter prompt",name= "prompt", required=True)):
    await ctx.defer()
    answer = query({
    "inputs": prompt
    })
    answers = answer[0]['summary_text']
    await ctx.respond("Summarized Text: "+answers)

# Little Easter Egg / Joke about what Elliot ate for lunch today
@bot.slash_command(guild_ids=["984609554836881470"], description= "Did you only eat chips?", name="elliot")
async def wasthatit(ctx,user:Option(discord.Member, "enter prompt",name= "user")):
    await ctx.respond(f"What did you eat this lunch? <@{user.id}>")

# Run the bot
bot.run(os.getenv("DB_TOKEN"))