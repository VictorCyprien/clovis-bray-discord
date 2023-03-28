from typing import List
import random

import aiobungie

import discord

from helpers.sentence_clovis import hello_sentence, escouades_sentence


def build_msg(new_channel):
    msg = ""
    msg += random.choice(hello_sentence) + "\n"
    msg += random.choice(escouades_sentence) + f" dans le salon {new_channel.mention}"
    return msg


async def get_characters_infos(client: aiobungie.Client, bungie_name: str):
    player_name, digit = bungie_name.split("#")
    async with client.rest:
        player = await client.fetch_player(player_name, digit)
        profile = await player[0].fetch_self_profile([aiobungie.ComponentType.PROFILE])
        profile = profile.profiles
        plateform = profile.type
        membership_id = profile.id
        characters_ids = profile.character_ids

        characters_list = []

        for character_id in characters_ids:
            character = await client.fetch_character(
                membership_id,
                plateform,
                character_id,
                components=[aiobungie.ComponentType.CHARACTERS]
            )
            characters_list.append(character)

    return characters_list


def build_embed(bungie_name: discord.Member, user_who_request_info: str, data: List):
    embed = discord.Embed(
        title=f"Personnages de {bungie_name.display_name}",
        color=discord.Color.green()
    )

    embed.set_author(
        name=bungie_name.display_name,
        icon_url=bungie_name.avatar.url
    )

    embed.set_thumbnail(url=data[0].character.emblem_icon)

    for character in data:
        print(character)

        embed.add_field(
            name=character.character.class_type.name,
            value="\u200b",
            inline=False,
        )

        embed.add_field(
            name="Niveau de lumière",
            value=character.character.light,
        )

        embed.add_field(
            name="Dernière connexion",
            value=character.character.last_played,
        )

        embed.add_field(
            name="Temps de jeu total",
            value=character.character.total_played_time,
        )

    embed.set_footer(
        text=f"Information demandé par {user_who_request_info}"
    )

    return embed
