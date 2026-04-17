import subprocess, os

for i in range(5):
    os.chdir(str(i+1))
    subprocess.call('py runme.py')
    os.chdir("../")