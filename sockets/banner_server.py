#!/usr/bin/env python

import socket

def main():
    ports = [21,23,22,80,8080]
    ip = "192.168.56.101"
    for port in ports:
        print("[*] Testing port %s at IP %s") % (port, ip)
        try:
            #socket.setdefaulttimeout(1)
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect_ex((ip,port))
            output = s.recv(1024)
            print("[+] The banner: %s for IP: %s at Port: %s") % (output,ip,port)
        except:
            print("[-] Failed to Connect to %s:%s") % (ip, port)
        finally:
            s.close()

if __name__ == "__main__":
    main()
