from selenium import webdriver
import time
import os
from random import choice
import requests
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time
import timeit
from multiprocessing import Queue
import queue
from bs4 import BeautifulSoup

os.system('cls')


def get_valid_proxy(proxy):
	return 1

def get_proxies():
	options = webdriver.ChromeOptions()
	options.add_argument("log-level=3")
	options.add_argument("--headless")
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(chrome_options=options)
	driver.get("https://sslproxies.org/")
	driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//th[contains(., 'IP Address')]"))))
	ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
	ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
	driver.quit()
	proxies = []
	for i in range(0, len(ips)):
		proxies.append(ips[i]+':'+ports[i])
	return proxies

def trabalhador():
	a = database_videos()
	print("[+] Video escolhido: "+str(a))
	try:
		print('[*] Proxy: *NO PROXY ACTIVE*!!')
		options = webdriver.ChromeOptions()
		options.add_argument('--log-level=3')
		#options.add_argument('--proxy-server=%s' % proxy)
		#options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
		ua = UserAgent()
		options.add_argument('user-agent=%s'%ua.random)
		options.add_argument('--no-sandbox')
		options.add_argument("--headless")
		options.add_argument('--disable-dev-shm-usage')
		options.add_argument('--mute-audio')
		options.add_experimental_option('excludeSwitches', ['enable-logging'])
		driver = webdriver.Chrome(options=options)
		#driver.set_timeout(120)
		driver.get(a)
		driver.refresh()
		driver.refresh()
		driver.refresh()
		driver.refresh()
		driver.refresh()
		prevTitle = driver.title
		try:
			play_button = driver.find_element_by_xpath("//div[@class='ytp-cued-thumbnail-overlay']//button[@class='ytp-large-play-button ytp-button']")
			play_button.click()
			print("[*] VIDEO STARTADO COM SUCESSO!")
		except:
			pass
		time.sleep(10)
		try:
			play_button = driver.find_element_by_xpath("//div[@class='ytp-cued-thumbnail-overlay']//button[@class='ytp-large-play-button ytp-button']")
			play_button.click()
			print("[*] Video pausado por 3s")
		except:
			pass
		time.sleep(3)
		try:
			play_button = driver.find_element_by_xpath("//div[@class='ytp-cued-thumbnail-overlay']//button[@class='ytp-large-play-button ytp-button']")
			play_button.click()
			print("[*] Video startado novamente")
		except:
			pass
		time.sleep(10)
		try:
			play_button = driver.find_element_by_xpath("//div[@class='ytp-cued-thumbnail-overlay']//button[@class='ytp-large-play-button ytp-button']")
			play_button.click()
			print("[*] Video pausado por 3s")
		except:
			pass
		time.sleep(3)
		try:
			play_button = driver.find_element_by_xpath("//div[@class='ytp-cued-thumbnail-overlay']//button[@class='ytp-large-play-button ytp-button']")
			play_button.click()
			print("[*] Video startado novamente")
		except:
			pass
		time.sleep(10)
		time.sleep(30)
		driver.close()
		print('[*] Titulo: '+str(prevTitle))
		print("[+] Trabalho terminado!")
		print("[+] Iniciando outro TRABALHADOR")
		print('---')
		#os.system('taskkill /F /IM chrome.exe')
		trabalhador()
	except Exception as error:
		print('---')
		print("[-] Disconnectando TRABALHADOR: "+str(error))
		driver.close()

for i in range(0,7):
	threading.Thread(target=trabalhador,).start()
#trabalhador()
