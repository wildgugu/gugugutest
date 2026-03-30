class Timer:
    def __enter__(self):
    # 导入time模块，用于时间计算
        import time
    # 记录当前时间作为开始时间，并存储在self.start中
        self.start = time.time()
    # 返回self对象，支持上下文管理协议
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):#类型，值，追踪信息
    # 导入time模块，用于获取时间
        import time
    # 记录结束时间
        self.end = time.time()
    # 打印耗时信息，保留两位小数
        print(f"耗时: {self.end - self.start:.2f}秒")
    # 返回False，表示不异常处理，如果有异常会继续抛出，并且释放资源
        return False
if __name__ == '__main__':
    # 使用示例
    with Timer() as t:
        # 执行一些耗时操作
        sum(range(1000000))
        # 上下文管理器会自动在with代码块结束时调用__exit__方法
    #因为没有异常，所以上文的return false返回空不会触发异常
    print('a')