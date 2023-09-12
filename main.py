#import selenium webdriver and env files

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv('D:/PROJECTS_TO_UPLOAD_ON_GITHUB/autmatedLoginProcessUsingPyton/venv/.env')

#create a driver for Chrome broweser
driver = webdriver.Chrome()


# Accessing a website where login is attempted
url = 'https://app.hubspot.com/login'
driver.get(url)


#getting the proper username and password input fields and button using their id
username_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'loginBtn')


# Input your login credentials
username_input.send_keys(USER_EMAIL)
password_input.send_keys(USER_PASSWORD)

# Simulate clicking the login button
login_button.click()


# Close the browser window
driver.quit()

