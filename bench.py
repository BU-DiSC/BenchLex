import subprocess
import argparse
import sys
sys.path.insert(0,"./benchlex/experiments")
import experiment1
import experiment2
import experiment3
import experiment4
sys.path.insert(0,"./benchlex/")
import alexpy

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
    parser.add_argument('--nb_of_runs', help='Nb of times to run experiment', required=True)
    return vars(parser.parse_args())

def call(args):
    nb = subprocess.run(f'--run_experiment={args}')

def experim():
    args = menu()
    nb = int(call(args))
    if(nb == 1):
        experiment1.run()
    elif(nb == 2):
        experiment2.run()
    elif(nb == 3):
        experiment3.run()
    elif(nb == 4):
        experiment4.run()
    else:
        print("Error: experiment not found")






    

