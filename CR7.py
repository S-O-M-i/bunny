import os,sys, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests	
bit = platform.architecture()[0]
if bit == '64bit':
    from xXx import menu
    time.sleep(3)
    os.system("xdg-open http://www.apkworldmod.com/")
    menu()
elif bit == '32bit':
    from f32 import _site_view_
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    _site_view_()
 
 
 
