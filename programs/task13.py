

# delete all .csv files

import os
import shutil
try:
    files = os.listdir()
    #print(files)
    for file in files:
        if os.path.isfile(file)  and file.endswith(".csv") :
            backupname = file + ".bak"
            shutil.copy(file,backupname)
            print("backup is taken for", file)
            os.remove(file)
            print(file,"is deleted")
except Exception as err:
    print(err)

