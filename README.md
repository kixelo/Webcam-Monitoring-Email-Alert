# Webcam Monitoring Email Alert

With this script you can detect any movement while running your webcam.

## IDE application that I used for coding part
```
PyCharm
```

## Build Setup, required to install dependencies
```
pip install opencv-python
pip install send_email
pip install glob2
```

## Build Setup, needed standard Python modules
```
import time
import os
from threading import Thread
```

## How to run the script
```
1. download all needed files into one folder
2. locate the folder path, windows user type command in CMD: cd 'your_folder_path'
3. then in CMD install ALL needed dependencies by command: pip install secure-smtplib etc...
4. before running the script, make sure that your Computer/ Laptop has WEBCAM, then run the app by typing command in CMD: python main.py
5. the script will switch on your webcam and if any movements occur, then make picture of moving object and send you an email with pic attachment.
```

## App image
<img src="https://github.com/kixelo/Webcam-Monitoring-Email-Alert/blob/master/webcam_movement_alert.PNG" />
