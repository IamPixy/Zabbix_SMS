import requests
import sys

def send_text_message(username, password, domain, url, sender_number, message, receiver_number):
    headers = {'accept': "application/json", 'cache-control': "no-cache"}
    payload_json = {'senders': [sender_number], 'messages': [message], 'recipients': [receiver_number]}

    try:
        response = requests.post(url, headers=headers, auth=(username + '/' + domain, password), json=payload_json)
        print(response.json())
        print('*****************************************************************')
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Error sending message:", response.text)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python script.py <username> <password> <domain> <URL> <sender_number> <message> <receiver_number>")
    else:
        username, password, domain, url, sender_number, message, receiver_number = sys.argv[1:8]
        send_text_message(username, password, domain, url, sender_number, message, receiver_number)
