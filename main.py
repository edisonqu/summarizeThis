
# This example requires the 'message_content' intent.

import discord
import dotenv
import os
dotenv.load_dotenv()
import discord
from discord import Option
from summarize import query


bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=["984609554836881470"], description= "Summarize this Text!")
async def summarize(ctx,prompt:Option(str, description="enter prompt",name= "prompt")):
    # await ctx.channel.trigger_typing()
    answer = query({
    "inputs": prompt
})
    print(prompt)
    print(answer[0]['summary_text'])
    answers = answer[0]['summary_text']
    try:
        await ctx.respond(f"Summarized Text: {answers}")
    except:
        await ctx.send(f"Summarized Text: {answers}")

@bot.slash_command(guild_ids=["984609554836881470"], description= "Is that it?", name="food")
async def wasthatit(ctx,user:Option(discord.Member, "enter prompt",name= "user")):
    if user == None:
        user = ctx.author
    await ctx.respond(f"Was that it? @{user}")


bot.run(os.getenv("DB_TOKEN"))