import alexpy

def write(res,filename):
    with open(filename, 'a') as f:
        f.write(str(res) + "\n")
        f.close()

def runThrough(x):
    for i in range(x):
        experiment1 = alexpy.AlexPy("resources/sample_keys.bin","binary",500,1000,1000,0.5,"uniform")
        result = experiment1.main()
        write(result,"output.txt")

if __name__ == "__main__":
    #default
    runThrough(10)