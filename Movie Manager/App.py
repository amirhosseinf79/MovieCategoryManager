
from datetime import datetime as dt
import numpy as np
import os
import re

def name_maker(name):
    file_name2 = name
    file_type2 = re.findall("\..{3}$",file_name2)
    if len(file_type2)>0:
        file_type2 = file_type2[0]
    else:
        file_type2 = "" 
    file_name2 = re.sub(file_type2,"",file_name2)
    file_name2 = re.sub("\."," ",file_name2)
    file_name2 = re.sub(" - shortcut","",file_name2)
    file_name2 += file_type2
    return file_name2

try:
    app_root = "Category"
    os.mkdir("{}".format(app_root))
except:
    pass

for (root,dirs,files) in os.walk(os.getcwd()):
    if len(re.findall(app_root,root))==0:
        for file in files:
            file_name = name_maker(file)
    
            file_name_match = re.match("(.)* ([1800-{}])".format(dt.now().strftime("%Y")),file_name)
    
            if file_name_match:
                try:
                    movie_folder = file_name_match[0][:-2]
                except:
                    movie_folder = dt.now().strftime("%Y%m%d - {}".format(np.random.randint(10,1500)))
                try:
                    os.mkdir("{}/{}".format(app_root,movie_folder))
                except:
                    pass
                try:
                    os.rename("{}/{}".format(root,file),"{}/{}/{}".format(app_root,movie_folder,file_name))
                except:
                    pass
                for dupfile in files:
                    file_name2 = name_maker(dupfile)
                    
                    if re.findall(movie_folder,file_name2) and file != dupfile:
                        try:
                            os.rename("{}/{}".format(root,dupfile),"{}/{}/{}".format(app_root,movie_folder,file_name2))
                        except:
                            pass