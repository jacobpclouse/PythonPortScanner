# Port Scanner File - Pg 136

# Import Libraries
import threading
import socket

# Defining Variables
target = '192.168.1.108'

# Defining Functions
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using TCP
    s.settimeout(0.5)#

    # try connecting, print if successful, go on to next if not
    try:
        con = s.connect((target,port))

        print('Port: ', port,' is open.')

        con.close()
    except:
        pass

# Main Program -- Going through 9000 ports to see if they are open
r = 1

for x in range(1,9000):
    t = threading.Thread(target=portscan,kwargs={'port':r})

    r += 1
    t.start()