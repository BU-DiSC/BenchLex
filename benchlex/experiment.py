import alexpy
import os
import csv

class experiment():
    def __init__(self,lookup_distribution, user, insert_frac):
        self.lookup_distribution = lookup_distribution
        self.user = user
        self.insert_frac = insert_frac
        
    def write(res,filename):
        with open(filename, 'a') as f:
            f.write(str(res) + "\n")
            f.close()

    def runThrough(self, x):
        filename = f"/home/{self.user}/BenchLex/benchlex/output.txt"
        if os.path.isfile(filename):
            os.remove(filename)

        lookups = []
        inserts = []
        ops = []
        for i in range(x):
            experiment1 = alexpy.AlexPy("/home/"+ self.user +"/BenchLex/resources/sample_keys.bin","binary",500,1000,1000,self.insert_frac,self.lookup_distribution, self.user)
            result = experiment1.main()
            experiment.write(result,filename)
            lookups.append(result[0])
            inserts.append(result[1])
            ops.append(result[2])
        return [self.insert_frac, sum(lookups)/x, sum(inserts)/x, sum(ops)/x]

if __name__ == "__main__":
    #default'
    user = input("user: ")


    #writing to csv
    fields = ["insert_frac", "lookups/sec", "inserts/sec", "ops/sec"]
    rows = []
    filename = "data.csv"
    for i in range(1, 200): # i / 100 is insert frac
        test = experiment("uniform", user, i / 200)
        rows.append(test.runThrough(1000)) #run each insert_frac 1000 times, calc mean
        print(i)
    
    with open(filename, 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        
        # writing the data rows 
        csvwriter.writerows(rows)
