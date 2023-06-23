
def send_songs(bot,chat, songs):
    for song in songs:
        bot.send_message(chat, f'{song}')
