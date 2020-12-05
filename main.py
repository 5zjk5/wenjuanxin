from selenium import webdriver
import random


driver = webdriver.Chrome()


# driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
#安装目录不在python目录下解决办法

driver.get('https://www.baidu.com')
#打开一个主标签页


for i in range(1):

    js = "window.open('https://www.wjx.cn/m/99634699.aspx')"
    #定义一个js语句传给driver.execute_scrip执行：打开新标签页

    driver.execute_script(js)

    #driver.get('https://www.wjx.cn/m/99634699.aspx')

    handlers =driver.window_handles

    driver.switch_to_window(handlers[1])

    # 获得所有问题的页数
    questions = driver.find_elements_by_xpath('//div[@id="divQuestion"]/fieldset')

    # 循环每一页
    for question in questions:
        # 获得此页所有问题
        qs = question.find_elements_by_xpath('./div[@class="field ui-field-contain"]')
        # 循环每个问题
        for q in qs:
            ####先滑到标签再去点击
            driver.execute_script("arguments[0].scrollIntoView();",q)
            ### 找到标签下的所有答案
            ans=q.find_elements_by_xpath('./div[2]/div[@class="ui-radio"]')
            # 随机选择一个答案
            a = random.choice(ans)
            # 点击
            a.click()

        try: # 判断是否是最后一页
            # 点击下一页
            next = driver.find_elements_by_xpath('//div[@id="divNext"]')[0]
            next.click()
        except:
            pass

    # 回答完所有问题后提交
    sub = driver.find_elements_by_xpath('//div[@id="ctlNext"]')[0]
    sub.click()

    #driver.close()

    #driver.switch_to_window(handlers[0])

#driver.quit()