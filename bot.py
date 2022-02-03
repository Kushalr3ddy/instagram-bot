from selenium import webdriver
from time import sleep
import pickle
import os
import json
limit=10
tag="meme"
url="https://www.instagram.com/accounts/login/?force_classic_login"
tag_url=f"https://www.instagram.com/explore/tags/{tag}/"
browser = webdriver.Firefox()


limit=10
username ="your_username_here"
password="your_password_here"

def login():
    browser.get(url)
    sleep(3)
    print("logging in...")
    browser.find_element_by_xpath("//*[@id=\"id_username\"]").click()
    browser.find_element_by_xpath("//*[@id=\"id_username\"]").send_keys(username)
    browser.find_element_by_xpath("//*[@id=\"id_enc_password\"]").click()
    browser.find_element_by_xpath("//*[@id=\"id_enc_password\"]").send_keys(password)

    browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[3]/input").click()
    print("logged in")

    
    pickle.dump(browser.get_cookies(), open("cookies.pkl","wb"))
    print("stored session cookies")
    

    sleep(5)
    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/di/html/body/div[5]/div/div/div/div[3]/button[2]v[3]/button[2]").click()

def comment():
    count=1
    browser.get(url)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        print("loading cookies")
        browser.add_cookie(cookie)
    browser.get(tag_url)
   
    sleep(5)
    try:
        browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        pass
    try:
        while(count<=limit):
            for row in range(1,4):
                for column in range(1,4):
                    #finding each post and clickign on it
                    browser.find_element_by_xpath(f"//*[@id=\"react-root\"]/section/main/article/div[1]/div/div/div[{row}]/div[{column}]/a/div/div[2]").click()
                    sleep(3)
                    #clicking on the comment box
                    browser.find_element_by_xpath("/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").click()
                    browser.find_element_by_xpath("/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").send_keys("testing this shid bot")
                    sleep(2)
                    #clicking on the post button
                    browser.find_element_by_xpath("/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button[2]").click()
                    #exiting the post after commenting
                    sleep(2)
                    browser.find_element_by_xpath("/html/body/div[5]/div[1]/button").click()
                    


    #shid way of handling exceptiony
    except Exception as e:
        print(e)
        pass
        #print("Refreshing page...")
        browser.get(tag_url)     
        print("reloading and waiting for 5 mins...")
        sleep(300)
        print("done waiting reloading script")
        comment()

if os.path.isfile("cookies.pkl")==True:
    pass
    #comment()

else:
    login()

comment()