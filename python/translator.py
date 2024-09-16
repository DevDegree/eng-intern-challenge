import os
import subprocess
import sys

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__))
    executable = f'{script_dir}/../rust/target/release/rust'

    command = [executable]
    command += sys.argv[1:]

    subprocess.run(command)
