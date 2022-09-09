from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import ddddocr
import time
import sys
import os


def PostPic(imgbytes):
    '''
    功能: 识别验证码
    参数: 
         imgbytes: 图片的二进制格式
    返回值: 验证码
    '''
    ocr = ddddocr.DdddOcr(show_ad=False)
    res = ocr.classification(imgbytes)
    return res


username = sys.argv[1]  # 用户名
password = sys.argv[2]  # 密码
registerurl = sys.argv[3]  # 登记网址

display = Display(visible=0, size=(800, 800))
display.start()

# Check if the current version of chromedriver exists
chromedriver_autoinstaller.install()
# and if it doesn't exist, download it automatically,
# then add chromedriver to path

chrome_options = webdriver.ChromeOptions()
# Add your options as needed
options = [
    # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
]

for option in options:
    chrome_options.add_argument(option)

while True:
    try:
        # 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
        driver = webdriver.Chrome(options=chrome_options)

        # 2.通过浏览器向服务器发送URL请求
        driver.get(registerurl)

        while True:

            # 3.找到用户名, 并且输入用户名
            # username = driver.find_element(by=By.ID, value='un')
            # username.send_keys(username)
            driver.execute_script(
                f"document.getElementById('un').value='{username}'")

            # 4.找到密码, 并且输入密码
            # password = driver.find_element(by=By.ID, value='pd')
            # password.send_keys(password)
            driver.execute_script(
                f"document.getElementById('pd').value='{password}'")

            # 5.找到验证码图片, 截图
            count = 10
            while True:
                codeimg = driver.find_element(by=By.ID, value='codeImage')
                codeimg.screenshot('codeimg.png')
                with open('codeimg.png', 'rb') as f:
                    code = PostPic(f.read())
                    # 可能出现的两种错误
                if len(code) == 4 and code.isdigit():
                    break
                count -= 1
                if count == 0:
                    count = 10
                    codeimg.click()

            # 6.找到验证码输入框, 并且输入验证码
            # verifycode = driver.find_element(by=By.ID, value='code')
            # verifycode.send_keys(code)
            driver.execute_script(
                f"document.getElementById('code').value='{code}'")

            # 7.点击登录按钮
            driver.execute_script(
                f"document.getElementById('index_login_btn').click()")
            # loginbtn = driver.find_element(by=By.ID, value='index_login_btn')
            # loginbtn.click()

            # 8.判断是否登录成功
            err = None
            try:
                err = driver.find_element(by=By.ID, value='errormsg')
            except:
                pass
            if err == None:
                break

        # 9.删除验证码图片
        os.remove('codeimg.png')

        # 10.点击同意
        driver.execute_script(
            "document.getElementsByClassName('am-button am-button-primary')[0].click()")

        # 11.打印登记时间
        bookst = driver.execute_script(
            "return document.getElementsByName('bookingStartTime')[0].value")
        print(bookst)

        # 12.输入申请理由
        visitcase = driver.find_element(by=By.NAME, value='visitCase')
        visitcase.send_keys('.')

        # 13.点击提交
        driver.execute_script(
            "document.getElementsByClassName('submitbtn')[0].click()")

        # 14.睡眠1秒
        time.sleep(1)

        # 15.打印登记成功
        print('登记成功🚗')

        # 16.输出内容到GitHub_Action_Results.txt, 作为一个项目更新
        # GitHub Action是两个月如果项目不发生更改的话, 会被冻结

        with open('./GitHub_Action_Results.txt', 'w') as f:
            f.write(
                f"This was written with a GitHub action\nBooktime:{bookst}\nStatus:Success")

        # 17.退出循环
        break

    except:
        pass

    finally:
        # 18.关闭浏览器
        driver.close()
        driver.quit()
