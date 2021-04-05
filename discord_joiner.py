import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time


invite = input("Discord Invite Link: ")
interval = input("Interval Between Join [2 Decimal Spaces]")
print("Webhooks Are used To Get Notified When Its Finished")

if len(invite) > 6:
    invite = invite[19:]

apilink = "https://discordapp.com/api/v6/invite/" + str(invite)

print(invite)

with open('tokens.txt', 'r') as handle:
    tokens = handle.readlines()
    for x in tokens:
        token = x.rstrip()
        headers = {
            'Authorization': token
        }
        requests.post(apilink, headers=headers)
        time.sleep(float(interval))

    embed = DiscordEmbed(
    title="Joined Server | Status Success",
    description="All tokens have joined the server successfully",
    color='27FF00'
)


with open('webhook.txt', 'r') as handle:
    webhookadd22 = handle.readlines()
    webhook = DiscordWebhook(url=webhookadd22, username="Discord Server Joiner Made By Possible#0999")
    webhook.add_embed(embed)
    response = webhook.execute()
    exit(0)