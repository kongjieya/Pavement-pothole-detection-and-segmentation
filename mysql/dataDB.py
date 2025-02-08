import pymysql
# 连接数据库的函数
def connect_to_database():
    try:
        # 连接数据库
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='yolo'
        )

        # 获取游标
        cursor = connection.cursor(pymysql.cursors.DictCursor)  # 使用 DictCursor 返回字典格式的结果

        # 返回连接和游标对象，以便在其他地方使用
        return connection, cursor

    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")


connection, cursor = connect_to_database()

def selectDB(sql):
    # # 打开数据库连接
    # db = connectDB()
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    results = cursor.fetchall()
    # db.close()
    return results




def insertDB(sql):
    try:
        result = cursor.execute(sql)
        connection.commit()
        return result  # 返回受影响的行数
    except Exception as e:
        connection.rollback()
        print(f"InsertDB Error: {e}")
        return None



def delDB(sql_list):
    try:
        for sql in sql_list:
            cursor.execute(sql)
            connection.commit()

        return "success"
    except Exception as e:
        connection.rollback()
        return "failure"



def closeDB():
    try:
        connection.close()
    except Exception as e:
        print("db:", e)


class SI:
    USER = None
    mainWin = None
    loginWin = None
    Ui_registerWindow = None
    projectPath = None
    AIWindow = None

