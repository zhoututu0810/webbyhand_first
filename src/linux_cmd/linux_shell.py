import subprocess
p = subprocess.Popen(args=['/Users/alice/PycharmProjects/webbyhand_first/src/linux_cmd/to.sh', '1', '2'], shell=True, stdout=subprocess.PIPE)
print(p.stdout.read())