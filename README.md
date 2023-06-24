# Song Database Management

This project allows you to manage a song database by retrieving songs from Spotify and storing them in a MySQL database. It also provides the ability to send the added songs to a Telegram chat using a Telegram bot to download.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.11.4
- MySQL database server
- Spotify API credentials
- Telegram bot API token

## Setup Spotify API

To set up the Spotify API in the Spotify Developer Dashboard, follow these steps:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account.

2. Click on "Create an App" or "Create a New App" to create a new application.

3. Provide a name for your application and a short description.

4. Set the redirect URI(s) for your application. This is the URL where Spotify will redirect users after they grant permission to your application. Set the redirect URI to `http://localhost:8888/callback`.
 
5. Click on "Save", you will be redirected to the application dashboard.

6. Click on "Settings" and note down the "Client ID" and "Client Secret" values. You will need these to authenticate and access the Spotify API in the file /classes/info.py.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Song-Database-Management.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the credentials:

   - Spotify API credentials: Open the `classes/info.py` file and replace the `spotify_client_id` and `spotify_client_secret` with your own Spotify API credentials.

   - Telegram bot API token: Open the `classes/info.py` file and replace the `api_key` with your Telegram bot API token.

4. Set up the MySQL database:

   - Create a new database named `songs`.
   - Update the MySQL connection details (host, user, password) in the `classes/database.py` file according to your MySQL setup.

5. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. When prompted, enter the number of songs you want to retrieve from Spotify for each request (Limit of 50).

2. The application will create the database and table if they don't already exist.

3. Songs will be retrieved from Spotify and added to the database. If a song already exists in the database, it will be skipped.

4. The application will print the songs added to the database and send them to the configured Telegram chat using the Telegram bot.

5. If no new songs are found, a message will be displayed indicating that.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or issues, please contact [lsascol01l@gmail.com](mailto:lsascol01l@gmail.com).
