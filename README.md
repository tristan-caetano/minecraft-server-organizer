# minecraft-server-organizer
This project uses a series of scripts, a Raspberry Pi, and a relay to remotely start a Minecraft server. Anyone given the main program and their IP allowed will be able to turn on the computer as well as the Minecraft server.

## Packages Required
This project requires the following packages:

**paramiko**: Performs the required SSH connections.

**glob**: Searches directory for file paths.

**pandas**: Parses the .csv files.

## Initial Setup
**THIS PROGRAM IS SETUP TO RUN A MINECRAFT SERVER ON A LINUX MACHINE, ALTHOUGH THE START SCRIPT CAN RUN ON ANY DEVICE THAT HAS PYTHON**

List of scripts and what they do:

**serber_accesser.py**: SSHs from the client computer (any OS) to the Raspberry Pi to run the **pi_remote_power.c** binary and the **run_from_py.py** script. This script can exist in and be ran from anywhere on the client system.

**pi_remote_power.c**: Required to be compiled to **pi.a**. This binary sends a signal from the Raspberry Pi to the Minecraft server to turn it on. This script should be placed in the *Documents/Code/minecraft-server-organizer* directory of the Raspberry Pi.

**run_from_py.py**: SSHs from the Raspberry Pi to the Minecraft server, and runs the **jar_collector.py** script and starts the first server in the list. This script should be placed in the *Documents/Code/minecraft-server-organizer* directory of the Raspberry Pi.

**jar_collector.py**: Stores the LaunchServer.sh script locations of multiple servers on the same machine and can run them from a single place. This script should be placed in the */home* directory of the Minecraft server.

## Server Setup

Once **jar_collector.py** has been placed in the correct directory on the server, run it with this command: `python3 jar_collector.py`
A menu will appear in the terminal, follow it to add a minecraft server to the list. Please note that this pipeline will only run the firstserver that you added to the list. You can view the list within the program, or by viewing the **server_list.csv** that is created. It has the following format:

|servername  |mod         |version     |directory   |launch_shell|
|------------|------------|------------|------------|------------|

## SSH Setup
These scripts require for there to be an SSH server on both the Raspberry Pi, and the Minecraft server. 

The Raspberry Pi's SSH server should be accessible from anywhere such as being portforwarded. 

The Minecraft server's SSH server can be either local or public.

The SSH server should have a password, should require an IP whitelist, or use RSA tokens. Although these aren't *required* for the program to work, it will leave your system vulnerable so its **HIGHLY** recommended you take these security precautions.

Finally, a file **ssh_data.csv** must be created, and the following format must be made.

|serverip|username|password|
|--------|-------|---------|

The first column is the **public** serverip, username, and password  of the Raspberry Pi.

The second column is the **local** serverip, username, and password  of the Minecraft server.

This file needs to be placed in the same directory as the **serber_accesser.py** on the client machine **and** the **run_from_py.py** on the Raspberry Pi.

Yes, this isn't particularly secure, but it can only be accessed once the password is already known. Not to mention the whitelist and RSA keys. The password is really just one step in what should be 2 or 3 step authentication.

## Start Script
Once all scripts are placed in their correct locations, **pi_remote_power.c** is compiled, and the SSH servers are setup, all that is needed to do is to run `python3 serber_accesser.py`.
