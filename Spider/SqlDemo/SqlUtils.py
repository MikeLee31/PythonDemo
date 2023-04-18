import pymysql

from Utils.ExcelUtils import  save_to_excel


class Videos(object):

    def __init__(self, v_id: int, a_id: int, v_code: str, name: str, a_name: str, date: str, img_url: str) -> object:
        self.v_id = v_id
        self.a_id = a_id
        self.v_code = v_code
        self.name = name
        self.a_name = a_name
        self.date = date
        self.img_url = img_url

    def __str__(self):
        return f'{self.v_code}-{self.name}-{self.a_name}'

    def get_insert_sql(self):
        print(self.__str__())
        s = "insert into videos( v_code,a_id,name,date,img_url ) values ('{}',{},'{}','{}','{}')".format(
            self.v_code, self.a_id, self.name, self.date, self.img_url
        )
        print(s)
        return s


# 打开数据库连接
def get_db_connect():
    db = pymysql.connect(host='175.24.163.181',
                         user='root',
                         password='Lh113115',
                         database='javbus',
                         port=3306,
                         charset='utf8mb4')
    return db


def insert(db, sql):
    cur = db.cursor()
    try:
        row_change = cur.execute(sql)
        # 提交
        db.commit()
        print(f'插入成功,修改行{row_change}')
    except Exception as e:
        print(e)
        print('数据库插入操作错误回滚')
        db.rollback()


def query(db, sql):
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句
        name_fileds = cur.description
        data = []
        field = []
        for i in range(len(name_fileds)):
            field.append(name_fileds[i][0])
        print(field)
        data.append(field)
        results = cur.fetchall()  # 获取查询的所有记录
        # 遍历结果
        for row in results:
            data.append(list(row))
        save_to_excel(data, 'test', 'show')
    except Exception as e:
        raise e


if __name__ == '__main__':
    v = Videos(2, 2, 'ss', '213', '123', '2022-02-13', 'https://1615.com')
    insert(db=get_db_connect(), sql=v.get_insert_sql())
