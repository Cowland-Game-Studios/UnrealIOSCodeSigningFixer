import os
import time
import yaml

#get info from yaml file
try:
    with open("Settings.yaml", 'r') as f:
        YamlInfo = yaml.safe_load(f)
        
        #setup info

        Path = YamlInfo['Path']
        Delay = int(YamlInfo['Delay'])

except:
    raise SystemExit("\nCould not load all info, Or file nonexistant. \nIf file corrupted, reinstall the applicatoin and reenter info. \nIf the file doesn't exist, make sure you are in the root directory of the python script.")

#making sure you're not bsing the path
if not os.path.exists(Path):
    raise SystemExit(f"\n{Path} is not a valid path\n")
else:
    print(f"\n{Path} is a vaid path \n")

#confirm run
if(input("\nAny Key & Enter To Start, \"X\" & Enter To Cancel \n\n>>>").strip().lower() == "x"):
    raise SystemExit("\nOperation Cancelled\n")

#clear the folder, and stop the bug from happening
try:
    while True:
        os.system(f"xattr -cr {Path}")
        print(f"Cleared {Path}, Press Ctrl+C to stop")
        time.sleep(Delay)
        print(f"Delayed for {Delay}")
except:
    raise SystemExit("\nError, Could not clear/delay script\n")