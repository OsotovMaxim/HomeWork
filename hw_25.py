import os
import subprocess

results = 'Results'
link = 'Source'
current_dir = os.path.dirname(os.path.abspath(__file__))
source = os.path.join(current_dir, link)
fotos = os. listdir(source)
path_name = os.path.join(current_dir, results)
if results not in os.listdir(current_dir):
    os.mkdir(path_name)
for foto in fotos:
    subprocess.Popen('convert.exe {}/{} -resize 200 {}/{}'.format(link, foto, results, foto))