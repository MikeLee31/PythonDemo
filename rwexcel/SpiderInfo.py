import xlrd
import xlwt
def read_excel():
    name = 'read.xlsx'
    sheetIndex = 0
    Read_col = 7
    Read_row = 0


    # 打开文件
    workBook = xlrd.open_workbook(name);

    Read_col = Read_col
    Read_row = Read_row

    sheet1_content1 = workBook.sheet_by_index(0)
    col = sheet1_content1.col_values(Read_col)
    #print(col)

    with open("out.txt","w") as f:
        for x in range(2, len(col)):
            s = round(col[x])
            print(s)
            f.write(str(s)+" ")


if __name__ == '__main__':
    read_excel();
