# wrapped

Assets for the weekly Discord "Wrapped" story.

- `Discord_Wrapped.dc.html` - the Stories-style wrapped video component.
- `generate_id_cache.py` - one-off script that snapshots current Discord
  member/channel names into `users.json` / `channels.json`, so the
  `user_id` / `channel_id` values stored in Supabase's `wrapped_messages`
  and `wrapped_reactions` tables can be resolved to display names when
  building a Wrapped. Run it manually, right before building a Wrapped,
  not as a long-running bot.

## Running the cache generator

```
pip install -r requirements.txt
DISCORD_TOKEN=... DISCORD_GUILD_ID=... python generate_id_cache.py
```

Requires the Server Members Intent enabled for the bot application in the
Discord Developer Portal. On success it overwrites `users.json` and
`channels.json` in this directory with a fresh snapshot and exits.
