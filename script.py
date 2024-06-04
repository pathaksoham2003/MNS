import os
import subprocess

# Get the current working directory
current_directory = os.getcwd()

# Iterate from 1 to 601
for i in range(1, 602):
    dex_file = f"classes{i}-dex2jar.jar"
    command = f"jar xf ./{dex_file}"
    
    # Check if the .dex file exists before attempting to run the command
    if os.path.exists(os.path.join(current_directory, dex_file)):
        print(f"Executing: {command}")
        subprocess.run(command, shell=True)
    else:
        print(f"File {dex_file} does not exist in the directory {current_directory}")

print("Finished processing all .dex files.")