import subprocess
# import the benchmark from bench.py
user =  input("user: ")
import sys
sys.path.insert(0,"/home/" + user + "/BenchLex/")
from bench import *

"""
Python wrapper around ALEX to call and record values from ALEX
"""

class AlexPy():
    def __init__(self,keys_file,keys_file_type,init_num_keys,total_num_keys,batch_size,insert_frac, lookup_distribution):
        self.keys_file = keys_file 
        self.keys_file_type = keys_file_type
        self.init_num_keys = init_num_keys
        self.total_num_keys = total_num_keys
        self.batch_size = batch_size
        self.insert_frac = insert_frac
        self.lookup_distribution = lookup_distribution
        

    def run(self):
       
        path = "/home/" + user + "/ALEX/build/benchmark"
        cmd = path + f"\
        --keys_file={self.keys_file} \
        --keys_file_type={self.keys_file_type} \
        --init_num_keys={self.init_num_keys} \
        --total_num_keys={self.total_num_keys} \
        --batch_size={self.batch_size} \
        --insert_frac={self.insert_frac}\
        --lookup_distribution={self.lookup_distribution}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
        return result.splitlines()[-1]

    # def bench(self):
    def main(self):
        aResult = AlexPy(self.keys_file,self.keys_file_type,self.init_num_keys,self.total_num_keys,self.batch_size,self.insert_frac, self.lookup_distribution)
        result = AlexPy.run(aResult)
        out = output(result)
        print(out)


