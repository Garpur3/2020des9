import time
import datetime

class Time():
    initial_time = time.process_time()
    times = {}

    def add(time_id):
        Time.times[time_id] = time.process_time()
    
    def delta(id1, id2):
        return abs(Time.times[id1] - Time.times[id2])

    def pause(time_id):
        Time.times[time_id] = str(Time.times[time_id])

    def unpause(time_id):
        if type(Time.times[time_id]) == str:
            Time.times[time_id] = time.process_time() - float(Time.times[time_id])
        else:
            pass
    
    def get_time(time_id):
        return time.process_time() - Time.times[time_id]

    def make_time(sec_float):
        try:
            sec = int(sec_float)
            hh = sec//3600
            sec -= hh*3600
            mm = sec//60
            sec -= mm*60
            time_string = "{}:{}:{}".format(("0"+str(hh))[-2:],("0"+str(mm))[-2:],("0"+str(sec))[-2:])
            return(time_string)

        except Exception:
            return 'Invalid input'

    def print_time(seconds_float):
        print(f'Runtime: {Time.make_time( seconds_float )}')
        print(f'Seconds: {seconds_float:.4f}')

