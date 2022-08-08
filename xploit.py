import ipapi
import os
import time
from colorama import init
init()
from colorama import Fore, Back, Style

os.system("clear")
print(Fore.GREEN, """                                                                                                                     
HHHHHHHHH     HHHHHHHHHXXXXXXX       XXXXXXX                   lllllll                    iiii          tttt          
H:::::::H     H:::::::HX:::::X       X:::::X                    l:::::l                   i::::i      ttt:::t          
H:::::::H     H:::::::HX:::::X       X:::::X                    l:::::l                    iiii       t:::::t          
HH::::::H     H::::::HHX::::::X     X::::::X                    l:::::l                               t:::::t          
  H:::::H     H:::::H  XXX:::::X   X:::::XXXppppp   ppppppppp    l::::l    ooooooooooo   iiiiiiittttttt:::::ttttttt    
  H:::::H     H:::::H     X:::::X X:::::X   p::::ppp:::::::::p   l::::l  oo:::::::::::oo i:::::it:::::::::::::::::t    
  H::::::HHHHH::::::H      X:::::X:::::X    p:::::::::::::::::p  l::::l o:::::::::::::::o i::::it:::::::::::::::::t    
  H:::::::::::::::::H       X:::::::::X     pp::::::ppppp::::::p l::::l o:::::ooooo:::::o i::::itttttt:::::::tttttt    
  H:::::::::::::::::H       X:::::::::X      p:::::p     p:::::p l::::l o::::o     o::::o i::::i      t:::::t          
  H::::::HHHHH::::::H      X:::::X:::::X     p:::::p     p:::::p l::::l o::::o     o::::o i::::i      t:::::t          
  H:::::H     H:::::H     X:::::X X:::::X    p:::::p     p:::::p l::::l o::::o     o::::o i::::i      t:::::t          
  H:::::H     H:::::H  XXX:::::X   X:::::XXX p:::::p    p::::::p l::::l o::::o     o::::o i::::i      t:::::t    tttttt
HH::::::H     H::::::HHX::::::X     X::::::X p:::::ppppp:::::::pl::::::lo:::::ooooo:::::oi::::::i     t::::::tttt:::::t
H:::::::H     H:::::::HX:::::X       X:::::X p::::::::::::::::p l::::::lo:::::::::::::::oi::::::i     tt::::::::::::::t
H:::::::H     H:::::::HX:::::X       X:::::X p::::::::::::::pp  l::::::l oo:::::::::::oo i::::::i       tt:::::::::::tt
HHHHHHHHH     HHHHHHHHHXXXXXXX       XXXXXXX p::::::pppppppp    llllllll   ooooooooooo   iiiiiiii         ttttttttttt  
                                             p:::::p                                                                   
IP SEEKER v1.8                               p:::::p    HAUSA XPLOIT                                                               
                                            p:::::::p                                                                  
 coder: ABDULGEE                            p:::::::p                                                                  
                                            p:::::::p                                                                  
                                            ppppppppp                                
""", Style.RESET_ALL)
print("Enter your target IP ADDREASE below")
ip = input("Enter Target IP: ")
os.system("clear")
time.sleep(3)
print(Fore.GREEN, """
    _ __ ___   __ _(_) __| | ___ ___   __| | ___ _ __ 
   | '_ ` _ \ / _` | |/ _` |/ __/ _ \ / _` |/ _ \ '__|
   | | | | | | (_| | | (_| | (_| (_) | (_| |  __/ |   
   |_| |_| |_|\__,_|_|\__,_|\___\___/ \__,_|\___|_|   
                                                   
 ====================================================================
 **                 WebSite : hausahackers.org                        **
 **                 Channel : hausa hackers/cyberXploit hausa          **
 **                 CODER :   maidcoder/ABDULGEE                        **
 **                 Thank's : ::ABBALO_LUCKY/YAZEED/KBOY_HACKERX/AUTA:: **
 ====================================================================    


""", Style.RESET_ALL)
print(Fore.RED, "make sure you have good internet connection????")
time.sleep(2)
print("loading.......15")
time.sleep(2)
print("loading........35")
time.sleep(2)
print("loading.........54")
time.sleep(2)
print("loading..........68")
time.sleep(2)
print("loading...........79")
time.sleep(2)
print("loading............86")
time.sleep(2)
print("loading.............91")
time.sleep(2)
print("loading..............95")
time.sleep(2)
print("loading...............97")
time.sleep(2)
print("loading.....................", Style.RESET_ALL)
time.sleep(4)
p = location = ipapi.location(ip)
for k, v in location.items():
    print(k, v)
print("thanks for used our tool")