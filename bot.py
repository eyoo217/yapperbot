import discord
import responses
from discord import FFmpegPCMAudio
from discord.ext import commands


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = '-INSERT DISCORD USER TOKEN HERE-'
    intents = discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.event
    async def on_voice_state_update(member, before, after):
        targetID = #INSERT TARGET USER ID HERE
        channel = client.get_channel() #PLACE MAIN CHANNEL HERE
        punishmentChannel = client.get_channel() #PLACE JAIL CHANNEL HERE
        m_url = 'https://www.youtube.com/watch?v=wFeHYBQe-Sw' #SCREAMING VIDEO LINK

        if not before.channel and after.channel and member.id == targetID:
            await channel.send('Target is in channel')
            await member.move_to(punishmentChannel)
            voice = await member.voice.channel.connect()
            source = FFmpegPCMAudio('screaming.mp3')
            player = voice.play(source)

    client.run(TOKEN)






