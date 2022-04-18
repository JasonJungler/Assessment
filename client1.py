# -*- coding: utf-8 -*-
"""This module contains a program that behaves as below. 
Client1:
    Reads intergers from the socket and calculate the Mean value of the integers.
"""
import sys
from socket import AF_INET, SOCK_STREAM, socket
from statistics import mean


def main():
    """Read data via socket and get mean"""
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((sys.argv[-2], int(sys.argv[-1])))
        print('Client1 is ready')
        s.listen(1)
        conn, _ = s.accept()
        data = conn.recv(1024).decode()
        print(f'Mean is {mean(eval(data))}')
        conn.send('done'.encode())


if __name__ == '__main__':
    main()
