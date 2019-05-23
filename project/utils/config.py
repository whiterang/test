

class Config:
    desired_caps = {
        "platformName":'Android', 
        "platfrmVersion":"5.1.1", 
        "deviceName":"vivo x6plus", 
        "appPackage":"com.zhihu.android", 
        "appActivity":".app.ui.activity.MainActivity",              #用adb shell dumpsys activity | findstr "mFocusedActivity"获取
        "unicodeKeyboard": True, 
        "resetKeyboard": True
    }