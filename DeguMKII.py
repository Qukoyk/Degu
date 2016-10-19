#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import文
import RPi.GPIO as GPIO
from time import sleep
import time,os,pickle

#ポート設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		
#初期化数据
os.chdir('/home/pi/Documents/Degu/Data')
trail = 1
time0 = time.time()														#始まりの時間
time1 = time.time()														
time2 = time.time()														#前回反応の時間点
jiKoku = []
day = time.strftime("%Y-%m-%d")
headTitle = ["Group,ID,Time"]

#データ保存先を指定
mydata = []
mydata2 = []
myfile = open(day + '.csv','a')
kumiTemp = open('/home/pi/Documents/Degu/kumiTemporary.txt','r+')
for line in headTitle:
	myfile.write(line+'\n')
kumi = kumiTemp.read()
kumiTemp.close()
print ("第",kumi,"組、",str((time.strftime("%H:%M:%S", time.localtime()))),"から始動！")	

#メインプログラム	
try:
	while True:															#時間統制部分
		if time1-time0 < 299:											#5分間300秒があるが、一秒の整備時間の原因で引く
			time1 = time.time()
			
			if GPIO.input(24) == GPIO.LOW:
				GPIO.output(25, GPIO.HIGH)
				time1 = time.time()										#反応瞬間の時間
				print ("第",kumi,"組")												
				print ("    回数 ",trail)
				print ("    時刻 ",time.strftime("%H:%M:%S", time.localtime()))
				print ("時間間隔 ",round((time1-time2),1),"","秒"	,'\n')		#反応間かかった時間、小数点後1桁保留
				jiKoku.append(time.strftime("%H:%M:%S", time.localtime()))
				mydata = [str(kumi),',',str(trail),',',str((time.strftime("%H:%M:%S", time.localtime()))),'\n',]
				trail = trail+1
				time2 = time.time()
				for line in mydata:
					myfile.write(line)
				while GPIO.input(24) == GPIO.LOW:						#「保護わく」
					sleep(0.01)											#同じ

			else:
				GPIO.output(25, GPIO.LOW)
				time1 = time.time()
				
			sleep(0.01)	
			
		else:															#一日に達すれば命令
			print("第",str(kumi),"組　",str((time.strftime("%H:%M:%S", time.localtime()))),"でブロック終了")
			kumiTemp = open('/home/pi/Documents/Degu/kumiTemporary.txt','w')
			kumi = int(kumi)+1
			for line in str(kumi):
				kumiTemp.write(line)										
			myfile.close()												#ファイルを閉める
			kumiTemp.close()
			GPIO.cleanup()												#ポート釈放
			exit()
		sleep(0.01)														#サーキュレーション尺度
			
			
		
except KeyboardInterrupt:												#サーキュレーション終了
			pass

#クロスファイル	
print("プログラム中断")
kumi = kumiTemp.read()
kumiTemp = open('/home/pi/Documents/Degu/kumiTemporary.txt','w')
kumi = int(kumi)+1
for line in str(kumi):
	kumiTemp.write(line)
myfile.close()
kumiTemp.close()

#ポート釈放			
GPIO.cleanup()
