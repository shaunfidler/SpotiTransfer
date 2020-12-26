# SpotiTransfer
Transfer Liked Songs from One Spotify Account to Another

# Purpose
Designed to create a CSV file containing the 'Liked Songs' from an account, containing the date liked, song, artist, and Spotify ID. Then, this CSV file can be loaded and imported into another account. 

# Files
* launch.bat -- Launch this to set the environment variables and load the program
* spotiTransfer.py  -- Python Program to export and imported the liked songs

# Dependencies
* SpotiPy -- https://spotipy.readthedocs.io/
* Spotify Developer ClientID and ClientSecret

# Instructions
**Example case: Moving Liked Songs from Username: OldAccount to Username: NewAccount

* Open launch.bat
0 - Authenticate a User: 
Type the username of the account you want to obtain an access token for and the browser will open up, asking to give the program access to your account. You must either be already logged-in or log in when asked to. 

This process should be done twice to authenticate both the old account and new account. Simply login to the old account, run the authorization to generate a token, then logout. Afterwards, login to the new account and run the authorize selection again, now with the second username. After this, an access token will be stored in a .cache-[USERNAME] file to authorize each of the respective accounts. From here, further actions will be authorized and login will not be necessary. 

For example, in our case we would login to OldAccount, authenticate the account with the program and then logout. Following, login to the NewAccount in the browser and once again authenticate.

1 - Save Songs:
Enter the username of the account you would like to create a file for and the name for the destination file. This will create a .csv file containing the date liked, song, artist, and Spotify ID. 

For example, in our case we would use OldAccount as the username and OldAccount.csv as the filename. Afterwards, 'Liked Songs' from OldAccount would be stored in the CSV file. 

2 - Transfer Saved Songs:
Enter the username of the account you would like to transfer to, followed by the .csv file storing the previous account's 'Liked Songs'. 

For example, in our case we would use NewAccount as the username and OldAccount.csv as the filename. Afterwards, 'Liked Songs' from OldAccount would be imported one by one into the NewAccount, maintaining the original order. There is a one-second delay between each song import to ensure ordering is correct. 

**With the process complete, Liked songs should have been migrated from OldAccount to NewAccount. 
