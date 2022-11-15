import socket

import os

def sendfile(con):
    
    str1 = con.recv(1024)
    
    filename = str1.decode('utf-8')
    
    print('The sever want my file to server:',filename)
    
    if os.path.exists(filename):
        
        print('I have %s, begin to upload!' % filename)
        
        con.send(b'yes')
        
        con.recv(1024)
        
        size = 1024
        
        with open(filename,'rb') as f:
            
            while True:

               data = f.read(size)

               con.send(data)

               if len(data) < size:

                   break

                print('%s is uploaded successfully!' % filename)

    else:
        
        print('Sorry , I have no %s' % filename)

        con.send(b'no')

    con.sendfile(con)

    con.close

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect(('localhost' , 8888))
