import discord
from discord.message import Message
from src.config import settings
from src.util import save_message, load_messages
from src.llm import summarize_with_query

MESSAGE_STORE = "data/messages.json"

# Discord Client
class SummarizerClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message: Message):
        if message.author.bot:
            return

        log_entry = f"{message.author.name}: {message.content}"
        print(log_entry)

        # Save the message
        save_message(log_entry)

        # Handle !summarize command
        if message.content.startswith("!summarize"):
            query = message.content.replace("!summarize", "").strip()
            await message.channel.send("Summarizing...")

            messages = load_messages()
            summary = summarize_with_query(messages, query)

            # If summary is a dict (from RetrievalQA), get 'result'
            if isinstance(summary, dict):
                summary = summary.get("result", "[No summary returned]")

            # Discord message limit is 2000 characters
            max_len = 2000
            for i in range(0, len(summary), max_len):
                await message.channel.send(f"Summary:\n{summary[i:i+max_len]}")

# Intents and run
intents = discord.Intents.default()
intents.message_content = True
client = SummarizerClient(intents=intents)
client.run(settings.BOT_TOKEN)
