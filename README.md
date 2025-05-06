# DiscordAI Bot Template 
This is the template based on my SamurAI AI discord bot from one of my channels (using [discord.py](https://github.com/Rapptz/discord.py) ) relying on [openrouter](https://openrouter.ai/) endpoints and using [Moonlight 16b-a3b](https://huggingface.co/moonshotai/Moonlight-16B-A3B), though you could use anything. Can help with questions coding, and fun! May wish to add add'l token limits and "be helpful assistant". Be nice to your AI so it doesn't pick up bad (language) habits! You may want to work on add'l security modules. I have something like that on mine, but figured I'd keep it simple here.

Basically just: 
* plug in your openrouter key/env var
* And your discord bot key/ env var
* And pick the model you want.

Might want to get rid of timeout could cause problems. And there was also some problems with something else I forget.

Since discord has a limit of 2000 characters (4000 with Nitro), this will truncate responses past that and put ...continued. Trigger ai aliased as a1 in deference to US Department of Education.
