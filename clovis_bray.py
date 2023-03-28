import os
import random
import asyncio
from dotenv import load_dotenv

import discord
from discord.ext import commands

import aiobungie

from helpers.functions_helpers import build_msg, get_characters_infos, build_embed
from helpers.status_clovis import status_clovis

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(
    command_prefix="/", 
    description="Je suis le grand Clovis Bray I", 
    intents=intents
)

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()


async def change_status():
    while True:
        current_status = random.choice(status_clovis)
        activity = discord.Activity(type=current_status[0], name=current_status[1])
        await client.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(15)


@client.event
async def on_ready():
    print("Intelligence artificiel activée !")
    try:
        synced = await client.tree.sync()
        print(f"Synced : {len(synced)} command(s) !")
    except Exception as e:
        print(e)
    client.loop.create_task(change_status())


@client.event
async def on_guild_channel_create(new_channel: discord.TextChannel):
    if new_channel.name.startswith("id-"):
        channel_to_send = client.get_channel(1072254406004838504)
        msg = build_msg(new_channel)
        await channel_to_send.send(f"@everyone {msg}")


@client.tree.command()
async def talk(interaction: discord.Interaction):
    """ Talk to Clovis !
    """
    await interaction.response.send_message("Foutez le camp de ma lune !")


@client.tree.command()
async def register(ctx: discord.Interaction):
    """ Register to Charlemagne
    """
    view = MyView()
    view.add_item(discord.ui.Button(
        label="S'inscrire", 
        style=discord.ButtonStyle.green, 
        url="https://warmind.io/auth/discord", 
        emoji="✔️"
        )
    )
    await ctx.response.send_message("Cliquez sur 'S'inscrire' pour vous associer à Charlemagne !", view=view)


@client.tree.command()
async def get_destiny_character(ctx: discord.Interaction, bungie_name: discord.Member):
    """ Get your destiny characters inforamtions
    """
    print(bungie_name.display_name)

    data = await get_characters_infos(client_bungie_api, bungie_name.display_name)
    embed = build_embed(bungie_name, ctx.user.display_name, data)

    await ctx.response.send_message(
        f"Récupérations des informations de l'utilisateur {bungie_name.display_name}", 
        embed=embed
    )


load_dotenv(dotenv_path="config")
client_bungie_api = aiobungie.Client(os.getenv('BUNGIE_API_TOKEN'))
client.run(os.getenv("TOKEN"))
