# -*- coding: utf-8 -*-
# @Time: 2022/10/6 16:01
# @Author: oyret

import re
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def main():
    print("开始签到......")
    chrome_option = Options()
    chrome_options.add_argument('--headless')
    chrome_option.add_argument('--disable-infobars') #去掉chrome正受到自动测试软件的控制的提示
    chrome_option.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"') #添加请求头
    chrome_option.add_argument('lang=zh_CN.UTF-8') #设置默认编码为utf-8
    chrome_option.add_argument('--disable-gpu') # 规避部分谷歌的bug
    # chrome_option.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
    
    browser = webdriver.Chrome(service=Service(chrome_dirver_path), options=chrome_option)
    browser.get(url)
    browser.set_window_size(1000, 600)
    time.sleep(random.randint(5, 10))
    # 点击登录图像
    browser.find_element(by=By.CLASS_NAME, value='login-button').click()
    time.sleep(random.randint(5, 10))
    # 点击账号登录
    browser.find_element(by=By.XPATH, value='//div[@class="dlann"]/div[4]').click()
    time.sleep(random.randint(5, 10))
    # 输入用户名
    browser.find_element(by=By.XPATH, value='//div[@id="zhdlk"]/div/label[2]/input').send_keys(username)
    time.sleep(random.randint(5, 10))
    # 输入密码
    browser.find_element(by=By.XPATH, value='//div[@id="zhdlk"]/div/label[5]/input').send_keys(password)
    time.sleep(random.randint(5, 10))
    # 点击快速登录
    browser.find_element(by=By.XPATH, value='//div[@id="zhdlk"]/div/div[3]/button').click()
    time.sleep(random.randint(5, 10))
    # 显示任务中心
    browser.find_element(by=By.XPATH, value='//ul/li[@class="la-do"]/button').click()
    time.sleep(random.randint(5, 10))
    # 点击任务中心
    browser.find_element(by=By.XPATH, value='//ul/li[@class="you"]/a').click()
    time.sleep(random.randint(5, 10))
    # 点击签到   
    browser.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div[1]/div[2]/ul/li[4]/a').click()
    time.sleep(random.randint(5, 10))
    # 点击关注某人
    browser.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div[1]/div[2]/ul/li[3]/a').click()
    time.sleep(random.randint(5, 10))   
    ## 点击关注
    while browser.find_element(by=By.XPATH, value='//div[@id="primary-home"]/div/div/div/div/label/input').get_attribute('value') < re.search('\d{1,6}', browser.find_element(by=By.XPATH, value="//div[@id='primary-home']/div/div/div/div/label").text)[0]: # 当前页码 < 总页码
        flag = 0 # 是否点击关注的标志
        for i in range(1,17):
            if browser.find_element(by=By.XPATH, value='//ul/li[{}]/div/div[4]/button[1]'.format(i)).text!='已关注':      
                browser.find_element(by=By.XPATH, value='//ul/li[{}]/div/div[4]/button[1]'.format(i)).click()
                flag = 1
                time.sleep(random.randint(5, 10))
                break   
            time.sleep(random.randint(2, 3))  
        if flag == 0:
            browser.find_element(by=By.XPATH, value='//*[@id="primary-home"]/div[2]/div/div/div[2]/a[2]').click() # 下一页
            time.sleep(random.randint(2, 3))  
        else:
            ## 返回任务中心
            for j in range(int(browser.find_element(by=By.XPATH, value='//div[@id="primary-home"]/div/div/div/div/label/input').get_attribute('value'))):  # 页面后退次数由当前页码确定
                browser.back()
                time.sleep(random.randint(5, 10))
            break

    for i in range(3):
        # 点击评论
        browser.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div[1]/div[2]/ul/li[2]/a').click()
        time.sleep(random.randint(5, 10))
        ## 评论
        browser.find_element(by=By.XPATH, value='//div["respond"]/div[3]/div[2]/div[2]/textarea[@id="textarea"]').click()
        time.sleep(random.randint(5, 10))
        browser.find_element(by=By.XPATH, value='//div["respond"]/div[3]/div[2]/div[2]/textarea[@id="textarea"]').send_keys(random.choice(comments))
        time.sleep(random.randint(5, 10))
        browser.find_element(by=By.XPATH, value='//*[@id="respond"]/div[3]/div[3]/div[2]/button[2]').click()
        time.sleep(random.randint(5, 10))
        
        ## 返回任务中心
        browser.back()
        time.sleep(random.randint(5, 10))
        # 刷新页面
        browser.refresh()
        time.sleep(random.randint(5, 10))
    print("签到成功......")
    browser.quit()
     
    
if __name__ == '__main__':
    chrome_dirver_path = '' # chromedriver的绝对路径
    username = '' # 账号
    password = '' # 密码
    url = 'https://zhutix.com/'
    comments = ['很漂亮，我收藏了。','好好看，快来下载。','绝了，符合我的审美。','真不错，很喜欢哦。','真好看啊，强烈推荐。','好看好看，绝绝子。','看着非常不错，试试看。','谢谢分享，嘻嘻嘻。','已下载，真是太好看了。']
    main()
