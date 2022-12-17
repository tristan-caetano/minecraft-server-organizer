# Tristan Caetano
# Remote Server Activation
# Script that allows the pi to connect to the server and start it

# This script is to be run from the pi from the serber_accesser.py script

# Importing packages
import paramiko
import pandas as pd

# Function to turn server on and run commands
def run_commands():

    # Getting csv data
    ssh_data = pd.read_csv('ssh_data.csv')

    # Setting Serber Credentials
    server = ssh_data['serverip'][1]
    username = ssh_data['username'][1]
    password = ssh_data['password'][1]

    # SSHing into server
    print("\nConnecting to server...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)
    print("\nConnection successful!")

    serber_start_com = "screen -S serber -dm python3 jar_collector.py 1"

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(serber_start_com)

run_commands()
