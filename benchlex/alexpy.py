import subprocess
# import the benchmark from bench.py
import sys
sys.path.append("bench")
from bench import *

"""
Python wrapper around ALEX to call and record values from ALEX
"""
class AlexPy():
    def __init__(self,keys_file,keys_file_type,init_num_keys,total_num_keys,batch_size,insert_frac):
        self.keys_file = keys_file 
        self.keys_file_type = keys_file_type
        self.init_num_keys = init_num_keys
        self.total_num_keys = total_num_keys
        self.batch_size = batch_size
        self.insert_frac = insert_frac
        return

    def bench(self):
        main()
        return
