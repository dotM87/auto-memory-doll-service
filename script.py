from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

#here replace the text with the path of your credendials
SERVICE_ACCOUNT_FILE = 'yourcredentials.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

#here replace the text by the id of your spreadsheet
#example: given the url of your spreadsheet https://docs.google.com/spreadsheets/d/abcdefghijklmnopqrstuvwxyz0987654321/edit
#your id would be: abcdefghijklmnopqrstuvwxyz0987654321
SPREADSHEET_ID = 'documentID'

#here put the range where the phone numbers are located in your spreadsheet
RANGE_NAME = 'C2:C18'

service = build('sheets', 'v4', credentials=creds)
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()

values = result.get('values', [])
phone_numbers = ['+591' + value[0] for value in values]

service = Service('/usr/lib/chromium-browser/chromedriver.unstripped')
driver = webdriver.Chrome(service=service)
driver.get('https://web.whatsapp.com/')

#press enter when login has been successful
input('ready?')

for phone_number in phone_numbers:
    link = f"https://web.whatsapp.com/send?phone={phone_number}"
    driver.execute_script(f'window.open("{link}","_blank");')
    driver.implicitly_wait(10)
    message_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="1"]')
    
    #enter here the message you wish to send
    message_box.send_keys('https://chat.whatsapp.com/L8FjY2LrQ4E0u3eTfma5ub')
    
    send_button = driver.find_element("xpath", '//span[@data-icon="send"]')
    send_button.click()
    driver.implicitly_wait(5)
    try:
        alert = driver.switch_to.alert
        alert.dismiss()
    except:
        pass

driver.quit()
