from selenium import webdriver
import time
import math 

link = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	number1 = browser.find_element_by_id("num1")
	number2 = browser.find_element_by_id("num2")
	sum = int(number1.text) + int(number2.text)
	
	browser.find_element_by_css_selector("[value = sum]").click()
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла