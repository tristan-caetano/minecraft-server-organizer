# Tristan Caetano
# Minecraft Server Organizer
# Script that collects and organizes Minecraft server properties and jar files

# Importing packages
from os.path import exists
import pandas as pd

# Saving the server info to a csv file
def save_server_info(data_list):

    # Naming csv file
    server_list = "server_list.csv"

    # Checking if there is already a csv file
    if exists(server_list):
        list = pd.read_csv(server_list)
    else:
        list = pd.DataFrame(columns=["servername", "mod", "version", "directory"])

    # Adding new data to list
    list.loc[len(list.index)] = data_list

    # Saving data to csv file
    list.to_csv(server_list, index=False)

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
            directory = input("\nInput the directory of the server folder.\n Do NOT add a '/' to the end.\n")
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
        
        # Sending info to be saved to a csv file
        save_server_info(data_list)


get_server_location()