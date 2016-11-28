import time,os

day = time.strftime("%Y-%M-%d")
headTitle = ["Group,ID,Time"]

os.chdir('/var/www/html/Degu')

with open('/home/pi/Documents/Degu/kumiTemporary.txt','w') as kumiTemp:
	kumiTemp.write('1')

myfile = open(day + '.csv','a')
for line in headTitle:
	myfile.write(line+'n')
	
exit()
