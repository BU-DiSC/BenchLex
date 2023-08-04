import os
import sys
import csv
import subprocess

class Experiment1():
    def __init__(self,user) -> None:
        self.user = user
        

    def run(self):
        sys.path.insert(0, f'/home/{self.user}/BenchLex/benchlex/')
        from experiment import experiment
        print("Running Experiment1...")

        fields = ["K","L", "lookups/sec", "inserts/sec", "ops/sec", "loadtime"]
        rows = []
        filename = "data10.csv"
        N = 1000000
        for k in range(0,101,10):
            for l in range(0,101,10):
                if not(k == 7 and l == 60):
                    test = experiment("uniform", self.user, 0.5, f"/home/{self.user}/bods/workloads/createdata_N{N}_K{k}_L{l}_S1234_a1_b1_P0.txt","text", k, l, N)
                    test.createKeysFile()
                    rows.append(test.runThrough(2)) #run each insert_frac 10 times, calc mean
                    print(k, l)
        
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
            
            # writing the fields 
            csvwriter.writerow(fields) 
            
            # writing the data rows 
            csvwriter.writerows(rows)
