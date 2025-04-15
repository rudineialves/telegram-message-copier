from telethon.sync import TelegramClient, events

api_id     = 36884619
api_hash   = 'f8d9a9b2e2dd5dfb3174d58f6fc8d041'
id_origem  = -1005781271040 #canal origem
id_destino = -1002285229580 #canal destino


client = TelegramClient('telcopymsg', api_id, api_hash)
client.start()

@client.on(events.NewMessage([id_origem]))
async def main(event):
    await client.send_message(id_destino, event.message.text)

client.run_until_disconnected()







