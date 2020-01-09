import time


class Tiem:
    tiems = {}

    def __init__(self):
        self.t0 = time.time()

    def time_i_has_been_running(self):
        timed = int(time.time() - self.t0)
        return Tiem.make_time(str(timed))

    def set(id):
        if id in Tiem.tiems.keys():
            print("ID in use")
        else:
            Tiem.tiems[id] = get_time()

    def delta(id):
        if id in Tiem.times.keys():
            return get_time() - Tiem.tiems[id]
        else:
            print("ID not in use")

    def make_time(sec_str):
        if sec_str.isdigit():
            sec = int(sec_str)
            hh = sec//3600
            sec -= hh*3600
            mm = sec//60
            sec -= mm*60
            time_string = "{}:{}:{}".format(("0"+str(hh))[-2:],("0"+str(mm))[-2:],("0"+str(sec))[-2:])
            return(time_string)

        else:
            return("Invalid input.")

import random
n = 20000000
t = Tiem()
random_list = []
for i in range(n):
    random_list += [random.random()]
print(t.time_i_has_been_running())

