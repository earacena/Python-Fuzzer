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
    if len(sys.argv) < 2:
        print ("[-] Error -> Missing executable name: pfuzz.py FILE")
        return
    exec_name = str(sys.argv[1])
    exec_cmd = './' + exec_name

    
    process = Popen([exec_cmd], stdin=PIPE, stderr=PIPE)
    gen_str = generate_random_string()
    enc_gen_str = gen_str.encode('utf8')
    print(gen_str)
    print(enc_gen_str)
    stdin, stderr = process.communicate(enc_gen_str)
    
if __name__ == "__main__":
    main()
