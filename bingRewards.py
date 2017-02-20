# encoding=utf8
import os
import sys
import string
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


# loginUrl = "http://www.bing.com/"
loginUrl ="https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1487226969&rver=6.7.6631.0&wp=MBI&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttp%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1&lc=1033&id=264960"
def main():
	global loginUserName
	loginUserName = ""

	global password 
	password = ""

	login()


def login():

	global loginUserName
	global password 

	chromedriver = "/Users/martinhuang/Desktop/Python/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)


	driver.get(loginUrl)
	
	box = driver.find_element_by_xpath('//*[@id="CredentialsInputPane"]/div[2]/div/div/div[3]/div/div/div[2]/div')
	actions = ActionChains(driver)
	actions.move_to_element(box).send_keys(loginUserName).perform()

	driver.implicitly_wait(3)

	driver.find_element_by_id("idSIButton9").click()

	passwordBox = driver.find_element_by_css_selector('#CredentialsInputPane > div:nth-child(2) > div > div > div:nth-child(8) > div')
	actions = ActionChains(driver)
	actions.move_to_element(passwordBox).send_keys(password).perform()
	driver.implicitly_wait(3)
	# driver.find_element_by_id('i0118').send_keys(password)
	# driver.find_element_by_xpath('//*[@id="i0118"]')
	# signInButton = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
	# actions.move_to_element(signInButton).click(signInButton)
	# driver.find_element_by_xpath('//*[@id="i0118"]').send_keys(password)
	driver.find_element_by_xpath('//*[@id="idSIButton9"]').send_keys("\n")
	driver.refresh()
	time.sleep(2)

	search(driver)

	# pause(driver)
	driver.quit()

def search(driver):
	searchWords = ['testing', 'python', 'selenium', 'chicken', 'overwatch']

	for word in searchWords:
		driver.find_element_by_id('sb_form_q').send_keys(word)
		driver.find_element_by_id('sb_form_go').click()
		driver.find_element_by_id('sb_form_q').clear()
		time.sleep(2)


def pause(webdriver):
	element = WebDriverWait(webdriver, 5).until(
	    	EC.presence_of_element_located((By.ID, "myDynamicElement")))


if __name__ == '__main__':
	main()
