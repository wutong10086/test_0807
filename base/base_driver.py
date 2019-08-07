from appium import webdriver


def get_driver():
    desired_caps = dict()
    # 需要连接的手机的平台(不限制大小写)
    desired_caps['platformName'] = 'Android'
    # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
    desired_caps['platformVersion'] = '5.1'
    # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
    desired_caps['deviceName'] = '192.168.146.101:5555'
    # 需要启动的程序的包名
    desired_caps['appPackage'] = 'com.android.contacts'
    # 需要启动的程序的界面名
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    desired_caps["noReset"] = True
    desired_caps["automationName"] = 'Uiautomator2'

    # 连接appium服务器，相当于管家rd
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
