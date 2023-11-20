# Function to open Notepad
import subprocess

# Function to open Notepad
def open_notepad():
    try:
        subprocess.Popen(["notepad.exe"])
        print("Notepad opened successfully.")
    except FileNotFoundError:
        print("Error: Notepad not found or unable to open.")


def open_chrome():
    try:
        subprocess.Popen(["C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"])
        print("Chrome opened successfully.")
    except FileNotFoundError:
        print("Error: Chrome not found or unable to open.")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to interact with WhatsApp
def whatsapp_interaction():
    try:
        # Path to the Chrome webdriver (update with the path to your chromedriver executable)
        webdriver_path = "path_to_chromedriver"

        # Initialize the Chrome webdriver
        driver = webdriver.Chrome(webdriver_path)

        # Open the web version of WhatsApp
        driver.get("https://web.whatsapp.com/")
        print("Please scan the QR code to log in to WhatsApp.")

        # Wait for the user to scan the QR code and log in
        input("Press Enter after scanning the QR code and logging in to WhatsApp...")

        # Example: Send a message to a contact or group
        target = "Contact or Group Name"
        message = "Hello from Python!"

        # Locate the search input field
        search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()

        # Enter the contact or group name
        search_box.send_keys(target)
        time.sleep(2)

        # Select the chat
        selected_chat = driver.find_element_by_xpath(f'//span[@title="{target}"]')
        selected_chat.click()

        # Locate the message input field
        message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
        message_box.click()

        # Send the message
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
        print(f"Message sent to {target}.")

        # Close the browser
        driver.quit()
    except Exception as e:
        print(f"Error interacting with WhatsApp: {e}")

# Call the function to interact with WhatsApp
whatsapp_interaction()


import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email
def send_email():
    try:
        # Email configuration
        sender_email = "your_email@gmail.com"
        receiver_email = "recipient_email@gmail.com"
        subject = "Test Email from Python"
        body = "This is a test email sent from a Python program."

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, "your_password")
        smtp_server.send_message(message)
        smtp_server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to receive emails
def receive_email():
    try:
        # Email configuration
        username = "your_email@gmail.com"
        password = "your_password"

        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("inbox")

        # Search for emails
        result, data = mail.search(None, "ALL")
        mail_ids = data[0]
        id_list = mail_ids.split()

        # Fetch the most recent email
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]

        # Parse the raw email
        email_message = email.message_from_bytes(raw_email)
        print("Subject:", email_message["Subject"])
        print("From:", email_message["From"])
        print("Body:", email_message.get_payload(decode=True).decode())
    except Exception as e:
        print(f"Error receiving email: {e}")

# Call the function to send an email
send_email()

# Call the function to receive emails
receive_email()


import requests

# Function to send an SMS
def send_sms():
    try:
        # SMS gateway configuration
        api_key = "your_api_key"
        sender_id = "SENDERID"
        receiver_number = "RECIPIENT_NUMBER"
        message = "Test SMS from Python"

        # Send the SMS using the SMS gateway API
        url = f"https://api.smsgatewayprovider.com/send?apikey={api_key}&senderid={sender_id}&number={receiver_number}&message={message}"
        response = requests.get(url)
        if response.status_code == 200:
            print("SMS sent successfully.")
        else:
            print("Failed to send SMS.")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# Function to receive SMS
def receive_sms():
    try:
        # SMS API configuration
        api_key = "your_api_key"

        # Fetch the latest SMS using the SMS API
        url = f"https://api.smsprovider.com/receive?apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            sms_data = response.json()
            print("Received SMS:", sms_data)
        else:
            print("Failed to receive SMS.")
    except Exception as e:
        print(f"Error receiving SMS: {e}")

# Call the function to send an SMS
send_sms()

# Call the function to receive SMS
receive_sms()


import openai

# Set your OpenAI API key
api_key = "your_api_key"
openai.api_key = api_key

# Function to interact with ChatGPT
def chatgpt_interaction(prompt):
    try:
        # Send a prompt to ChatGPT and receive a response
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150
        )
        print("ChatGPT response:", response.choices[0].text.strip())
    except Exception as e:
        print(f"Error interacting with ChatGPT: {e}")

# Example prompt for ChatGPT
prompt = "You: Hello, how are you today?\nChatGPT:"

# Call the function to interact with ChatGPT
chatgpt_interaction(prompt)


from geopy.geocoders import Nominatim

# Function to retrieve geolocation
def retrieve_geolocation(address):
    try:
        # Initialize the geolocator
        geolocator = Nominatim(user_agent="geoapiExercises")

        # Retrieve geolocation based on the address
        location = geolocator.geocode(address)
        if location:
            print("Address:", address)
            print("Latitude and Longitude:", (location.latitude, location.longitude))
        else:
            print("Geolocation not found for the address:", address)
    except Exception as e:
        print(f"Error retrieving geolocation: {e}")

