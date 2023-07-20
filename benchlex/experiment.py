import alexpy
import os

class experiment():
    def __init__(self,lookup_distribution, user):
        self.lookup_distribution = lookup_distribution
        self.user = user
        
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
            experiment1 = alexpy.AlexPy("/home/"+ self.user +"/BenchLex/resources/sample_keys.bin","binary",500,1000,1000,0.5,self.lookup_distribution, self.user)
            result = experiment1.main()
            experiment.write(result,filename)
            lookups.append(result[0])
            inserts.append(result[1])
            ops.append(result[2])
        return sum(lookups)/len(lookups), sum(inserts)/len(inserts), sum(ops)/len(ops)

if __name__ == "__main__":
    #default'
    user = input("user: ")
    test = experiment("uniform", user)
    print(test.runThrough(1))