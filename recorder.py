import pyautogui
import time
import keyboard
import threading
import sys


def print_mouse_position():
    while(1):
        x, y = pyautogui.position()
        print(f"Tọa độ chuột hiện tại: X = {x}, Y = {y}")
        time.sleep(1)


# Bắt đầu lắng nghe sự kiện chuột


def pressAndRelease(sequence,sleep_):
    for i in sequence:
        keyboard.press(i)
        time.sleep(0.5)
        keyboard.release(i)
    time.sleep(sleep_)

def pressAndHold(sequence,sleep_):
    for i in sequence:
        keyboard.press(i)
    time.sleep(0.5)
    for i in sequence:    
        keyboard.release(i)
    time.sleep(sleep_)

def click(x,y):
    pyautogui.click(x,y)

def clickSleep(x,y,sleep_):
    pyautogui.click(x,y)
    time.sleep(sleep_)
# Biến cờ để kiểm tra liệu có cần thoát chương trình hay không
exit_flag = False

def listen_for_exit():
    global exit_flag
    while True:
        if keyboard.is_pressed('esc'):  # Kiểm tra phím Esc
            print("Đã nhấn Esc. Thoát chương trình.")
            exit_flag = True  # Cập nhật flag để dừng chương trình
            break
        time.sleep(0.5)  # Giảm tải CPU


def action_captureImageTradigView4K():
    global exit_flag
    if exit_flag:
        return  # Nếu đã nhấn Esc, thoát khỏi hành động này

    pyautogui.click(6301, 54)
    time.sleep(0.5)

    pyautogui.click(6243, 129)
    time.sleep(1)

    pyautogui.moveTo(4610-1880, 300)
    pyautogui.mouseDown()
    pyautogui.moveTo(6126-1880, 300, duration=1.5)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.click(6000-1880, 300)
    time.sleep(4)

def action_TradingViewApplyTemplate_8char_2k_desktopApp():
    global exit_flag
    if exit_flag:
        return  # Nếu đã nhấn Esc, thoát khỏi hành động này
    pyautogui.click(76,220)


    keyboard.press('f5')
    time.sleep(0.5)
    keyboard.release('f5')
    time.sleep(1)

    keyboard.press('enter')
    time.sleep(0.5)
    keyboard.release('enter')
    time.sleep(4)

    pyautogui.click(76,220)
    pyautogui.click(484,54)
    time.sleep(1)
    pyautogui.click(538,176)

    pyautogui.click(76,525)
    pyautogui.click(484,54)
    time.sleep(1)
    pyautogui.click(538,176)

    pyautogui.click(76,855)
    pyautogui.click(484,54)
    time.sleep(1)
    pyautogui.click(538,176)

    pyautogui.click(76,1200)
    pyautogui.click(484,54)
    time.sleep(1)
    pyautogui.click(538,176)

    pyautogui.click(2078,220)
    pyautogui.click(484,54)
    time.sleep(1)
    pyautogui.click(538,176)

    pyautogui.click(2078,525)
    pyautogui.click(484,54)
    time.sleep(1)
    pyautogui.click(538,176)

    pyautogui.click(2078,855)
    pyautogui.click(484,54)
    time.sleep(1)
    pyautogui.click(538,176)

    pyautogui.click(2078,1200)
    pyautogui.click(484,54)
    time.sleep(1)
    pyautogui.click(538,176)
    time.sleep(1)


    keyboard.press('ctrl')
    keyboard.press('s')
    time.sleep(0.5)
    keyboard.release('ctrl')
    keyboard.release('s')
    time.sleep(2)

    keyboard.press('ctrl')
    keyboard.press('w')
    time.sleep(0.5)
    keyboard.release('ctrl')
    keyboard.release('w')
    time.sleep(1)

def action_TradingViewApplyTemplate_8char_2k_firefox():
    global exit_flag
    if exit_flag:
        return  # Nếu đã nhấn Esc, thoát khỏi hành động này
    pyautogui.click(76,220)


    keyboard.press('f5')
    time.sleep(0.5)
    keyboard.release('f5')
    time.sleep(1)

    keyboard.press('enter')
    time.sleep(0.5)
    keyboard.release('enter')
    time.sleep(4)

    pyautogui.click(76,220+70)
    pyautogui.click(840,102)
    time.sleep(1)
    pyautogui.click(890,226)

    pyautogui.click(76,525+70)
    pyautogui.click(840,102)
    time.sleep(1)
    pyautogui.click(890,226)

    pyautogui.click(76,855+70)
    pyautogui.click(840,102)
    time.sleep(1)
    pyautogui.click(890,226)

    pyautogui.click(76,1200+70)
    pyautogui.click(840,102)
    time.sleep(1)
    pyautogui.click(890,226)

    pyautogui.click(2078,220+70)
    pyautogui.click(840,102)
    time.sleep(1)
    pyautogui.click(890,226)

    pyautogui.click(2078,525+70)
    pyautogui.click(840,102)
    time.sleep(1)
    pyautogui.click(890,226)

    pyautogui.click(2078,855+70)
    pyautogui.click(840,102)
    time.sleep(1)
    pyautogui.click(890,226)

    pyautogui.click(2078,1200+70)
    pyautogui.click(840,102)
    time.sleep(1)
    pyautogui.click(890,226)
    time.sleep(1)


    keyboard.press('ctrl')
    keyboard.press('s')
    time.sleep(0.5)
    keyboard.release('ctrl')
    keyboard.release('s')
    time.sleep(2)

    keyboard.press('ctrl')
    keyboard.press('w')
    time.sleep(0.5)
    keyboard.release('ctrl')
    keyboard.release('w')
    time.sleep(1)


