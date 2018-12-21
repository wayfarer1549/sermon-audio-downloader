import requests
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
# Create an initial request to download the file
initial_request = requests.get(download_url)

if 'acceptemail.asp' in initial_request.url:
	print("Reached form")
	print("The url is: ", initial_request.url)

	# generate a post request to the form to initiate the download
	form_parameters = {
	'already_in': 'true',
	'cmd': 'download',
	'data': 'ID=' + sermon_ID + '&session=' + sermon_ID,
	'SKIP': 'Maybe Later'}

	# verify the form parameters
	for parameter, key in form_parameters.items():
		print(parameter, key)

	# Create the second request to get the download
	download_request = requests.post(initial_request.url, data=form_parameters)

	
	# Check the received response
	print(download_request.status_code)
	#print(download_request.text)

	# Open the file for saving
	filename = 'sermon-' + sermon_ID + '.mp3'
	file_out = open(filename, 'wb')
	file_out.write(download_request.content)

	# Close the file
	file_out.close()
	

	
else:
	print("The url is actually: ", request.url)

'''
# Open the file for saving
filename = 'sermon-' + sermon_ID + '.mp3'
file_out = open(filename, 'wb')
file_out.write(request.content)

# Close the file
file_out.close()
'''

# Save the file