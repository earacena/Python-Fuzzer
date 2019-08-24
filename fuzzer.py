# Project: Python fuzzer
# Author: Emanuel Aracena
# Name of file: pfuzz.py
# Date created: August 23, 2019
# Description: A Python3 fuzzer for finding input that crashes C programs in
#              in order to generate test cases.

import datetime
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

def generate_random_bytes(size=10):
    return os.urandom(size)

# Return code of subprocess returns as -N if error arises,
# the name of the error can be retrieved by multiply it by one
# and using signal.Signals.(N).name to receive the name
# If no error, return code is 0
def get_return_code_error(return_code):
    return signal.Signals(-1 * return_code).name

def prepare_savefile():
    ts = datetime.datetime.now().isoformat()
    filename = 'fuzzer_test_' + ts
    file = open(filename, 'a')
    file.write("\nTests performed with fuzzer.py ")
    file.write("that resulted in an error/crash.\n")
    file.write("File timestamp: " + ts + "\n\n")
    return file

def store_result(file, encoded, return_code, test_num):    
        file.write("[Test " + str(test_num) + "]\n")
        file.write("Decoded input: \n" + str(encoded) + "\n")
        file.write("Return code: " + str(return_code) + "[" +
                   get_return_code_error(return_code) + "]\n\n")
    
def main():
    if len(sys.argv) < 3:
        print ("[-] Error -> Proper usage: fuzzer.py FILE NUM_OF_TESTS")
        return
    exec_name = str(sys.argv[1])
    exec_cmd = './' + exec_name
    num_of_tests = int(sys.argv[2])
    file = prepare_savefile()

    for i in range(num_of_tests):
        print("\n[Test " + str(i) + "]\n")
        process = Popen([exec_cmd], stdin=PIPE, stderr=PIPE)
        
        # Random string
        #gen_str = generate_random_string(random.randint(1,100))
        #enc_gen_str = gen_str.encode('utf8')

        # Random bytes
        enc_gen_str = generate_random_bytes(random.randint(1,100))
        stdin, stderr = process.communicate(enc_gen_str)
        return_code = process.returncode

        # Return code of subprocess returns as -N if error arises,
        # the name of the error can be retrieved by multiply it by one
        # and using signal.Signals.(N).name to receive the name
        # If no error, return code is 0
        if return_code != 0:
            print("\nReturn code: " + get_return_code_error(return_code)+
                  " [" + str(return_code) + "]")
            store_result(file, enc_gen_str, return_code, i)
        else:
            print("\nReturn code: " + '0')

    file.close()
        
if __name__ == "__main__":
    main()
