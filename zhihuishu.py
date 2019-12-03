# -
#智慧树刷课

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:08:23 2019

@author: Mario
"""
from selenium import webdriver
import time
import threading
import pyautogui as pag

url = 'https://study.zhihuishu.com/learningNew/videoList?recruitAndCourseId=4b5c505e40524158404a59595d'
number='*******'#手机号码
password='******'#密码
#video_lis = ['video-1717369','video-2086499']
browser=webdriver.Chrome()
browser.get(url)
def login(number,password):
     phone_number=browser.find_element_by_id('lUsername')#通过id定位，手机号码
     pwd=browser.find_element_by_id('lPassword')#密码
     login_btn=browser.find_element_by_class_name('wall-sub-btn')#登陆按钮
     phone_number.send_keys(number)#输入手机号码
     pwd.send_keys(password)#输入密码
     login_btn.click()#点击登陆按钮

def video_begin():
     s = pag.confirm('Are you sure to start ?')#if click ok then return “OK”
     if s == "OK":
         time.sleep(2)
         im1 = pag.screenshot()
         im1.save('my_screenshot0.png')
#在当前屏幕中查找指定图片(图片需要由系统截图功能截取的图)
         coords = pag.locateOnScreen('my_screenshot.png')
#获取定位到的图中间点坐标
         x,y=pag.center(coords)
         print(x,y)
#左击该坐标点
         #y = y+175
         #x,y = 651,876
         pag.rightClick(x,y)
         pag.click(x,y)
         print(x,y)
         pag.rightClick(1012,270)
         pag.click(1012,270)
         #video = browser.find_element_by_id(video_lis[1])
         #video.click()
         pag.click(400,645)
         
#判断是否有答题窗口弹出       
def is_exist():
    while True:
        try:
            browser.switch_to.default_content()
            browser.switch_to.frame('tmDialog_iframe')#答题窗口在另一个frame里面，要切换
            box=browser.find_elements_by_class_name('answerOption')#答题列表
            radio=box[0].find_element_by_tag_name('input')#找到第一个选项
            radio.click()#选择
            browser.switch_to.default_content()
            browser.find_element_by_link_text('关闭').click()#关闭答题窗口
        except:
            browser.switch_to.parent_frame()#没有弹出，切换回本来的frame
            time.sleep(5)

#判断当前视频是否结束
def is_end():
    while True:
        try:
            time.sleep(1)
            video=browser.find_element_by_id('mediaplayer')#定位视频窗口
            #获取当前播放的进度
            current_time=video.find_element_by_class_name('currentTime').get_attribute('textContent')
            #该视频的总时间
            total_time=video.find_element_by_class_name('duration').get_attribute('textContent')
            #time.sleep(5)
            '''
            ct_lst = list(current_time)
            tt_lst = list(total_time)
            ct_int = int(ct_lst[6]+ct_lst[7])+int(ct_lst[3]+ct_lst[3])*60
            tt_int = int(tt_lst[6]+tt_lst[7])+int(tt_lst[3]+tt_lst[3])*60
            p = (ct_int/tt_int)*100
            '''
            time.sleep(5)
            print(current_time,total_time)
            #p = ct_int/tt_int
            #print('\r'+'▇'*(i//2)+str(p)+'%', end='')
            if current_time==total_time:
                print('当前视频播放结束，开始下一节')
                #当前视频播放结束，点击下一节
                #js="document.ElementById('nextBtn').click()"#js脚本
                #browser.execute_script(js)    
                time.sleep(10)#10秒检测一次
                pag.moveTo(109,930)#下一个
                pag.click()
                time.sleep(5)
                pag.moveTo(631,922)#切换1.5倍速
                pag.click(636,767)
                time.sleep(5)
                pag.moveTo(722,928)#切换流畅
                pag.click(725,816)
                time.sleep(10)
        except:
            current_time='00:00'
            total_time='00:01'

if __name__=='__main__':
    login(number,password)
    time.sleep(10)
    video_begin()
    #is_end()
    
    t1=threading.Thread(target=is_exist)
    t2=threading.Thread(target=is_end)
    t2.start()
    time.sleep(3)
    t1.start()
    t2.join()
    t1.join()
