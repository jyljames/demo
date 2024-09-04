import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     passwd='root',
                     db='houseurls',
                     charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO houseurl(urls)
                 VALUES ('hjhuihkj')"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print("插入成功")
except:
    # 如果发生错误则回滚
    print("插入失败")
    db.rollback()

# 关闭数据库连接
db.close()