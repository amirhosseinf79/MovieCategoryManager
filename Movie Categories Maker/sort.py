
import sys
import os
import re

files = os.listdir()
for n in range(len(files)):
    if re.findall("\.mkv|\.mp4",files[n]):
        clear_name = re.match("(.)* [1900-2100]",files[n])[0][:-2]
    else:
        continue
    
    old_name = files[n]
    new_name = re.sub(" - Shortcut","",files[n])            
    try:
        os.mkdir(clear_name)
    except:
        pass
    try:
        os.rename("{}".format(old_name),"{}/{}".format(clear_name,new_name))
    except:
        pass
    print("{} Copied to {}/{}".format(old_name,clear_name,new_name))
    
    for m in range(n+1,n+len(files)):
        if re.findall("{}".format(clear_name),files[m]):
            old_name = files[m]
            new_name = re.sub(" - Shortcut","",files[m])
            
            try:
                os.rename("{}".format(old_name),"{}/{}".format(clear_name,new_name))
            except:
                pass
            print("{} Copied to {}/{}".format(old_name,clear_name,new_name))
        else:
            break