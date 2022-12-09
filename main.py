from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os,sqlite3

def main ():
    pwd = os.getcwd()
    db_pwd = pwd + "/thesmurfssociety.db"
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('SELECT * FROM thesmurfssociety;')
    rows = c.fetchall()
    count=1

    WEB_DRIVER_PATH = pwd + "/tool/chromedriver"
    print(WEB_DRIVER_PATH)
    opt = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=WEB_DRIVER_PATH, options=opt)
    driver.get("https://thesmurfssociety.com/")
    #driver.maximize_window()
    time.sleep(10)
    driver.execute_script("window.scrollBy(0,8500)")
    time.sleep(2)
    for i in rows[0:40]:
        google_email=i[4]
        secret_key = i[3].split(" ")
        address=i[1]
        print("当前循环数量 "+str(count))
        print("当前钱包地址："+str(address))
        print("当前钱包助记词："+str(secret_key))
        print("当前email："+str(google_email))
        emila = driver.find_element(By.XPATH, '//*[@id="smooth-content"]/div/section[10]/div/div[1]/form/div[2]/input')
        emila.send_keys(google_email)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="smooth-content"]/div/section[10]/div/div[1]/form/div[2]/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="smooth-content"]/div/section[10]/div/div[1]/form/div[2]/input').clear()
        count=count+1
        print("&&&&&&&&&&&&&")
        time.sleep(2)

if __name__ == '__main__':
    main()
