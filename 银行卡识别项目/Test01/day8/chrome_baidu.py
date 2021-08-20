from time import sleep
from selenium import webdriver

# 1. 打开(新开)一个Chrome浏览器 版本83.0.4.4103
driver = webdriver.Chrome()

# 2. 打开（加载）一个指定页面
driver.get("https://www.baidu.com/")

# 3. 找到百度首页的关键字输入框
# element：页面元素（页面里的所有东西统称元素，如图片、按钮、超链、编辑框等）
key_word = driver.find_element_by_id('kw')

# 4. 在该输入框中输入查询文字： Ak47
key_word.send_keys('AK47')

# 5. 找到（定位到）“百度一下”这个按钮
bt = driver.find_element_by_id('su')

# 6. 模拟操作元素：点击按钮
bt.click()

# 停顿(线程等待)一下
sleep(8)

# 7. 关闭浏览器
driver.quit()



