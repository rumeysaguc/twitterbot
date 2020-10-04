from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
from adres import email, password


url = 'https://www.twitter.com/login'
browser = webdriver.Chrome()

browser.get(url)
browser.maximize_window()
time.sleep(3)


emailInput = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
passwordInput = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")

emailInput.send_keys(email)
passwordInput.send_keys(password)
buton = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span")
buton.click()

