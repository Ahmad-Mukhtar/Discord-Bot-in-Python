import discord
import time
import asyncio

client = discord.Client()
users = []
current_mssg_user = current_mssg = ""


async def update_state():
    await client.wait_until_ready()
    global current_mssg_user, current_mssg

    while not client.is_closed():
        try:
            print(f"""Time : {time.time()} User: {current_mssg_user} Message: {current_mssg}""")
            current_mssg_user = current_mssg = ""
            await asyncio.sleep(5)

        except Exception as e:
            print(e)
            await asyncio.sleep(5)


def gettoken():
    return "read token from file"


def getId():
    return 872100274154664007


mytoken = gettoken()
channels = ["commands", "Yaiwo"]
commands = ["!Users", "!Hi"]
bad_words = ["buri", "sad", "f u"]


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            print(f"""Welcome to the Server {member.mention}""")


@client.event
async def on_message(mssg):
    for word in bad_words:
        if word in mssg.content:
            print("A bad word said")
            try:
                await mssg.channel.purge(limit=1)
            except Exception as e:
                print(e)

    if mssg.author not in users:
        users.append(str(mssg.author))

    global current_mssg_user, current_mssg

    current_mssg_user = str(mssg.author)

    current_mssg = str(mssg.content)

    if str(mssg.channel) in channels:
        ServerId = client.get_guild(getId())
        if mssg.content.find("!Hi") != -1:
            await mssg.channel.send("Hi")
        if mssg.content == "!Users":
            await mssg.channel.send(f"""# no of members {ServerId.member_count}""")
        if mssg.content == "!help":
            desc = ""
            for comds in commands:
                desc += comds + "\n"

            print(desc)

            embed = discord.Embed(title="Bot Help", description="Some useful Commands")

            embed.add_field(name="Commands", value=desc, inline=False)

            await mssg.channel.send(content=None, embed=embed)
    else:
        if str(mssg.content) in commands:
            await mssg.channel.send("You can Only use Commands in the Following Channels\n")
            for chanls in channels:
                await mssg.channel.send(chanls + "\n")

            print(f"""User: {mssg.author} tried to do command {mssg.content} in channel {mssg.channel}""")


# client.loop.create_task(update_state())
client.run(gettoken())
