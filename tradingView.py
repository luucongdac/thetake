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
# print_mouse_position()

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


def action_TradingViewApplyTemplate_8char_2k():
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
    pyautogui.click(845,54)
    time.sleep(1)
    pyautogui.click(932,176)

    pyautogui.click(76,525)
    pyautogui.click(845,54)
    time.sleep(1)
    pyautogui.click(932,176)

    pyautogui.click(76,855)
    pyautogui.click(845,54)
    time.sleep(1)
    pyautogui.click(932,176)

    pyautogui.click(76,1200)
    pyautogui.click(845,54)
    time.sleep(1)
    pyautogui.click(932,176)

    pyautogui.click(2078,220)
    pyautogui.click(845,54)
    time.sleep(1)
    pyautogui.click(932,176)

    pyautogui.click(2078,525)
    pyautogui.click(845,54)
    time.sleep(1)
    pyautogui.click(932,176)

    pyautogui.click(2078,855)
    pyautogui.click(845,54)
    time.sleep(1)
    pyautogui.click(932,176)

    pyautogui.click(2078,1200)
    pyautogui.click(845,54)
    time.sleep(1)
    pyautogui.click(932,176)
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



range_ = 2
for _ in range(range_):
    action_TradingViewApplyTemplate_8char_2k()
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
