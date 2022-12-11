# Tristan Caetano
# Minecraft Server Organizer
# Script that collects and organizes Minecraft server properties and jar files

# Importing packages
from os.path import exists
import pandas as pd
import glob
import os

# Script for running server
def run_server():

    # Naming csv file
    server_list = "server_list.csv"

    list_num = 1

    # Checking if there is already a csv file
    if exists(server_list):
        list = pd.read_csv(server_list)
    else:
        print("No .csv found.\nMake sure the .csv is named 'server_list.csv'.\nExiting to main menu.\n")
        main_menu()
    
    print("\nPlease input the number of the server that you would like to run.\n")

    # Printing out the list of just the server names
    for x in range(0, len(list)):
        print(str(list_num) + ").", str(list.iloc[x][0])), "\n"
        list_num += 1

    # Getting the user choice for the server that they want to run
    shell_in = int(input())

    # Getting shell file information
    shell = list['launch_shell'][shell_in - 1]
    shell_loc = list['directory'][shell_in - 1]

    # Running the server
    os.system("chmod +x '" + shell + "'")
    os.system("(cd '" + shell_loc + "' ; '" + shell + "')")


# Saving the server info to a csv file
def save_server_info(data_list):

    # Naming csv file
    server_list = "server_list.csv"

    # Checking if there is already a csv file
    if exists(server_list):
        list = pd.read_csv(server_list)
    else:
        list = pd.DataFrame(columns=["servername", "mod", "version", "directory", "launch_shell"])

    # Adding new data to list
    list.loc[len(list.index)] = data_list

    # Saving data to csv file
    list.to_csv(server_list, index=False)

# Using the given directory, gather shell files
def find_shells(data_list):

    # Appending .sh to the directory
    path_search = data_list[3] + "*.sh"

    # Getting list of all shell scripts in directory
    list_of_shells = glob.glob(path_search)

    # Iterator for list
    list_num = 1

    # Printing out all found files to user
    for item in list_of_shells:
        print(str(list_num) + ").", item), "\n"
        list_num += 1
    
    # Asking user to choose file found
    chosen_num = int(input("Which shell is the launch shell?"))
    data_list.append(list_of_shells[chosen_num - 1])

    # Saving data to csv
    save_server_info(data_list)

# Getting basic server information and directory location
def get_server_location():

    # Boolean variables
    server_details_acquired = False
    server_directory_found = False

    # While loop that keeps asking the user for the directory if it can't find server.properties
    while not server_directory_found:

        # If basic server data hasn't been collected yet, it will here
        if not server_details_acquired:

            # Getting server name, if its modded, and the mc version
            name = input("\nWhat is the name of the server?\n")
            modded = input("\nInput the name of the mod, input 'vanilla' for no mods.\n")
            version = input("\nWhat version of Minecraft is it?\n")

            # Getting the directory of the server, and appending server.properties
            directory = input("\nInput the directory of the server folder.\nMake sure there is a slash at the end.\n")
            server_properties = directory + "/server.properties"

            # Details completed, skipping if
            server_details_acquired = True

        # Checking if server.properties exists, if not, asking user for the directory again
        if exists(server_properties):

            print("\nServer Properties found, proceeding...\n")
            server_directory_found = True

        else:

            directory = input("\nServer Properties not found, input correct server directory:\n")
            server_properties = directory + "/server.properties"

        # Creating list containing server info
        data_list = [name, modded, version, directory]
        
        # Sending info to find shell files
        find_shells(data_list)

# Main menu
def main_menu():

    # List of menu options
    list_of_options = ["Add new server config.", 
                        "Run server.",]
    # Iterator for list
    list_num = 1

    while(True):

        print("\nMinecraft Server Organizer\nMain Menu\n")

        # Printing out all found files to user
        for option in list_of_options:
            print(str(list_num) + ").", option), "\n"
            list_num += 1
        
        menu_in = input("\nEnter 'q' to quit, 's' to shutdown, or 'r' to reboot.\n")

        if menu_in == "q" or menu_in == "Q":
            quit()
        elif menu_in == "s" or menu_in == "S":
            os.system("shutdown")
            quit()
        elif menu_in == "r" or menu_in == "R":
            os.system("reboot")
            quit()
        elif menu_in == '1':
            get_server_location()
        elif menu_in == '2':
            run_server()
        else:
            print("\nCommand not found, please input an available number or 'q'.\n")

        list_num = 1

main_menu()