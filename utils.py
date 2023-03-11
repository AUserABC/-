import time
import pymysql

def get_conn():
    """
        :return 连接，游标
    """
    conn = pymysql.connect(host = "127.0.0.1",
                          user="root",
                          password="abc123",
                          db="cov",
                          charset="utf8")
    cursor = conn.cursor()
    return conn,cursor


def close_conn(conn,cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询结果((),())的形式
    """
    conn,cursor = get_conn()
    cursor.execute(sql,args)
    res=cursor.fetchall()
    close_conn(conn,cursor)
    return res

def get_c1_data():
    """
    返回大屏div id=c1所需要的数据
    :return:
    """
    sql = "select sum(confirm),(select suspect from history order by ds desc limit 1),sum(heal),sum(dead) from details where update_time = (select update_time from details order by update_time limit 1)"
    res = query(sql)
    return res[0]


def get_c2_data():
    sql = "select province,sum(confirm) from details where update_time=(select update_time from details order by update_time desc limit 1) group by province"
    res = query(sql)
    return res

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

def get_l1_data():
    sql = "select ds,confirm,suspect,heal,dead from history limit 53"
    res = query(sql)
    return res

def get_l2_data():
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res

def get_l21_data():
    sql = 'select content from mhotword order by  id asc limit 10'
    res = query(sql)
    return res

def get_r1_data():
    sql='SELECT city,confirm FROM (select city,confirm ' \
        'from details where update_time=(select update_time from details ' \
        'order by update_time desc limit 1) and province not in ("北京","上海","天津","重庆","台湾","香港") ' \
        'union all select province as city,sum(confirm) as confirm from details where update_time=(select update_time from details order by update_time desc limit 1) ' \
        'and province in ("北京","上海","天津","重庆") group by province) as a ORDER BY confirm DESC LIMIT 5'
    res = query(sql)
    return res

def get_r2_data():
    """
    :return:
    """
    sql = 'select dt from hotsearch order by id desc  limit 1'
    dt = query(sql)
    sql='select content from hotsearch where dt = %s order by  id asc limit 13'
    res = query(sql,dt[0])
    return res

if __name__ == "__main__":
    # print(get_c1_data())
    # print(get_l1_data())
    # print(get_l2_data())
    print(get_r2_data())