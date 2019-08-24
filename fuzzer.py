# Project: Python fuzzer
# Author: Emanuel Aracena
# Name of file: pfuzz.py
# Date created: August 23, 2019
# Description: A Python3 fuzzer for finding input that crashes C programs in
#              in order to generate test cases.

import signal
import string
import sys
import random
import os
import subprocess
from subprocess import Popen, PIPE

def generate_random_string(size=10, chars=string.printable):
    random_str = ''
    random_str = random_str.join(random.choices(chars, k=size))
    print(random_str)
    return random_str

def main():
    if len(sys.argv) < 3:
        print ("[-] Error -> Proper usage: pfuzz.py FILE NUM_OF_TESTS")
        return
    exec_name = str(sys.argv[1])
    exec_cmd = './' + exec_name
    num_of_tests = int(sys.argv[2])
    
    for i in range(num_of_tests):
        print("\n[Test " + str(i) + "]\n\n")
        process = Popen([exec_cmd], stdin=PIPE, stderr=PIPE)
        gen_str = generate_random_string(random.randint(1,100))
        enc_gen_str = gen_str.encode('utf8')
        stdin, stderr = process.communicate(enc_gen_str)
    
if __name__ == "__main__":
    main()