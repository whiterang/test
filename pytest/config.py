class Config:
    desired_caps = {
        "platformName":'Android', 
        "platfrmVersion":"5.1.1", 
        "deviceName":"vivo x6plus", 
        "appPackage":"io.appium.android.apis", 
        "appActivity":".ApiDemos", 
        "unicodeKeyboard": True, 
        "resetKeyboard": True
    }

    zhihu_desired_caps = {
        "platformName":'Android', 
        "platfrmVersion":"5.1.1", 
        "deviceName":"vivo x6plus", 
        "appPackage":"com.zhihu.android", 
        "appActivity":".app.ui.activity.MainActivity", 
        "unicodeKeyboard": True, 
        "resetKeyboard": True
    }