import os


def exec_cmd(cmd_str):
    # 使用popen
    import os
    res = os.popen(cmd_str)
    # 获得控制台输出
    output_str = res.read()
    print(output_str)


if __name__ == '__main__':
    exec_cmd('ipconfig')
