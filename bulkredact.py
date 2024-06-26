import requests
import json
import logging
#This will require python to be installed locally, it's reccomended to use a virtual enviroment to execute this.
# Setup logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Base URL for the API endpoint, replace orgnamehere with the customers orgname
base_url = "https://orgnamehere.api.kustomerapp.com/v1/attachments/"

# Replace apitoken with your api token
headers = {
    'Authorization': 'Bearer apitoken',
    'Content-Type': 'application/json'
}

# List of attachment IDs and file names attachment id is the fist value and the attachment name is the second value. Both are required
attachments = [
("662fd8c829b40685516ae50d", "WhatsApp Video 2024-04-29 at 12.13.04 PM.mp4"),
("663034ef60c066da9760f898", "VID-20240330-WA0114.mp4"),


]

# List to store failed updates
failed_updates = []

# Do not change anyhting below.
def update_attachment(attachment_id, file_name):
    """
    Sends a PUT request to update the attachment and logs the process.
    """
    url = f"{base_url}{attachment_id}"
    json_data = json.dumps({
        "redacted": True,
        "name": file_name
    })
    response = requests.put(url, headers=headers, data=json_data)
    try:
        response.raise_for_status()
        logging.info(f"Successfully updated {file_name}: {response.json()}")
    except requests.exceptions.HTTPError as err:
        logging.error(f"HTTP error occurred for {file_name}: {str(err)} - {response.text}")
        failed_updates.append((attachment_id, file_name))
    except Exception as e:
        logging.error(f"An error occurred for {file_name}: {str(e)}")
        failed_updates.append((attachment_id, file_name))

# Loop through each attachment and update
for attachment_id, file_name in attachments:
    update_attachment(attachment_id, file_name)

# Output the list of failed updates
if failed_updates:
    print("Failed to update the following attachments:")
    for att_id, fname in failed_updates:
        print(f"Attachment ID: {att_id}, File Name: {fname}")
else:
    print("All attachments updated successfully.")