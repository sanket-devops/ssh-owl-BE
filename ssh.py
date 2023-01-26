import paramiko
import sys

hostName = "localhost"
hostUser = "****"
hostPass = "****"

command = ["cat /etc/hostname", "ip add | grep '192.168'", "cat /etc/os-release"]
# results = []

def ssh_conn():
    results = []
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostName, username=hostUser, password=hostPass)
    for x in command:
        temp = []
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(x)
        print(ssh_stdout)
        for line in ssh_stdout:
            temp.append(line.strip('\n'))
        results.append(temp)
    return results