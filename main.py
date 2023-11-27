from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

import os

folder_path = '/path/to/folder'
for filename in os.listdir(folder_path):
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, filename.replace(" ", "_")))

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email", "your_password")

msg = "Hello, this is a test email!"
server.sendmail("your_email", "recipient_email", msg)
server.quit()

import pandas as pd

data = pd.read_excel('example.xlsx')
print(data.head())

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.python.org')
print(browser.title)
browser.quit()

import tweepy

consumer_key = 'your_key'
consumer_secret = 'your_secret'
access_token = 'your_token'
access_token_secret = 'your_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status('Hello, this is a test tweet from Python!')

import urllib.request

urllib.request.urlretrieve("https://www.python.org/static/img/python-logo.png", "python-logo.png")

import shutil

shutil.copy2('/path/to/file.txt', '/path/to/destination_folder')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("Hello, Google!")
search.send_keys(Keys.RETURN)

from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
c.drawString(100,750,"Hello, this is a PDF report!")
c.save()