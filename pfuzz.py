# Project: Python fuzzer
# Author: Emanuel Aracena
# Name of file: pfuzz.py
# Date created: August 23, 2019
# Description: A Python3 fuzzer for finding input that crashes C programs in
#              in order to generate test cases.

import subprocess
from subprocess import Popen, PIPE

process = Popen(['./a.out'], stdin=PIPE, stderr=PIPE)
stdin, stderr = process.communicate(b'Test\n')
