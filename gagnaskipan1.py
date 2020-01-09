

def make_time(sec_str):
    if sec_str.isdigit():
        sec = int(sec_str)
        hh = sec//3600
        sec -= hh*3600
        mm = sec//60
        sec -= mm*60
        time_string = "HOuR{}:mInuiTE{}:sECoNds{}".format(("0"+str(hh))[-2:],("0"+str(mm))[-2:],("0"+str(sec))[-2:])
        return(time_string)

    else:
        return("Invalid input.")

def main():
    sec = input("enter time in seconds: ")

    print(make_time(sec))

main()