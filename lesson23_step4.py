from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    # Открываем браузер
	browser = webdriver.Chrome()
	browser.get(link)
	
	# Жмем на кнопку - получаем результат
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	
	# Подтверждаем confirm
	confirm = browser.switch_to.alert
	confirm.accept()
	
	# Считываем значение x и считаем его, вызывая функцию
	number1 = browser.find_element_by_id("input_value")
	y = calc(number1.text)
	
	# Вписываем ответ в поле 
	input1 = browser.find_element_by_id("answer")
	input1.click()
	input1.send_keys(y)
	
	# Отмечаем чекбокс
	#checkbox1 = browser.find_element_by_id("robotCheckbox")
	#checkbox1.click()
	
	# Отмечаем радиобуттон
	#rbutton = browser.find_element_by_id("robotsRule")
	#browser.execute_script("window.scrollBy(0, 100);")
	#rbutton.click()
	
	# Жмем на кнопку
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	

	
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла