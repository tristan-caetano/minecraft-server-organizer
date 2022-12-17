# Tristan Caetano
# Serber Accesser
# Script that allows the user to remotely turn on the minecraft server

# This script is to be run from any computer that wants to turn on the server remotely

# Importing packages
import paramiko
import pandas as pd
import time

# Function to turn server on and run commands
def run_commands():

    # Getting csv data
    ssh_data = pd.read_csv('ssh_data.csv')

    # Setting Serber Credentials
    server = ssh_data['serverip'][0]
    username = ssh_data['username'][0]
    password = ssh_data['password'][0]

    # SSHing into server
    print("\nConnecting to pi...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)
    print("\nConnection successful!")

    # Turning on and starting server
    pi_cd_comm = "cd Documents/Code/minecraft-server-organizer"
    pi_relay_comm = "./pi"
    pi_to_serber_comm = "python3 run_from_pi.py"

    print("Turning on server.")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(pi_cd_comm)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(pi_relay_comm)
    time.sleep(40)
    print("Starting server")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(pi_to_serber_comm)

run_commands()