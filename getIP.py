import socket
import fcntl
import struct


def get_ip_address(ifname):
    #建立套接字（可以通过这个东西，实现主机内主机间的进程通信），面向网络且无连接
    #简写，两个都是默认参数：s = socket.socket()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    return socket.inet_ntoa(
        # 0x8915：执行的操作。该操作返回的结构体含有ipv4地址，输入也需要结构体，所以将网卡信息放到ifreq结构体中（第三个参数）。
        #输出结果也为ifreq结构体
        #ifname[:15]网卡长度16字节
        #文件描述符，第一参数
        fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))
        [20:24])

#网卡名字eth0  eth0:1 子网卡。
get_ip_address('eth0')

def test():
    return  null


