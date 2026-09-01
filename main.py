import os
import pytest

#pytest.main在 Python 代码内部启动 pytest，等价于在终端敲 pytest 命令**。全部用例跑完之后，才回到 python 脚本，继续往下执行后面代码
#-s表示输出不捕获，即可输出用例的打印内容，-v表示详细输出
pytest.main(["-s","-v"])
#调用操作系统的终端命令，就相当于在 cmd/PowerShell 手动敲一行命令回车执行**。
os.system('allure generate -o report -c temps')