# Call the function to retrieve geolocation
retrieve_geolocation("New York City, NY")


import tweepy

# Set your Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to retrieve current trends on Twitter
def retrieve_twitter_trends():
    try:
        # Retrieve current trends for a specific location (e.g., worldwide)
        trends = api.trends_place(id=1)  # id=1 corresponds to the global trends
        if trends:
            print("Current Twitter trends:")
            for trend in trends[0]["trends"]:
                print("- " + trend["name"])
        else:
            print("No trends found.")
    except Exception as e:
        print(f"Error retrieving Twitter trends: {e}")

# Call the function to retrieve current trends on Twitter
retrieve_twitter_trends()



# Set your Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to retrieve top 10 posts of specific hashtags
def retrieve_top_hashtags(hashtags):
    try:
        for hashtag in hashtags:
            print(f"Retrieving top 10 posts for #{hashtag}...")
            # Retrieve top 10 posts for the specific hashtag
            for tweet in tweepy.Cursor(api.search, q=f"#{hashtag}", lang="en", result_type="popular", tweet_mode="extended").items(10):
                print(f"Tweet: {tweet.full_text}")
    except Exception as e:
        print(f"Error retrieving top posts for specific hashtags: {e}")

# Call the function to retrieve top 10 posts of specific hashtags
retrieve_top_hashtags(["python", "datascience"])

import requests
from bs4 import BeautifulSoup

# Function to retrieve data from a Wikipedia page
def retrieve_data_from_page(url):
    try:
        # Send an HTTP GET request to the Wikipedia page
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, "html.parser")
            # Extract the main content from the page (e.g., the first paragraph)
            main_content = soup.find("p").get_text()
            print("Retrieved data from the page:")
            print(main_content)
        else:
            print(f"Failed to retrieve data from the page. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error retrieving data from the page: {e}")

# Call the function to retrieve data from a Wikipedia page
retrieve_data_from_page("https://en.wikipedia.org/wiki/Python_(programming_language)")


import pygame

# Function for a simple audio player
def simple_audio_player(audio_file_path):
    try:
        # Initialize the pygame module
        pygame.init()
        # Load the audio file
        pygame.mixer.music.load(audio_file_path)
        # Set the volume (optional)
        pygame.mixer.music.set_volume(0.5)
        # Play the audio file
        pygame.mixer.music.play()
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing the audio: {e}")
    finally:
        # Quit the pygame module
        pygame.quit()

# Call the function to play an audio file
simple_audio_player("path_to_your_audio_file.mp3")


import cv2

# Function for a basic video player
def basic_video_player(video_file_path):
    try:
        # Open the video file
        cap = cv2.VideoCapture(video_file_path)
        # Check if the video file was successfully opened
        if not cap.isOpened():
            print("Error: Unable to open the video file.")
            return
        # Read and display each frame of the video
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Video Player", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error playing the video: {e}")

# Call the function to play a video file
basic_video_player("path_to_your_video_file.mp4")


import pyttsx3

# Function to control speaker sound while speaking text
def control_speaker_sound(text, rate=150, volume=1.0):
    try:
        # Initialize the pyttsx3 module
        engine = pyttsx3.init()
        # Set the speech rate (optional)
        engine.setProperty('rate', rate)
        # Set the speech volume (optional)
        engine.setProperty('volume', volume)
        # Speak the text
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking the text: {e}")
    finally:
        # Stop the engine and exit
        engine.stop()

# Call the function to speak the text with a custom rate and volume
control_speaker_sound("Hello, world!", rate=100, volume=0.5)


# Dictionary mapping menu options to corresponding functions
menu_options = {
    1: open_notepad,
    2: open_chrome,
    3: whatsapp_interaction,
    4: email_interaction,
    5: sms_interaction,
    6: chatgpt_interaction,
    7: retrieve_geolocation,
    8: retrieve_twitter_trends,
    9: retrieve_top_hashtags,
    10: retrieve_data_from_page,
    11: simple_audio_player,
    12: basic_video_player,
    13: control_speaker_sound
}

# Main function to display the menu and perform actions based on user's choice
def main():
    while True:
        print("Menu:")
        for key, value in menu_options.items():
            print(f"{key}. {value.__name__.replace('_', ' ').title()}")
        choice = int(input("Enter your choice (1-13): "))
        if choice in menu_options:
            menu_options[choice]()
        else:
            print("Invalid choice! Please try again.")

# Call the main function to start the program
main()
