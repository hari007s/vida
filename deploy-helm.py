import re
import os
os.system('pip3 install paramiko')
import paramiko
import sys

host = sys.argv[1]
port = 10004
username = sys.argv[2]
password = sys.argv[3]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command("export KUBECONFIG=/root/kubeconfig.yaml \n helm delete wp \n helm repo update \n helm install wp hb/wordpress-mysql-stateless")
stdin.close()
lines = stdout.readlines()
print (lines)
stdout.close()
stdin.close()
ssh.close()
