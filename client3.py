# -*- coding: utf-8 -*-
"""This module contains a program that behaves as below. 
Client3:
    Reads intergers from the shared-memory and calculate the Mode value of the integers.
"""
import array
import sys
import time
from multiprocessing import shared_memory
from statistics import multimode


def main():
    """Convert bytearray to list from shared memory then get mode"""
    # Access existing shared memory
    shm_name = sys.argv[-1].strip()
    shm = shared_memory.SharedMemory(name=shm_name)
    print('Client3 is ready')
    while shm.buf[0] == 0:
        time.sleep(1)
    data_byte_array = array.array('b', shm.buf[1:shm.buf[0] + 1])
    mode_list = multimode(list(data_byte_array))
    print(f'Mode is {mode_list[0] if len(mode_list) == 1 else mode_list}')

    # Free and release the shared memory block at the very end
    shm.close()
    shm.unlink()


if __name__ == '__main__':
    main()
