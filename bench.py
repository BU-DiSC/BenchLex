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
    
def call_benchmark(args):
    result = subprocess.run(f"./build/benchmark \
    --keys_file={args['keys_file']} \
    --keys_file_type={args['keys_file_type']} \
    --init_num_keys={args['init_num_keys']} \
    --total_num_keys={args['total_num_keys']} \
    --batch_size={args['batch_size']} \
    --insert_frac={args['insert_frac']}", shell=True, capture_output=True, text=True).stdout
    return result.splitlines()[-1]

def output(result):
    out = result.strip().split("\t")[1:]
    out[0] = out[0][:-1]
    out[1] = out[1][:-1]
    out = tuple(out)
    out = tuple(int(float(i.split()[0])) for i in out)
    return out

def main():
    args = loadArgs()
    result = call_benchmark(args)
    out = output(result)
    print(out)


if __name__ == "__main__":
    main()
