def my_decorator(func):
    def wrapper(*args, **kwargs):
        """
        这是一个装饰器函数，用于在被装饰的函数执行前后添加额外的功能。
        参数:
            *args: 位置参数，可以接受任意数量的位置参数
            **kwargs: 关键字参数，可以接受任意数量的关键字参数
        """
        print("在原函数之前执行")  # 在原函数执行前打印提示信息
        func(*args, **kwargs)      # 调用被装饰的原始函数，并传递所有参数
        print("在原函数之后执行")  # 在原函数执行后打印提示信息
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")
if __name__ == "__main__":
    greet("Alice")