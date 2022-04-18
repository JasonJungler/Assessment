# -*- coding: utf-8 -*-
"""This module contains a program that behaves as below. 
Server:
    Accept user keyboard input. The user types integers and separate them by using [Space]. 
    After clicking [Enter], server will write data to each clients via a socket, pipe, or 
    the shared memory, respectively.

Example:
    $ python server.py
"""
import time
from multiprocessing import shared_memory
from socket import AF_INET, SOCK_STREAM, socket
from subprocess import PIPE, Popen

HOST = '127.0.0.1'
PORT = '666'  # int


def parse_input(raw_input):
    """Confirm that all input elements are integers"""
    line = raw_input.strip().split()
    parsed_data = None
    int_list = []
    try:
        for element in line:
            int_list.append(int(element))
        parsed_data = str(int_list)
    except ValueError:
        print(f'{element} is not a valid integer.')

    return parsed_data


def send_by_socket(data):
    """Send input list to client1 via socket"""
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        s.send(data.encode())
        s.recv(1024)


def piping(process_obj, data):
    """Catch stdout from pipeed_process and print result"""
    result = process_obj.communicate(data.encode('utf-8'))[0].decode('utf-8')
    print(result)


def write_to_shm(shm_obj, data):
    """Write data to shared_memory"""
    data = eval(data)
    buffer = shm_obj.buf
    buffer[1:len(data) + 1] = bytearray(data)
    buffer[0] = len(data)


def main():
    """Initialize communication with clients then receive inputs from user"""
    # Allocate shared memory assuming it's a list with 1000 integers
    shm = shared_memory.SharedMemory(create=True, size=8064)

    # Initialize process & communications
    _ = Popen(['python', 'client1.py', HOST, PORT])
    piped_process = Popen(['python', 'client2.py'],
                          stdin=PIPE,
                          stdout=PIPE,
                          bufsize=8064)
    if piped_process.poll() is None:
        print('Client2 is ready')
    _ = Popen(['python', 'client3.py', shm.name])
    time.sleep(0.5)

    # Take input from user
    raw_input = input(
        'Server is ready. '
        'You can type intergers and then click [ENTER].  '
        'Clients will show the mean, median, and mode of the input values.\n')

    parsed_data = parse_input(raw_input)
    if parsed_data is not None:
        send_by_socket(parsed_data)
        piping(piped_process, parsed_data)
        write_to_shm(shm, parsed_data)

    time.sleep(3)
    shm.close()
    shm.unlink


if __name__ == '__main__':
    main()
