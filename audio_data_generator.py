import argparse
import os
import json

__dir__ = os.path.dirname(os.path.dirname(__file__))

arabic_file_kubro = open(f"{__dir__}/locales/data/kubro_section.json")
arabic_file_sugro = open(f"{__dir__}/locales/data/sugro_section.json")

parser = argparse.ArgumentParser()
parser.add_argument("--dzikir_type", dest="dzikir_type", type=str, help="Please Add Al Matsurat Type")
parser.add_argument("--audio_src", dest="audio_src", type=str, help="Please Add Audio src")
parser.add_argument("--audio_prefix", dest="audio_prefix", type=str, help="Please Add Audio Prefix")

parser.add_argument("--audio_name", dest="audio_name", type=str, help="Please Add Al Matsurat Audio Name")
parser.add_argument("--audio_file_name", dest="audio_file_name", type=str, help="Please Add Al Matsurat Audio File Name")

parser.add_argument("--dzikir_time", dest="dzikir_time", type=str, help="Please Add Al Matsurat Audio Dzikir Time")


args = parser.parse_args()

dzikir_type = args.dzikir_type
audio_src = args.audio_src
audio_prefix = args.audio_prefix

audio_name = args.audio_name
audio_file_name = args.audio_file_name
dzikir_time = args.dzikir_time

kubroSections = 100
sugroSections = 57

audioData = {}

audioData['name'] = audio_name
audioData['prefix'] = audio_prefix

if dzikir_type == "kubro" :
    repeatUntil = kubroSections
    loads = json.loads(arabic_file_kubro.read())
else :
    repeatUntil = sugroSections
    loads = json.loads(arabic_file_sugro.read())

audioData['contents'] = {}

for i in range(repeatUntil):
    audioData['contents'][loads[str(i)]] = str(audio_src).format(n = i+1)

arabic_file_sugro = open(f"{__dir__}/audio/{dzikir_type}/{dzikir_time}/{audio_file_name}.json", "w")

arabic_file_sugro.write(str(audioData).replace("'", "\""))