def action_TradingViewChaneTF_8char_2k_firefox():
    global exit_flag
    if exit_flag:
        return  # Nếu đã nhấn Esc, thoát khỏi hành động này
    click(76,220)

    pressAndRelease(['f5'],1)
    pressAndRelease(['enter'],4)

    clickSleep(76,220+70,0.1)
    pressAndHold(["alt","r"],0.1)
    pressAndRelease(["1","m","enter"],0.1)

    clickSleep(76,525+70,0.1)
    pressAndHold(["alt","r"],0.1)
    pressAndRelease(["1","w","enter"],0.1)

    clickSleep(76,855+70,0.1)
    pressAndHold(["alt","r"],0.1)
    pressAndRelease(["1","d","enter"],0.1)

    clickSleep(76,1200+70,0.1)
    pressAndHold(["alt","r"],0.1)
    pressAndRelease(["4","h","enter"],0.1)

    clickSleep(2078,1200+70,0.1)
    pressAndHold(["alt","r"],0.1)
    pressAndRelease(["1","h","enter"],0.1)

    clickSleep(2078,855+70,0.1)
    pressAndHold(["alt","r"],0.1)
    pressAndRelease(["1","5","enter"],0.1)

    clickSleep(2078,525+70,0.1)
    pressAndHold(["alt","r"],0.1)
    pressAndRelease(["5","enter"],0.1)

    clickSleep(2078,220+70,0.1)
    pressAndHold(["alt","r"],0.1)
    pressAndRelease(["1","enter"],0.1)

    time.sleep(1)

    pressAndHold(['ctrl','s'],2)
    pressAndHold(['ctrl','w'],1)

def action_TradingView_disableNews_8char_2k_firefox():
    global exit_flag
    if exit_flag:
        return  # Nếu đã nhấn Esc, thoát khỏi hành động này

    clickSleep(76,220,0.5)

    pressAndRelease(['f5'],1)
    pressAndRelease(['enter'],3)

    clickSleep(2387,102,1)
    clickSleep(1064,622,1)
    clickSleep(1202,488,1)
    clickSleep(1367,831,1)
    clickSleep(1542,833,1)
    time.sleep(1)

    pressAndHold(['ctrl','s'],2)

    time.sleep(1)
    pressAndHold(['ctrl','s'],2)
    pressAndHold(['ctrl','w'],1)

range_ = 2
for _ in range(range_):
    # print_mouse_position()
    # action_TradingViewApplyTemplate_8char_2k_desktopApp() #need remote all star of TF
    # action_TradingViewApplyTemplate_8char_2k_firefox()
    # action_TradingViewChaneTF_8char_2k_firefox()
    action_TradingView_disableNews_8char_2k_firefox()
while(1):
    None
# Function to simulate your loop, now respecting the exit condition
def loop(loop, range_):
    global exit_flag
    for _ in range(range_):
        if exit_flag:
            break  # Nếu đã nhấn Esc, thoát khỏi vòng lặp chính

        for _ in range(loop):
            if exit_flag:
                break  # Nếu đã nhấn Esc, thoát khỏi vòng lặp con
            action_captureImageTradigView4K()

        if exit_flag:
            break  # Nếu đã nhấn Esc, thoát khỏi vòng lặp chính

        time.sleep(1)

        keyboard.press('ctrl')
        keyboard.press('tab')
        time.sleep(0.5)
        keyboard.release('ctrl')
        keyboard.release('tab')
        time.sleep(1)

# Start the thread to listen for the 'esc' key press
exit_thread = threading.Thread(target=listen_for_exit)
exit_thread.daemon = True  # Cho phép thread tự động dừng khi chương trình chính dừng
exit_thread.start()

# Run your main loop
try:
    loop(16*24-110-50-7, 1)  # Example usage
except SystemExit:
    sys.exit()


