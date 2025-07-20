import discord
from discord.message import Message
from src.config import settings


class SummarizerClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message: Message):
        print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()


intents.message_content = True


client = SummarizerClient(intents=intents)


client.run(settings.BOT_TOKEN)
