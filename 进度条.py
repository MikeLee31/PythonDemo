import sys
import time


class ProgressBar:
    def __init__(self, output="进度", total=0, count=0):

        self.total = total
        self.count = count
        self.output = output
        print("--------------------")

    def move(self):
        if self.count < self.total:
            self.count += 1
            print('\r', end="")
            print("%s-%3d/%3d-%4.2f%%" % (self.output, self.count, self.total, self.count / self.total * 100), end="")
            sys.stdout.flush()
            if self.count == self.total:
                print()
                print("\n" + self.output + "结束")
                print("--------------------")
        else:
            print("--------------------")
            print("已完成,多余调用")
            print("--------------------")


if __name__ == '__main__':

    progressbar = ProgressBar(output="图片生成", total=100)
    for i in range(1, 100):
        # print('\r', end="")
        # print("进度: {}% ".format(i), end="")
        # sys.stdout.flush()
        progressbar.move()
        time.sleep(0.05)
