import subprocess
import argparse
import sys
import os
from benchlex.experiments.Experiment1 import Experiment1
from benchlex.experiments.Experiment2 import Experiment2
from benchlex.experiments.Experiment3 import Experiment3
from benchlex.experiments.Experiment4 import Experiment4
from benchlex.alexpy import AlexPy


def loadArgs():
    parser = argparse.ArgumentParser(description='Arguments for benchmark')
    parser.add_argument('--keys_file', help='keys file', required=True)
    parser.add_argument('--keys_file_type', help='keys file type', required=True)
    parser.add_argument('--init_num_keys', help='init num keys', required=True)
    parser.add_argument('--total_num_keys', help='total num keys', required=True)
    parser.add_argument('--batch_size', help='batch size', required=True)
    parser.add_argument('--insert_frac', help='insert fraction', required=True)
    parser.add_argument('--lookup_distribution', help='lookup_distribution', required=True)
    return vars(parser.parse_args())

def menu():
    parser = argparse.ArgumentParser(description='modes for bench.py')
    parser.add_argument('--run_experiment', help='Run experiment', required=True)
    return vars(parser.parse_args())

def call(args):
    nb = args["run_experiment"]
    return nb


def experim():
    args = menu()
    # print(args)
    nb = call(args)
    # print(nb)
    if(nb == "1"):
        ex = Experiment1(user)
        ex.run()
        
    elif(nb == "2"):
        ex = Experiment2(user)
        ex.run()
    elif(nb == "3"):
        ex = Experiment3(user)
        ex.run()
    elif(nb == "4"):
        ex = Experiment4(user)
        ex.run()
    else:
        print("Error: experiment not found")


if __name__ == "__main__":
    #default'
    user = input("user: ")
    experim()



    

