#coding:utf-8
from Tkinter import *
import traceback
import  socket

class SocketHandler:
    isconnected = False
    IP = ""
    PORT = 0
    address = (IP,PORT)
    sockets = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def __init__(self,ip,port):
        self.IP = ip
        self.PORT = port
        self.address = (self.IP,self.PORT)

    def disconnect(self):
        self.sockets.close()

    def sendMsg(self,msg):
        if not msg:
            pass
        self.sockets.sendto(msg,self.address)


root = Tk()
root.title("秒针空间-UDP控制")
root.geometry('460x380')
root.resizable(0, 0)
header = Frame(height=30,width=460,bg='green')
Label(header,text="IoT v1.0",font=('Arial',20)).pack(side=TOP)
header.pack()

banner = Frame(height=40,width=460)
#left
frm_L = Frame(banner)
Label(frm_L,text="IP:",font=("Arial",15)).pack(side=LEFT)
ip = StringVar()
Entry(frm_L,textvariable=ip).pack(side=TOP)
frm_L.pack(side=LEFT)
#right
frm_R = Frame(banner)
Label(frm_R,text="Port:",font=("Arial",15)).pack(side=LEFT)
port = StringVar()
Entry(frm_R,textvariable=port).pack(side=TOP)
frm_R.pack(side=RIGHT)
banner.pack()

state = 0

#处理函数
def connect():
    if ip.get() != '' and port.get() != '':
        IP = ip.get()
        PORT = port.get()
        ips = IP.split('.')
        IPS = []
        for i in ips:
            i = int(i)
            if i >= 255:
                print "请输入小于255的字段"
            else:
                i = str(i)
                IPS.append(i)
        IP = ".".join(IPS)
        s = SocketHandler(IP,int(PORT))
        show("已打开连接")
        global state
        state = s
    else:
        show("请补全信息")
def disconnect():
    print "closed"
    state.disconnect()
    show("断开连接")

def on_led():
    msg = "on"
    show(msg)
    show_led(msg)
    state.sendMsg(msg)

def off_led():
    msg = "off"
    show_led(msg)
    show(msg)
    state.sendMsg(msg)

def sendCMD():
    msg = cmd_input.get()
    show(msg)
    state.sendMsg(msg)

#button 设置
connect_btn = Button(root,text="打开连接",command=connect)
connect_btn.place(x=80,y=66,width=80,height=24)
disconnect_btn = Button(root,text="断开连接",command=disconnect)
disconnect_btn.place(x=240,y=66,width=80,height=24)

#命令行
open_led_btn = Button(root,text="开灯",command=on_led)
open_led_btn.place(x=80,y=110,width=80,height=24)
close_led_btn = Button(root,text="关灯",command=off_led)
close_led_btn.place(x=240,y=110,width=80,height=24)
#显示信息

content = Label(root, text="请先连接到udp服务器", bg="grey", anchor='center')
content.place(x=0, y=160, width=460, height=34)


#第三方信息命令
Commads = Label(root,text="命令：",font=('Arial',20))
Commads.place(x=68,y=260)
cmd_input = StringVar()
CMD_INPUT = Entry(root,textvariable=cmd_input)
CMD_INPUT.place(x=160,y=270)
cmd_btn = Button(root,text="发送",command=sendCMD)
cmd_btn.place(y=260,x=320)

def show(msg):
    content = Label(root,text=msg,bg="grey",anchor='center')
    content.place(x=0, y=160, width=460,height=34)

def show_led(msg):
    if msg == "on":
        closestate = Label(root,bg="#F0F0F0")
        closestate.place(x=210, y=110, width=24, height=24)
        openstate = Label(root,bg="green")
        openstate.place(x=50, y=110, width=24, height=24)
    elif msg == "off":
        openstate = Label(root,bg="#F0F0F0")
        openstate.place(x=50, y=110, width=24, height=24)
        closestate = Label(root,bg="black")
        closestate.place(x=210, y=110, width=24, height=24)

footer = Label(root,text="Designed by miaozhen - www.miaozhen360.com",font=('Arial',10))
footer.place(x=100,y=340)

try :
    root.mainloop()
except Exception as e:
    traceback.print_exc(file=open('info.log',''))
