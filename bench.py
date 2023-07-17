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
    parser.add_argument('--lookup_distribution', help='lookup_distribution', required=True)
    return vars(parser.parse_args())
    
