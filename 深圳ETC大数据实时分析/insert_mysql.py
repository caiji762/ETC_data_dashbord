# @skyclear
# -*-coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="cumt*08192859",
                           db="ETC",
                           charset="utf8")
# 创建游标
cursor = conn.cursor()# 执行完毕返回的结果集默认以元组显示
with open('allData.csv','r') as f:
    lines=f.readlines()
    for line in lines[1:]:
        line=line.split(',')

        line[-1]=line[-1].strip('\n')
        for i in range(1,len(line)):
            if line[i]=='NULL' or line[i]=="未知":
                line[i]=None
            # line[i]=f"\'{line[i]}\'"
        values=line[:-1]
        # values = ','.join(line[:-1])
        # print(values)
        sql=f"insert into etc_data(XH,CKSJ,CX,SFZRKMC,RKSJ,BZ,SFZCKMC,CP) values(%s,%s,%s,%s,%s,%s,%s,%s);";
        cursor.execute(sql,values)
        print(line[0])
        # if line[0]=='5000':
        #     break
        # res=cursor.fetchall()
        # res=' '.join(list(res))
        # print(res)
        # print(sql+' '+res)
    conn.commit()
    cursor.close()
    conn.close()
