from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

# 1. 定位：通过 ID 属性
driver.get('https://mail.163.com/register/index.htm?from=163navi&regPage=163')



# 2. 定位之后立即操作
driver.find_element_by_id('username').send_keys('hejiachen')

driver.find_element_by_id('password').send_keys('19990902a')

driver.find_element_by_id('phone').send_keys('17601065885')


# 3. 定位并点击“同意”按钮
driver.find_element_by_id('service').click()


# 4. 定位并点击“立即注册”按钮
driver.find_element_by_class_name('register-option').click()


# 停顿(线程等待)一下
sleep(10)

# 7. 关闭浏览器
driver.quit()