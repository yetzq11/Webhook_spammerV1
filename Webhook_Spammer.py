import requests
import threading

# sends a message to the webhook inserted
def send_message(webhook_url):
    while running:
        # can edit the message
        message = "My webhook n000000000000000000000000000000000000000000000000wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"

        # Sends a POST request to the webhook URL
        requests.post(webhook_url, json={"content": message})

        # You can print a message here if you want to confirm that messages are being sent
        print("Message sent to webhook")

def start_sending(webhook_url):
    global running
    running = True
    # Create a thread to continuously send messages
    threading.Thread(target=send_message, args=(webhook_url,)).start()
    print("Sending messages started.")

def stop_sending():
    global running
    running = False
    print("Sending messages stopped.")

# Main function
def main():
    global running
    running = False

    # makes the user enter the webhook url
    input("Enter the webhook URL and press ENTER to continue: ")
    webhook_url = input("Enter the webhook URL: ")

    # Main loop for user input
    while True:
        command = input("Enter 'start' to begin sending messages, 'stop' to stop sending, or 'exit' to quit: ")
        if command == 'start':
            start_sending(webhook_url)
        elif command == 'stop':
            stop_sending()
        elif command == 'exit':
            break
        else:
            print("Invalid command. Please enter 'start', 'stop', or 'exit'.")

if __name__ == "__main__":
    print("Welcome to the Webhook Messenger")
    main()
