'''
装饰器的应用场景：
日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
性能分析: 可以使用装饰器来测量函数的执行时间。
权限控制: 装饰器可用于限制对某些函数的访问权限。
缓存: 装饰器可用于实现函数结果的缓存，以提高性能。
'''
from typing import Any


def decor_class(func=None):
    def log_class(cls):
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.wrapped = cls(*args, **kwargs)
            def __getattr__(self, name:str)->Any:
                # 拦截目标方法
                if name == func:
                    # 获取原始方法
                    original_method = getattr(self.wrapped, name)
                    # 定义包装函数（真正被调用的）
                    def wrapper(*args, **kwargs):
                        print(f"调用 {cls.__name__}.{func}() 前")
                        result = original_method(*args, **kwargs)
                        print(f"调用 {cls.__name__}.{func}() 后")
                        return result  # 返回原方法结果
                    return wrapper  # 返回包装后的函数
                # 其他属性/方法直接返回
                else:
                    return getattr(self.wrapped, name)
        return Wrapper
    return log_class

@decor_class("display")
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")
    a=5
if __name__ == '__main__':
    obj = MyClass()
    obj.display()
    print(obj.a)


# def decor_class(func):
#     def log_class(cls):
#         """类装饰器，在调用方法前后打印日志"""
#
#         class Wrapper:
#             def __init__(self, *args, **kwargs):
#                 self.wrapped = cls(*args, **kwargs)  # 实例化原始类
#
#             # 转发未定义的属性（包括变量 a、方法 display）
#             def __getattr__(self, name):
#                 return getattr(self.wrapped, name)
#
#         # 动态给 Wrapper 类添加方法，不是挂到 globals
#         def ad_func(self):
#             print(f"调用 {cls.__name__}.{func}() 前")
#             # 调用原始方法
#             getattr(self.wrapped, func)()
#             print(f"调用 {cls.__name__}.{func}() 后")
#
#         #  把动态方法绑定到包装类上
#         setattr(Wrapper, func, ad_func)
#
#         return Wrapper  # 返回包装后的类
#     return log_class
#
# @decor_class("display")
# class MyClass:
#     def display(self):
#         print("这是 MyClass 的 display 方法")
#     a=5
#if __name__ == '__main__':
    # obj = MyClass()
    # obj.display()
    # print(obj.a)