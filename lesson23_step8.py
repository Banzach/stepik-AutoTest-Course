from selenium import webdriver
import time
import math
import os
import pyautogui

	
link = "http://suninjuly.github.io/file_input.html"


try:
    # Открываем браузер -> Выставляем время ожидания прогрузки элементов -> Переходим по ссылке 
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
	
	# Ищем элементы для ввода полей
    f_name = browser.find_element_by_css_selector("[name = 'firstname']")
    f_name.click()
    f_name.send_keys('Sergey')
    l_name = browser.find_element_by_css_selector("[name = 'lastname']")
    l_name.click()
    l_name.send_keys('Yurchenko')
    email = browser.find_element_by_css_selector("[name = 'email']")
    email.click()
    email.send_keys('B@mail')
	
	#Высылаем файл
    change_file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    change_file.send_keys(file_path)
    
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

	
finally:
    # После/вместо завершения действий ждем секунду
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла