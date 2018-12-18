# download.py takes a Sermon Audio mp3 ID and saves it to the specified
# directory.

# Prompt the user to enter a Sermon Audio ID for downloading
sermon_ID = input('Enter a Sermon Audio ID to download: ')

# Display the ID
print("The Sermon Audio ID was: ", sermon_ID)

# Build the download URL
base_url = 'https://mp3.sermonaudio.com/download/'
download_url = base_url + sermon_ID + '/' + sermon_ID + '.mp3'

# Display the download URL
print("The download url is: ", download_url)

# Download the file

# Save the file