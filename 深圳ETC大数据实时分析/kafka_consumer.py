import json
import pymysql
from kafka import KafkaConsumer
import re
import time

consumer = KafkaConsumer('test1',
                         bootstrap_servers=['192.168.60.134:9092'],auto_offset_reset='latest', enable_auto_commit=False)
for message in consumer:
     res=message.value.decode()
     res=re.findall('{"XH":(.+?),"CKSJ":(.+?),"CX":(.+?),"SFZRKMC":(.+?),"RKSJ":(.+?),"BZ":(.+?),"SFZCKMC":(.+?),"CP":(.+?)}',res)
     att=['XH','CKSJ','CX','SFZRKMC','RKSJ','BZ','SFZCKMC','CP']
     dic=dict(zip(att,res[0]))
     conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           passwd="hadoop",
                           port=8066,
                           db="TESTDB")
     cursor = conn.cursor()#  创建游标,执行完毕返回的结果集默认以元组显示
     into = "INSERT INTO etc_data(XH,CKSJ,CX,SFZRKMC,RKSJ,BZ,SFZCKMC,CP) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
     values = (dic['XH'],dic['CKSJ'],dic['CX'],dic['SFZRKMC'],dic['RKSJ'],dic['BZ'],dic['SFZCKMC'],dic['CP'])
     cursor.execute(into, values)
     conn.commit()
     conn.close()
     time.sleep(1)


