def TreePrintList(l: list, deep: int):
    for i in l:
        if type(i) is not list:
            pre_print(deep)
            print(i)
        else:
            TreePrintList(i,deep+1)


def pre_print(pre_count: int):
    for i in range(pre_count):
        print("| ", end="")


if __name__ == '__main__':
    li = [
        "tree",
        ["root1", "root2",["root3", "root4"]]
    ]
    TreePrintList(li, 0)
