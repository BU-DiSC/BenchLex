import alexpy

if __name__ == "__main__":
    experiment1 = alexpy.AlexPy("resources/sample_keys.bin","binary",500,1000,1000,0.5,"uniform")
    experiment1.main()