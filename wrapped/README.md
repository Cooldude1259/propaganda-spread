# wrapped

The weekly Discord "Wrapped" story, as a static page for GitHub Pages.

- `index.html` — the whole thing: plain HTML/CSS/vanilla JS, no build step,
  no external framework or script dependency. Open it directly or serve it
  as-is. The stats inside are hardcoded, not fetched at runtime.
- `names.json` — a reference cache of Discord `user_id` -> `{name, avatar}`
  and `channel_id` -> name, so IDs pulled from Supabase's `wrapped_messages`
  / `wrapped_reactions` tables can be resolved to real names without having
  to ask again each time. Not loaded by `index.html` at runtime — it's a
  lookup used when hand-editing the hardcoded stats for a new week.

## Updating for a new week

1. Query the `wrapped_messages` / `wrapped_reactions` tables in Supabase
   for the date range you want (total messages, per-user counts, per-hour
   counts, per-day counts, top emoji, most-reacted message).
2. Resolve the `user_id` / `channel_id` values via `names.json`. Add any
   new IDs to `names.json` as you learn their names.
3. Edit the hardcoded values directly in `index.html` (the `data-count`
   attributes, the avatar `src`, and the text content in each `.scene`
   block).
