import threading
import time

def print_numbers():
    for i in range(5):  # 使用for循环遍历0到4的数字
        time.sleep(1)   # 暂停1秒
        print(i)        # 打印当前数字


if __name__== '__main__':
    thread_s=threading.Thread(target=print_numbers)
    thread_s.start()
    thread_s.join()