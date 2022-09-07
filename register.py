from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import ddddocr
import time
import sys


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

    # "--headless",
    # "--disable-gpu",
    # "--window-size=1920,1200",
    # "--ignore-certificate-errors",
    # "--disable-extensions",
    # "--no-sandbox",
    # "--disable-dev-shm-usage",
    # '--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

# 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
driver = webdriver.Chrome(options=chrome_options)

# 2.通过浏览器向服务器发送URL请求
driver.get('http://access.hust.edu.cn/IDKJ-P/P/studentHome?data=3F6EB1A2999B2626FAB2DA0D114E4B98F665234B3FB79E5E10F2616C97EBFB5A#/')

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

# 9.点击同意
driver.execute_script(
    "document.getElementsByClassName('am-button am-button-primary')[0].click()")

# 10.输入申请理由
visitcase = driver.find_element(by=By.NAME, value='visitCase')
visitcase.send_keys('.')

# 11.点击提交
driver.execute_script(
    "document.getElementsByClassName('submitbtn')[0].click()")

# 12.睡眠1秒
time.sleep(1)

# 13.关闭浏览器
driver.close()
driver.quit()

# 14.打印登记成功
print('登记成功🚗')
