# Degu
A Python script to count the number of turns that degu had run.
  
## INTRO  
There's a degu in the lab.   
My professor used a PC with Windows XP to count the number of turns which degu had run.
Therefore, that PC seems had some problem and can't save the data for long time.
So he asked me that if I could build a budget to replace that PC.
  
## DETAILS  
I use Python 3 in a Raspberry Pi 3 to solve this problem.  
The script will count the turns for every 4'59". When degu run for half turn, the LED on the mother board will be lighted. The number of group, turns, time, and the time after last turn will show on the terminal at the same time. At the begining of each group, it'll shows "Groups Started in hh:mm:ss" in Japanese on the terminal, and "Group Ended in hh:mm:ss". Also, data will be saved in a directory in .csv which conclude Group, ID and Time.   
Cause it is Raspberry Pi, cron is a easy way to controll the automatic-running. You can see it in "corn.txt".    
Also, you can use actogram.py to analysis Degu's biological rhythms. It is based on matplotlib, a Python 2D plotting library , and could draw actograms of degu.    
![Degu Actogram](http://i.imgur.com/3EfTsK7.png "Actogram of Degu during 2016.11-2016.12")   

  
## STRUCTURE  
* **DeguMKII.py**  
  the main script.
* kumiReset.py  
  a script to reset the kumiTemporary in to 1 at 00:00 everyday. (Also contronlled by cron)  
* cron.txt  
  cronjob commands
* *actogram.py*    
  a script to analysis the biological rhythms of degu and creat actograms.
    
    
Qukoyk  
  <g160058@hiroshima-u.ac.jp>
