import time,os

day = time.strftime("%Y-%M-%d")
headTitle = ["Group,ID,Time"]
headTitle2 = ["Group,ID"]

os.chdir('/var/www/html/Degu')

with open('/home/pi/Documents/Degu/kumiTemporary.txt','w') as kumiTemp:
	kumiTemp.write('1')

myfile = open(day + '.csv','a')
for line in headTitle:
	myfile.write(line+'\n')

myfile2 = open(day + '_Result.csv','a')
for line in headTitle2:
	myfile2.write(line+'\n')

exit()
