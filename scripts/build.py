import json
import os
import sys

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './build-conf.json')

with open(file=filename) as f:
    settings = json.load(f)

source_file = sys.argv[1]
target_file_extension = settings.get("output_extension")
target_file = source_file.split(".")[0] + (
    "" if target_file_extension is None else target_file_extension
)

command = f"g++ -o {target_file} {source_file}"

os.system(command)
