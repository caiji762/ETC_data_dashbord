import time
import pymysql
import random
def get_time():

    time_str =  time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="192.168.60.134",
                           user="root",
                           password="hadoop",
                           db="TESTDB",
                           port=8066)
    # 创建游标
    cursor = conn.cursor()# 执行完毕返回的结果集默认以元组显示
    return conn, cursor

def close_conn(conn, cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_c1_data():
    res={}
    sql='select count(*) from etc_data;'
    num=query(sql)
    res['num']=num[0][0]
    res['time']=int(num[0][0])//50
    sql='select count(*) from etc_data where locate("客",CX)>0;'
    passenger=query(sql)
    res['passenger']=passenger
    sql = 'select count(*) from etc_data where locate("货",CX)>0;'
    truck = query(sql)
    res['truck']=truck
    return res


def get_c2_data():
    """
    :return:  返回各省数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    # sql = "select province,sum(confirm) from details " \
    #       "where update_time=(select update_time from details " \
    #       "order by update_time desc limit 1) " \
    #       "group by province"
    sql = "select SFZRKMC,count(*)" \
          "from etc_data group by SFZRKMC"
    res = query(sql)
    return res
    # re=[]
    # for i in res:
    #     re.append((dic[i[0]],i[1]))
    # return re

def get_l1_data():
    sql ="select count(*) ,SFZCKMC ,hour(CKSJ) as CKSJ_h,minute(CKSJ) as CKSJ_m  from etc_data group by CKSJ_h,CKSJ_m,SFZCKMC order by CKSJ_h, CKSJ_m;"
    # sql="select count(*) from etc_data"
    res=query(sql)
    re=[]
    r=[]

    for i in res:
        re.append({'station_name':i[1],'station_num':i[0],'time':f'12/22/{i[2]}:{i[3]}'})

    name=['广东水朗D站','广东罗田主线站','松山湖南']
    data=[re[-3].get('station_num'),re[-2].get('station_num'),re[-1].get('station_num')]
    time=re[-3].get('time')

    return ({'name':name,'data':data,'time':time})
def get_l2_data():
    sql = "select count(*),CKSJ,right(CX,3) as CX_3 from etc_data group by CKSJ,CX_3 order by CKSJ desc limit 24;"
    mul=12
    res=query(sql)
    time=[]
    num_p=[0]*mul
    num_t=[0]*mul
    num=[]
    for i in range(len(res)):
        if res[i][2]=="(客)":
            time.append(str(res[i][1].day)+'/'+str(res[i][1].hour)+':'+str(res[i][1].minute))
            num_p[i//2]=res[i][0]
        if res[i][2]=='(货)':
            num_t[i//2]=res[i][0]
    for i in range(len(num_t)):
        num.append(num_p[i]+num_t[i])
    time=list(reversed(time))
    num = list(reversed(num))
    num_p = list(reversed(num_p))
    num_t = list(reversed(num_t))
    return {"time":time,"num":num,"num_p":num_p,"num_t":num_t}

def get_r1_data():

    sql='select count(*) as num ,left(CP,2) as CP_2 ,right(CX,3) as CX_3 from etc_data group by CP_2 ,CX_3 order by  num desc '
    re = query(sql)
    name=[]
    values_p=[]
    values_t=[]
    for i in range(len(re)):
        if re[i][2]=='(客)' and len(values_p)<5:
            name.append(re[i][1])
            values_p.append(re[i][0])
            values_t.append(re[i+1][0])
    name=list(reversed(name))
    values_p=list(reversed(values_p))
    values_t = list(reversed(values_t))
    return {'name':name,'values_p':values_p,"values_t":values_t}

def get_r2_data():
    """
    :return:  返回最近的20条热搜
    """
    sql = "select CX,count(*) from etc_data group by CX"
    res = query(sql)
    re=[]
    for i in res:
        re.append({'name':i[0],'value':i[1]})
    return re


	
if __name__ == "__main__":
   print(get_l2_data())