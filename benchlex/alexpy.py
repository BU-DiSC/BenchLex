import subprocess
# import the benchmark from bench.py


"""
Python wrapper around ALEX to call and record values from ALEX
"""

class AlexPy():
    def __init__(self,keys_file,keys_file_type,init_num_keys,total_num_keys,batch_size,insert_frac, lookup_distribution, user):
        self.keys_file = keys_file 
        self.keys_file_type = keys_file_type
        self.init_num_keys = init_num_keys
        self.total_num_keys = total_num_keys
        self.batch_size = batch_size
        self.insert_frac = insert_frac
        self.lookup_distribution = lookup_distribution
        self.user = user

    def run(self):
        path = "/home/" + self.user + "/ALEX/build/benchmark"
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
    
    
    def output(result):
        out = result.strip().split("\t")[1:]
        out[0] = out[0][:-1]
        out[1] = out[1][:-1]
        out = tuple(out)
        out = tuple(int(float(i.split()[0])) for i in out)
        return out


    # def bench(self):
    def main(self):
        aResult = AlexPy(self.keys_file,self.keys_file_type,self.init_num_keys,self.total_num_keys,self.batch_size,self.insert_frac, self.lookup_distribution, self.user)
        result = AlexPy.run(aResult)
        out = AlexPy.output(result)
        return out


