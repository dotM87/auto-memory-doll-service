# auto-memory-doll-service
This script uses Selenium to automate sending messages on WhatsApp Web to multiple phone numbers. It retrieves the phone numbers from a Google Sheet using the Google Sheets API.

## Installation
To use this script, you will need to install the following dependencies:

* selenium
* google-auth
* google-auth-oauthlib
* google-auth-httplib2
* google-api-python-client

You can install these dependencies using pip:

```sh
pip install selenium google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```
You will also need to download the ChromeDriver executable and replace the SERVICE path in the script with the path to your ChromeDriver executable.

Usage
Before running the script, you need to provide the path to your Google Service Account credentials file and the ID of the Google Sheet containing the phone numbers. You also need to specify the range where the phone numbers are located, and the message you wish to send.

You can then run the script by running:

```sh
auto-memory-doll.py
```

The script will open a new instance of Chrome and prompt you to scan the QR code to login to WhatsApp Web. Once you have logged in, press enter in the terminal to start sending messages.

Note that the script may take a few seconds to send each message, so please be patient. Also note that WhatsApp has anti-spam measures in place, so use this script responsibly and at your own risk.
