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
        for i in range(101): # i / 100 is insert frac
            test = experiment("uniform", user, 0.5, f"/home/{user}/bods/workloads/createdata_N{1000}_K{10}_L{i}_S1234_a1_b1_P4.txt","text", 10, i, 1000)
            test.createKeysFile()
            rows.append(test.runThrough(1000)) #run each insert_frac 1000 times, calc mean
            print(i)

        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
            
            # writing the fields 
            csvwriter.writerow(fields) 
            
            # writing the data rows 
            csvwriter.writerows(rows)