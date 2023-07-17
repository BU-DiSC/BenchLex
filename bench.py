import subprocess
import argparse

def loadArgs():
    parser = argparse.ArgumentParser(description='Arguments for benchmark')
    parser.add_argument('--keys_file', help='keys file', required=True)
    parser.add_argument('--keys_file_type', help='keys file type', required=True)
    parser.add_argument('--init_num_keys', help='init num keys', required=True)
    parser.add_argument('--total_num_keys', help='total num keys', required=True)
    parser.add_argument('--batch_size', help='batch size', required=True)
    parser.add_argument('--insert_frac', help='insert fraction', required=True)
    return vars(parser.parse_args())
    

def output(result):
    out = result.strip().split("\t")[1:]
    out[0] = out[0][:-1]
    out[1] = out[1][:-1]
    out = tuple(out)
    out = tuple(int(float(i.split()[0])) for i in out)
    return out
