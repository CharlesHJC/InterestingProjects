from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
# 打开登录页面
driver.get('http://localhost/charleshe/index.asp')

# 完成登录
ipts = driver.find_elements_by_tag_name('input')
ipts[0].send_keys('admin')
ipts[1].send_keys('admin')
ipts[2].click()

sleep(2)
# 从当前默认位置切换到菜单框架中
driver.switch_to.frame('left')

# 点击菜单 系统设置
sysset_css = '.menuall > tbody:nth-child(1) > tr:nth-child(13) > td:nth-child(1)'
driver.find_element_by_css_selector(sysset_css).click()

sleep(2)
# 继续点击：计量单位管理
danwei_css = '#g_6 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(1)'
driver.find_element_by_css_selector(danwei_css).click()
sleep(2)

# 切换原始位置
driver.switch_to.default_content()
# 切到右侧框架
driver.switch_to.frame('right')
sleep(2)

# 点击添加全选框
driver.find_element_by_id('chkall').click()
sleep(2)
# 点击选择删除按钮
shanchu_css = 'input.button:nth-child(2)'
driver.find_element_by_css_selector(shanchu_css).click()
sleep(2)
# 处理弹框
driver.switch_to.alert.accept()
sleep(2)

# 切换原始位置
driver.switch_to.default_content()
# 切到右侧框架
driver.switch_to.frame('right')
sleep(2)

# 点击添加单位按钮
bt_css = 'input.button:nth-child(1)'
driver.find_element_by_css_selector(bt_css).click()
sleep(2)

# 输入单位名称
driver.find_element_by_name('danwei').send_keys('kg')
# 点击确认按钮
driver.find_element_by_name('submit').click()
sleep(2)
# 处理弹框
driver.switch_to.alert.accept()
sleep(2)

# 切换原始位置
driver.switch_to.default_content()
# 切到左侧框架
driver.switch_to.frame('left')
sleep(2)
# 点击产品大类管理
da_css = '#g_6 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)'
driver.find_element_by_css_selector(da_css).click()
sleep(2)

# 切换原始位置
driver.switch_to.default_content()
# 切到右侧框架
driver.switch_to.frame('right')
sleep(2)

# 点击添加大类
add_css = 'input.button:nth-child(1)'
driver.find_element_by_css_selector(add_css).click()
sleep(2)

# 输入大类名称
driver.find_element_by_name('bigclass').send_keys('CLASSmax')
# 点击确认按钮
driver.find_element_by_name('submit').click()
sleep(2)
# 处理弹框
driver.switch_to.alert.accept()
sleep(2)


# 切换原始位置
driver.switch_to.default_content()
# 切到左侧框架
driver.switch_to.frame('left')
sleep(2)
# 点击产品小类管理
xiao_css = '#g_6 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)'
driver.find_element_by_css_selector(xiao_css).click()
sleep(2)

# 切换原始位置
driver.switch_to.default_content()
# 切到右侧框架
driver.switch_to.frame('right')
sleep(2)

# 点击添加小类
addx_css = 'input.button:nth-child(1)'
driver.find_element_by_css_selector(addx_css).click()
sleep(2)

# 随机选择所属大类

sj_css = '.toptable > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > select:nth-child(1)'

# 创建下拉列表
sel_lst = Select(driver.find_element_by_name('bigclass'))

# 获取列表项的数量
lst_count = len(sel_lst.options)
rand = randint(0, lst_count-1)

# 通过随机产生的序号，选择一个列表项
sel_lst.select_by_index(rand)

# 输入小类名称
driver.find_element_by_name('smallclass').send_keys('CLASSmin')
sleep(2)
# 点击确认按钮
driver.find_element_by_name('submit').click()
sleep(2)
# 处理弹框
driver.switch_to.alert.accept()
sleep(2)




# 切换原始位置
driver.switch_to.default_content()

# 切换到顶部框架
driver.switch_to.frame('topFrame')
driver.find_element_by_link_text('安全退出').click()
sleep(2)
driver.switch_to.alert.accept()
sleep(2)
# 关闭浏览器
driver.quit()
