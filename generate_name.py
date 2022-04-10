import os
import json
import argparse
import string

__dir__ = os.path.dirname(os.path.dirname(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("--dzikir_type", dest="dzikir_type", type=str, help="Please Add Al Matsurat Type")
parser.add_argument("--dzikir_time", dest="dzikir_time", type=str, help="Please Add Al Matsurat Audio Dzikir Time")

args = parser.parse_args()

dzikir_type = args.dzikir_type
dzikir_time = args.dzikir_time

dir_path = os.path.join(__dir__, "audio", dzikir_type, dzikir_time)

files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.json') and f != "list.json"]
print(files)

names = []

for file in files:
    with open(file) as jsonFile:
        names.append({"name": json.loads(jsonFile.read())['name'], "file_name": os.path.basename(jsonFile.name)})

with open(os.path.join(dir_path, "list.json"), "w") as jsonFile:
        jsonFile.writelines(str(names).replace("'", "\""))