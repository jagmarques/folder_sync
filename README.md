# folder_sync
A Python program that synchronizes two folders: source and replica. It performs one-way synchronization periodically and logs the file operations. It uses command line arguments for folder paths, interval and log file path. It uses hashlib for MD5 calculation.

Run:
Create two folders: one for the source and one for the replica.
Open the Power Shell and run the following command: python task.py source_folder replica_folder -i 10 -l sync.log
The -i 10 argument specifies the synchronization interval in seconds, and the -l sync.log argument specifies the log file path. You can change these values as needed.
