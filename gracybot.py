import discord
from discord.ext import commands
from discord import app_commands
import aiohttp
from datetime import datetime, timedelta, timezone
import logging

import config

from typing import Optional, Tuple, Sequence

logger = logging.getLogger("gracybot")

class gracybot(commands.Bot):
    def __init__(self):
        # Load the configuration.
        self.config = config.Config()

        # Declare our intents, which are the things we want to know about as the
        # bot runs.
        intents = discord.Intents(guilds=True, guild_messages=True)

        # Set up an HTTP request tracer that will let us know what the current
        # rate limit is for deletions.
        trace_config = aiohttp.TraceConfig()
        trace_config.on_request_end.append(self._on_request_end)

        # Since on_ready may be called more than once during a bot session, we need to
        # make sure our main loop is only run once.
        # See <https://discordpy.readthedocs.io/en/stable/api.html#discord.on_ready>
        # This function is not guaranteed to be the first event called. Likewise, this
        # function is *not* guaranteed to only be called once. This library implements
        # reconnection logic and thus will end up calling this event whenever a RESUME
        # request fails.
        self.started = False

        super().__init__(commands.when_mentioned, intents=intents, help_command=None, http_trace=trace_config)