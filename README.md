# folder_sync
A Python program that synchronizes two folders: source and replica. It performs one-way synchronization periodically and logs the file operations. It uses command line arguments for folder paths, interval, and log file path. It uses hashlib for MD5 calculation.

## Run:
1. Create two folders: one for the source and one for the replica.
2. Open PowerShell and run the following command: python task.py source_folder replica_folder -i 10 -l sync.log

- The `source_folder` should be replaced with the path to your source folder.
- The `replica_folder` should be replaced with the path to your replica folder.
- The `-i 10` argument specifies the synchronization interval in seconds. You can change the `10` to any desired interval in seconds.
- The `-l sync.log` argument specifies the path to the log file where the file operations will be recorded. You can change `sync.log` to a different file name or provide a different path.

4. The program will start running and synchronize the source folder with the replica folder at the specified interval. Any changes made in the source folder will be reflected in the replica folder, and the file operations will be logged in the specified log file.

5. You can stop the program by pressing `Ctrl+C` in the terminal or PowerShell window.

Feel free to customize the folder paths, synchronization interval, and log file path according to your specific requirements.

## Dependencies
This program requires Python to be installed on your system. It also uses the `hashlib` library for MD5 calculation, which is a standard library in Python.

