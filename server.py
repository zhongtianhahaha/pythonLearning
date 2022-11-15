import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('localhost' , 8888))

s.listen(1)

print('Waiting for connecting...')

while True:

    (conn ,addr) = s.accept()

    filename = 'D:/python/my/client/text.txt'

    print('I want to get the file %s ! ' % filename)

    s.recv(filename.encode('utf-8'))

    str1 = s.recv(1024)

    str2 = str1.decode('utf-8')

    if str2 == 'no':

        print('To get the file %s is failed !' % filename)

    else:

        s.send(b'I am ready !')

        temp = filename.split('/')

        myname = 'my_' + temp[len(temp)-1]

        size = 1024

        with open(myname,'wb') as f:
            
            while True:

                data = s.recv(size)

                f.write(data)

                if len(data) < size:

                    break

    conn.close()

    print('The uploaded file is %s . ' % myname)

sock.close()

                

    
