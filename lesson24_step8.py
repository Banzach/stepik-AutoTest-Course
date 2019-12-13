from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # Открываем браузер
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
	
    button1 = browser.find_element_by_id('book')
    ourPrice = WebDriverWait(browser, 12).until(
	    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
    button1.click()
	
	# Жмем на кнопку
	#button = WebDrivedWait(browser, 12) .until(
	#    EC.element_to_be_clickable((By.ID, "book"))
	#	)
	#button.click()
	
	# Подтверждаем confirm
	#confirm = browser.switch_to.alert
	#confirm.accept()
	
	# Переходим на новую вкладку
	#new_window = browser.window_handles[1]
	#browser.switch_to.window(new_window)
	
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
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
	

	
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла