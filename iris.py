import time

import pyautogui
def click_button(button,offset = (0,0),refresh = False):
    pos = pyautogui.position()
    try:
        left, top, width, height = pyautogui.locateOnScreen(button,confidence = 0.8) # 根据图片定位按钮位置
        x = left + width / 2 # 计算中心点的x坐标
        y = top + height / 2 # 计算中心点的y坐标
        if button == r".\lib\5a.png":
            x = x + 991
            y = y + 14
        if button == r".\lib\a6a.png":
            print(11111)
            print(x,y)
            x = x +674
            y = y +46
            print(x,y)
        if button == r".\lib\5.png":
            x = x +1385
            y = y+26
        x = x + offset[0]
        y = y + offset[1]
        pyautogui.moveTo(x, y)
        time.sleep(0.2)
        pyautogui.click(x, y) # 点击一次左键
        print(1)
        pyautogui.click(*pos)  # 点击一次左键
        return True
    except:
        return False
        pass

def critical_click_button(button):
    try:
        left, top, width, height = pyautogui.locateOnScreen(button,confidence = 0.95) # 根据图片定位按钮位置
        x = left + width / 2 # 计算中心点的x坐标
        y = top + height / 2 # 计算中心点的y坐标
        if button == r".\lib\5.png":
            x = x +1385
            y = y+26
        time.sleep(0.2)
        pyautogui.click(x, y) # 点击一次左键
        print(1)
        return True
    except:
        return False
        pass
def quest(small = False,abyss = False,refresh = False):
    if small:
        while True:
            print(1)
            if abyss and not click_button('11a.png',refresh = refresh):
                click_button(r'.\lib\1a.png',refresh = refresh)
            if not abyss:
                click_button(r'.\lib\1a.png',refresh = refresh)
            click_button(r'.\lib\2a.png',refresh = refresh)
            click_button(r'.\lib\3a.png',refresh = refresh)

            click_button(r'.\lib\5a.png',refresh = refresh)
            click_button(r'.\lib\4a.png',refresh = refresh)
            time.sleep(1)
            # if click_button('6a.png',(676,41)):
            #     time.sleep(1)
            #     click_button("7a.png")
            #     time.sleep(1)
            #     click_button("7a.png")
            # if click_button("8a.png"):
            #     click_button("1b.png")
            #     time.sleep(10)
            #     while not click_button("2b.png"):
            #         pass
            #     while not click_button("3b.png"):
            #         pass

    while True:
        if abyss and not click_button(r'.\lib\0.png',refresh = refresh):
            click_button(r'.\lib\1.png',refresh = refresh)
        click_button(r'.\lib\2.png',refresh = refresh)
        click_button(r'.\lib\5.png',refresh = refresh)
        click_button(r'.\lib\3.png',refresh = refresh)
        click_button(r'.\lib\4.png',refresh = refresh)
        click_button(r'.\lib\6.png',refresh = refresh)
        time.sleep(1)
def visit():
    while True:
        if not critical_click_button(r'.\lib\8.png'):

            click_button(r'.\lib\10.png')
        critical_click_button(r'.\lib\7.png')
        critical_click_button(r'.\lib\8.png')
        critical_click_button(r'.\lib\9.png')
        time.sleep(1)

def campus():
    while True:
        click_button(r".\lib\5a.png")
        if not click_button(r".\lib\a6a.png"):
            click_button(r".\lib\1a.png")
        else:
            time.sleep(1)
            click_button(r".\lib\a7a.png")
            time.sleep(1)
            click_button(r".\lib\a7a.png")
        click_button(r".\lib\2a.png")
        if click_button(r".\lib\a1a.png"):
            click_button(r".\lib\a2a.png")
        if click_button(r".\lib\a3a.png"):
            click_button(r".\lib\a4a.png")
        click_button(r'.\lib\a5a.png')

def fish():
    while True:
        critical_click_button(r'.\lib\0c.png')
        time.sleep(1)

def main():
    # visit()
    # quest(small=True,abyss = True,refresh = True)
    # campus()
    fish()
    #

if __name__ == '__main__':
    main()