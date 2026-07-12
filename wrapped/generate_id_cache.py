"""One-off script: snapshot Discord member/channel names to JSON lookup files.

`wrapped_messages` / `wrapped_reactions` in Supabase only store Discord
user_id and channel_id, never display names. Run this manually before
building a Wrapped to resolve those IDs to current names.

This is NOT the always-on logging bot - it fetches one snapshot and exits.

Usage:
    DISCORD_TOKEN=... DISCORD_GUILD_ID=... python generate_id_cache.py

Requires the Server Members Intent enabled for the bot application in the
Discord Developer Portal.
"""

import json
import os
import sys
from pathlib import Path

import discord

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
DISCORD_GUILD_ID = os.environ.get("DISCORD_GUILD_ID")

if not DISCORD_TOKEN or not DISCORD_GUILD_ID:
    sys.exit("DISCORD_TOKEN and DISCORD_GUILD_ID must both be set")

GUILD_ID = int(DISCORD_GUILD_ID)
OUTPUT_DIR = Path(__file__).resolve().parent
USERS_PATH = OUTPUT_DIR / "users.json"
CHANNELS_PATH = OUTPUT_DIR / "channels.json"

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    guild = client.get_guild(GUILD_ID)
    if guild is None:
        sys.exit(f"Bot is not in guild {GUILD_ID} (or guild cache is empty)")

    await guild.chunk()

    users = {str(member.id): member.display_name for member in guild.members}
    channels = {str(channel.id): channel.name for channel in guild.channels}

    USERS_PATH.write_text(json.dumps(users, indent=2, ensure_ascii=False), encoding="utf-8")
    CHANNELS_PATH.write_text(json.dumps(channels, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Wrote {len(users)} users to {USERS_PATH}")
    print(f"Wrote {len(channels)} channels to {CHANNELS_PATH}")

    await client.close()


client.run(DISCORD_TOKEN)
