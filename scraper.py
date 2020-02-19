from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


#Chromedriver installation path
chromedriver_path = 'C:/chromedriver.exe' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(randint(2,3))
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(randint(2,3))

username = webdriver.find_element_by_name('username')
username.send_keys('user')
password = webdriver.find_element_by_name('password')
password.send_keys('pass')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(randint(2,3))

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()

user_list = pd.read_csv('user_list.csv')
user_list = list(user_list['0'])

#Hashtags for scraping
hashtag_list = ['hashtag1','hashtag2','hashtag3']

user_list = []
tag = -1

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5) 
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    first_thumbnail.click()
    sleep(randint(5,7))
    user = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
    print(user)
    user_list.append(user)
    for x in range(1,20):
        sleep(randint(2,3))
        webdriver.find_element_by_link_text('Next').click() 
        sleep(randint(2,3))
        user = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
        print(user)
        user_list.append(user)

#Creates a DataFrame with the unique users from user_list
user_df = pd.DataFrame(set(user_list))
user_df.to_csv('user_list.csv')
 
print('{} users have been added to the list'.format(len(user_list)))

