import os
import sys
import time
import shutil
import logging
import argparse
import hashlib

# Defining a function that synchronizes two folders
def sync(source, replica):
    # Logging the start of synchronization
    logging.info(f"Starting synchronization from {source} to {replica}")
    # Creating a set of source files and replica files
    source_files = set()
    replica_files = set()
    # Walking through the source folder and adding the relative paths to the set
    for root, dirs, files in os.walk(source):
        for file in files:
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, source)
            source_files.add(rel_path)
    # Walking through the replica folder and adding the relative paths to the set
    for root, dirs, files in os.walk(replica):
        for file in files:
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, replica)
            replica_files.add(rel_path)
    # Finding the files that are in source but not in replica (new or modified files)
    new_or_modified_files = source_files - replica_files
    # Finding the files that are in replica but not in source (deleted or renamed files)
    deleted_or_renamed_files = replica_files - source_files
    # Copying the new or modified files from source to replica
    for file in new_or_modified_files:
        # Getting the absolute paths of the source and replica files
        source_file = os.path.join(source, file)
        replica_file = os.path.join(replica, file)
        # Creating the parent directory of the replica file if it does not exist
        os.makedirs(os.path.dirname(replica_file), exist_ok=True)
        # Copying the file from source to replica
        shutil.copy2(source_file, replica_file)
        # Logging the copying operation
        logging.info(f"Copied {source_file} to {replica_file}")
    # Deleting or renaming the files from replica that are not in source
    for file in deleted_or_renamed_files:
        # Getting the absolute path of the replica file
        replica_file = os.path.join(replica, file)
        # Checking if the file has been renamed by comparing the MD5 hashes with the source files
        renamed = False
        for source_file in new_or_modified_files:
            # Getting the absolute path of the source file
            source_file = os.path.join(source, source_file)
            # Comparing the MD5 hashes of the source and replica files using the hashlib module
            if hashlib.md5(open(source_file, "rb").read()).hexdigest() == hashlib.md5(open(replica_file, "rb").read()).hexdigest():
                # The file has been renamed, so moving it to the new location
                shutil.move(replica_file, source_file)
                # Logging the moving operation
                logging.info(f"Moved {replica_file} to {source_file}")
                renamed = True
                break
        # If the file has not been renamed, then deleting it from replica
        if not renamed:
            # Deleting the file from replica
            os.remove(replica_file)
            # Logging the deletion operation
            logging.info(f"Deleted {replica_file}")
    # Logging the end of synchronization
    logging.info(f"Finished synchronization from {source} to {replica}")

# Defining a function that parses the command line arguments and returns them as a namespace object
def parse_args():
    # Creating an argument parser object
    parser = argparse.ArgumentParser(description="A program that synchronizes two folders")
    # Adding arguments for folder paths, synchronization interval and log file path 
    parser.add_argument("source", help="The path of the source folder")
    parser.add_argument("replica", help="The path of the replica folder")
    parser.add_argument("-i", "--interval", type=int, default=60, help="The synchronization interval in seconds (default: 60)")
    parser.add_argument("-l", "--log", default="sync.log", help="The path of the log file (default: sync.log)")
    # Parsing and returning the arguments as a namespace object 
    return parser.parse_args()

# Defining a function that configures the logging module 
def configure_logging(logfile):
    # Setting the basic configuration for logging 
    logging.basicConfig(
        # Setting the log file path 
        filename=logfile,
        # Setting the log level to INFO 
        level=logging.INFO,
        # Setting the log format to include the date, time, level and message 
        format="%(asctime)s - %(levelname)s - %(message)s",
        # Setting the date and time format to include the year, month, day, hour, minute and second 
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    # Creating a stream handler object to log to the console output 
    stream_handler = logging.StreamHandler()
    # Setting the level of the stream handler to INFO 
    stream_handler.setLevel(logging.INFO)
    # Setting the format of the stream handler to match the basic configuration 
    stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    # Adding the stream handler to the root logger 
    logging.getLogger().addHandler(stream_handler)

# Defining the main function that runs the program 
def main():
    # Parsing the command line arguments 
    args = parse_args()
    # Configuring the logging module 
    configure_logging(args.log)
    # Logging the start of the program 
    logging.info(f"Starting the program with arguments: {args}")
    # Entering an infinite loop that performs synchronization periodically 
    while True:
        # Calling the sync function with the source and replica folder paths 
        sync(args.source, args.replica)
        # Sleeping for the specified interval in seconds 
        time.sleep(args.interval)

if __name__ == "__main__":
    main()