from classes.info import IDS
from classes.database import SongsDatabase
from utils.get_songs import get_songs
from utils.send_songs import send_songs
from pytgbot import Bot

if __name__ == "__main__":
    try:
        # Create the database and table if they don't exist
        songs_db = SongsDatabase(host="localhost", user="root", password="XXXX")
        songs_db.create_database()
        songs_db.create_table()
        number = int(input("Number of songs for each request: "))
        ID = IDS()
        songs = get_songs(ID.spotify_client_id, ID.spotify_client_secret, n_songs=number)
        send = songs_db.add_song_to_db(songs)
        CHAT = ID.telegram_chat_id
        bot = Bot(ID.telegram_api_key)
        if len(send) == 0:
            print(10*'*')
            print('NEW SONGS NOT FOUND')
            print(10*'*')
        else:
            send_songs(bot,CHAT, send)

            print(10*'*')
            print('PROCESS ENDED')
            print(10*'*')

    except Exception as e:
        print(e)
