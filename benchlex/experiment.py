import alexpy
import os
import csv
import subprocess

class experiment():
    def __init__(self,lookup_distribution, user, insert_frac, keys_file, keys_file_type, K, L, N):
        self.keys_file = keys_file
        self.keys_file_type = keys_file_type
        self.lookup_distribution = lookup_distribution
        self.user = user
        self.insert_frac = insert_frac
        self.K = K
        self.L = L
        self.N = N
        
    #def write(res,filename):
        #with open(filename, 'a') as f:
            #f.write(str(res) + "\n")
            #f.close()

    def runThrough(self, x):
        #filename = f"/home/{self.user}/BenchLex/benchlex/output.txt"
        #if os.path.isfile(filename):
            #os.remove(filename)

        lookups = []
        inserts = []
        ops = []
        for i in range(x):
            experiment1 = alexpy.AlexPy(self.keys_file,self.keys_file_type,self.N / 2,self.N,self.N,self.insert_frac,self.lookup_distribution, self.user)
            result = experiment1.main()
            #experiment.write(result,filename)
            lookups.append(result[0])
            inserts.append(result[1])
            ops.append(result[2])
        return [self.K, self.L, sum(lookups)/x, sum(inserts)/x, sum(ops)/x] #cast K,L to int


    def createKeysFile(self):
        path = "/home/" + self.user + "/bods/src/sortedness_data_generator"
        cmd = path + f"\
        -N {self.N} \
        -K {self.K} \
        -L {self.L} \
        -S 1 \
        -o /home/{self.user}/bods/workloads/createdata_N{self.N}_K{self.K}_L{self.L}_S1234_a1_b1_P4.txt \
        -a 1\
        -b 1\
        -P 4"
        subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
if __name__ == "__main__":
    #default'
    user = input("user: ")

    #for i in range(101):
    #test = experiment("uniform", user, 0.5, f"/home/sbasil/bods/workloads/createdata_N1000_K{1}_L{1}_S1234_a1_b1_P4.txt","text", 0.1, 1)
    #test.createKeysFile()
    #print(test.runThrough(1))

    
    #writing to csv
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


    
