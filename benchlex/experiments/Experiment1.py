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

        fields = ["K","L", "lookups/sec", "inserts/sec", "ops/sec"]
        rows = []
        filename = "data.csv"
        for k in range(101):
            for l in range(101):
                test = experiment("uniform", self.user, 0.5, f"/home/{self.user}/bods/workloads/createdata_N{10000}_K{k}_L{l}_S1234_a1_b1_P4.txt","text", k, l, 10000)
                test.createKeysFile()
                rows.append(test.runThrough(100)) #run each insert_frac 10 times, calc mean
                print(k, l)
    
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
            
            # writing the fields 
            csvwriter.writerow(fields) 
            
            # writing the data rows 
            csvwriter.writerows(rows)