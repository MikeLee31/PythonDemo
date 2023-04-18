import pymysql


# 打开数据库连接
def get_db_connect(dbname='android'):
    db = pymysql.connect(host='175.24.163.181',
                         user='root',
                         password='Lh113115',
                         database=dbname,
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
        data = []
        results = cur.fetchall()  # 获取查询的所有记录
        # 遍历结果
        for row in results:
            data.append(list(row))
        return data
    except Exception as e:
        raise e


def query_name_fileds(db, sql):
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句
        name_fileds = cur.description
        field = []
        for i in range(len(name_fileds)):
            field.append(name_fileds[i][0])
        return field
    except Exception as e:
        raise e
