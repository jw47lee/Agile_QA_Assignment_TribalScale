from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math

PATH = ".\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://qainterview.pythonanywhere.com/')
input_box = driver.find_element_by_name("number")
calculate_box = driver.find_element_by_id("getFactorial")

base_case = "12" 
#extreme_case = "1000"
#edge_case1 = "0"
#edge_case2 = "-1"
bad_input = "s"

def input_num(n, box):
	box.send_keys(n)
	time.sleep(1)

def click_and_wait(box):
	box.click()
	time.sleep(1)

def result():
	result_txt = driver.find_element_by_id("resultDiv")
	return result_txt

def check_non_int_input(s):
	return s == "Please enter an integer"

def check_red_highlight():
	style_txt = input_box.get_attribute("style")
	return "red" in style_txt

def check_red_text(r):
	return "rgb(255, 0, 0)" in r.get_attribute("style")


input_num(base_case, input_box)
click_and_wait(calculate_box)
s = result().text
if(int(s.split()[-1]) == math.factorial(int(base_case))):
	print("PASS")
input_box.clear()

input_num(bad_input, input_box)
click_and_wait(calculate_box)
s = result().text
if(check_non_int_input(s) and check_red_highlight() and check_red_text(result())):
	print("PASS")
input_box.clear()

'''
I used Selenium wiht Python.
Since the question asks me to build two automated *UI* tests,
I focused on UI element of this website.
I used input: 12 for the first case, and string "s" for the second case.
I chose those two cases because those are the cases when UI is changed.
Especially when it receives invalid input, red highlight around the input box and red text appear
So I programmed my automation test to detect that.

'''





