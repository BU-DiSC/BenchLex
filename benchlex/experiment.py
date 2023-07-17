import alexpy
import os

def write(res,filename):
    with open(filename, 'a') as f:
        f.write(str(res) + "\n")
        f.close()
        
# def runThrough(x):
#     for i in range(x):
#         experiment1 = alexpy.AlexPy("resources/sample_keys.bin","binary",500,1000,1000,0.5,"uniform")
#         result = experiment1.main()
#         write(result,"benchlex/output.txt")

def runThrough(x):
    filename = "benchlex/output.txt"
    if os.path.isfile(filename):
        os.remove(filename)
    lookups = []
    inserts = []
    ops = []
    for i in range(x):
        experiment1 = alexpy.AlexPy("resources/sample_keys.bin","binary",500,1000,1000,0.5,"uniform")
        result = experiment1.main()
        write(result,filename)
        lookups.append(result[0])
        inserts.append(result[1])
        ops.append(result[2])
    return sum(lookups)/len(lookups), sum(inserts)/len(inserts), sum(ops)/len(ops)

if __name__ == "__main__":
    #default
    print(runThrough(10000))