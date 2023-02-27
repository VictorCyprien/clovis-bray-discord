import discord
from discord.ext import commands

client = commands.Bot(
    command_prefix="/", 
    description="Je suis le grand Clovis Bray I", 
    intents=discord.Intents.default()
)

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()


@client.event
async def on_ready():
    print("Intelligence artificiel activée !")
    activity = discord.Activity(type=discord.ActivityType.watching, name="la tombe de Raspoutine")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.tree.command()
async def talk(interaction: discord.Interaction):
    """ Talk to Clovis !
    """
    await interaction.response.send_message(f"Foutez le camp de ma lune !")

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


client.run('MTA3OTgzODA4NjM4MjQ4NTU0NA.GVViWm.wKoEhFldLcjs28Gx_MxK9CEalRJLQtt63LXDXE')
