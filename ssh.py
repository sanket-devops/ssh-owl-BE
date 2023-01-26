import paramiko
import sys

def ssh_conn():
    hostName = "192.168.120.191"
    hostUser = "prod-proxy"
    hostPass = "Yxorp$11-Jan-2023%dorP"
    results = []

    commands = ["cat /etc/hostname", "ip add | grep '192.168'", "cat /home/prod-proxy/temp.txt"]
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostName, username=hostUser, password=hostPass)
    for command in commands:
        temp = []
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(command)
        for line in ssh_stdout:
            nRemove = line.strip('\n')
            temp.append(nRemove)
        results.append(temp)
    print(results)
    return results