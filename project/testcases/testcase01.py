import unittest
from utils.pyappium import PyAppium
from utils.config import Config
import time


class TestCase01(unittest.TestCase):

    def setUp(self):
        self.pyappium = PyAppium(desired_caps=Config.desired_caps)
        self.old_driver = self.pyappium.get_origina_driver()
    
    def tearDown(self):
        self.pyappium.quit()
    
    # def test1_login(self):
    #     # pyappium = PyAppium(desired_caps=Config.desired_caps)

    #     def update():                           #获取更新弹窗
    #         gx = ("id","android:id/message")
    #         qx = ("id","android:id/button3")
    #         try:
    #             if self.pyappium.does_exist(gx) == True:
    #                 self.pyappium.click(qx)
    #         except: 
    #             pass
        
    #     update()
    #     phone_login = ("-android uiautomator",'new UiSelector().text("免密码登录")')
    #     login = ("-android uiautomator",'new UiSelector().text("密码登录")')
    #     input_phone = ("id","com.zhihu.android:id/email_input_view")
    #     password = ("id","com.zhihu.android:id/password")
    #     lo = ("id","com.zhihu.android:id/btn_progress")
    #     if self.pyappium.does_exist(login) == True:
    #         self.pyappium.click(login)
        
    #     self.pyappium.type(input_phone,"18892629039")
    #     self.pyappium.type(password,"zggh1141893331")
    #     self.pyappium.click(lo)

    #     update()

    #     notlogin = ("-android uiautomator",'new UiSelector().text("未登录")')
    #     self.pyappium.find_element(notlogin)
    #     self.assertFlase(self.pyappium.does_exist(notlogin))
    #     print("这是登录成功的测试用例")
    



    def test_validation(self):
        '''
        登录
        '''
        def update():                           #获取更新弹窗
            gx = ("id","android:id/message")
            qx = ("id","android:id/button3")
            try:
                if self.pyappium.does_exist(gx) == True:
                    self.pyappium.click(qx)
            except: 
                pass
        
        update()
        phone_login = ("-android uiautomator",'new UiSelector().text("免密码登录")')
        login = ("-android uiautomator",'new UiSelector().text("密码登录")')
        input_phone = ("id","com.zhihu.android:id/email_input_view")
        password = ("id","com.zhihu.android:id/password")
        lo = ("id","com.zhihu.android:id/btn_progress")
        if self.pyappium.does_exist(login) == True:
            self.pyappium.click(login)
        
        self.pyappium.type(input_phone,"18892629039")
        self.pyappium.type(password,"zggh1141893331")
        self.pyappium.click(lo)

        update()
       
        collection = ("id","com.zhihu.android:id/bottom_line")
        self.pyappium.click(collection)
        
        
        
      

        qh = ("-android uiautomator",'new UiSelector().text("上下滑动切换回答")')
        know = ("-android uiautomator",'new UiSelector().text("我知道了")')

        try:
            if self.pyappium.does_exist(qh) == True:
                self.pyappium.click(know)
        except:
            pass
        
        
        q = self.old_driver.find_element_by_id("com.zhihu.android:id/question_title")
        question = q.text
        

        time.sleep(20)
        sc = ("-android uiautomator",'new UiSelector().text("收藏")')
       

        sc = ("accessibility id", "收藏")
        # sc = ("xpth",'//android.webkit.WebView[@content-desc="知乎 - 知乎"]/android.view.View/android.view.View[49]/android.widget.Image[2]')
        # sc = ("xpth",'//android.view.View[@content-desc="收藏"]')


        moren = ("id","com.zhihu.android:id/collection_layout")
        complete = ("id","com.zhihu.android:id/button_layout")
        self.pyappium.click(sc)

        # self.old_driver.find_elements_by_accessibility_id("收藏").click()
        self.pyappium.click(moren)

        self.pyappium.click(complete)


        self.pyappium.back()

        notlogin = ("-android uiautomator",'new UiSelector().text("我的")')
        self.pyappium.click(notlogin)

        collection2 = ("id","com.zhihu.android:id/mine_collection_num")
        self.pyappium.click(collection2)

        co = ("-android uiautomator",'new UiSelector().text("默认收藏")')
        self.pyappium.click(co)

        time.sleep(10)                                          #得加等待时间
        testquestion = self.old_driver.find_element_by_id("com.zhihu.android:id/content_title").text
        

        self.assertEqual(question,testquestion)

        print("这是收藏测试用例")
   