from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')

sleep(3)
# 在百度首页点击“新闻”，弹出一个新的窗口
driver.find_element_by_partial_link_text('新闻').click()
sleep(3)

# 1. Selenium 一共涉及到两个窗口：百度首页、新闻页面
# 2. 拿到这两个窗口（的句柄）
hds = driver.window_handles
# 打印所有窗口句柄的信息
print(hds)
# 打印当前一共打开了多少个窗口
print(len(hds))
# 当前当前所在窗口句柄
print(driver.current_window_handle)

# 3. 通过句柄切换到我们准备操作的窗口（页面）
driver.switch_to.window(hds[1])
sleep(3)

# 在新打开的新闻页面，点击军事按钮
driver.find_element_by_partial_link_text('军事').click()
sleep(3)

# 在军事页面，打开一篇文章
driver.find_element_by_link_text('我国首艘核潜艇问世，和这玩具有关，美国一气之下将厂..').click()
sleep(3)


# 关闭当前窗口
# 注意：虽然关闭窗口了，但是句柄没有自动切回原始窗口
driver.close()
sleep(5)

# 手工切回到原来的窗口
driver.switch_to.window(hds[0])
# 在百度主页输入"Selenium关键字"并搜索
key_word =driver.find_element_by_id('kw')
key_word.send_keys('Selenium关键字')
bt = driver.find_element_by_id('su')
bt.click()
sleep(3)

# 退出，关闭所有打开的窗口(浏览器)
driver.quit()
