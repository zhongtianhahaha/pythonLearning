from PySide2.QtWidgets import QApplication,
 QMainWindow, QPushButton,
 QTextEdit,QMessageBox
from socket import *
def handleCalc():
    IP = '0.0.0.0'
    PORT = 50000
    BUFLEN = 512
    listenSocket = socket(AF_INET,SOCK_STREAM)
    listenSocket.bind((IP,PORT))
    listenSocket.listen(8)
    textEdit.setPlainText(f'''服务启动成功！！！\n监听在{PORT}端口\n等待客户连接......''')
    dataSocket, addr = listenSocket.accept()
    textEdit.setPlainText(f'''接受一个客户端连接，{addr}''')
    while True:
         recved = dataSocket.recv(BUFLEN)
         if not recved:
            break
         info=recved.decode()
         textEdit.setPlainText(f'''收到对方信息{info}''')
       dataSocket.send(f'服务端收到了信息{info}'.encode())
       dataSocket.close()
       listenSocket.close()app = QApplication([])
       window = QMainWindow()
       window.resize(500, 400)
       window.move(300, 310)
       window.setWindowTitle('Message Server')
       textEdit = QTextEdit(window)
       textEdit.move(10,25)textEdit.resize(300,350)
       button = QPushButton('Start', window)
       button.move(380,80)
       window.show()
       button.clicked.connect(handleCalc)
       app.exec_()
