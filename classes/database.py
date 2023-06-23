import mysql.connector
from mysql.connector import Error


class SongsDatabase:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.database = 'songs'

    def create_database(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = conn.cursor()
            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS {}".format(self.database))
            print("Database 'songs' created successfully or already exists")
        except Error as e:
            print("Error creating database:", e)
        finally:
            if conn.is_connected():
                conn.close()

    def create_table(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS songs (id INT AUTO_INCREMENT PRIMARY KEY, song_name VARCHAR(255), artist_name VARCHAR(255))")
            print("Table 'songs' created successfully or already exists")
        except Error as e:
            print("Error creating table:", e)
        finally:
            if conn.is_connected():
                conn.close()

    def add_song_to_db(self, songs):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = conn.cursor()
            send = []
            for song in songs:
                # Check if the song already exists in the database
                cursor.execute(
                    "SELECT song_name FROM songs WHERE song_name = %s AND artist_name = %s", (song[1], song[2]))
                existing_song = cursor.fetchone()
                # If the song doesn't exist, add it to the database
                if not existing_song:
                    cursor.execute(
                        "INSERT INTO songs (song_name, artist_name) VALUES (%s, %s)", (song[1], song[2]))
                    conn.commit()
                    print("Song added to the database:", song[1])
                    send.append(song[0])
                else:
                    print("Song already exists in the database:", song[1])
        except Error as e:
            print("Error adding songs to the database:", e)
        # Close the database connection
        finally:
            if conn.is_connected():
                conn.close()
                return send
