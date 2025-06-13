from pathlib import Path

path = Path("aini_2.txt")
# path.write_text("hello world")####错误实例，不小心创造了一个错误实例
try:
    print(path.read_text())
except  FileNotFoundError:
    print("没有找到文件")

###这是一个列表错误的、异常except  FileNotFoundError:
###    print("没有找到文件")


###except zerodivisionerror  ZeroDivisionError  除数不为0的异常