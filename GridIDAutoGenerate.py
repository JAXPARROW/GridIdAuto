from datetime import datetime
import time


def grid_id():
    prefix = "PGRD"
    now = datetime.now()
    data_time = str(int(now.strftime("%Y%m%d%H%M%S%f")))
    uid = prefix+data_time
    #print(uid)
    return(uid)
grid_id()

