import time as t 
def speed_check():
    
    inp = input("press enter to start....")
    if not inp:
        start_time = t.perf_counter()
    words = len(input("> ").split())
    end_time = t.perf_counter()
    total_time = int(end_time - start_time)
    wpm = words * (60/total_time)
    print(total_time)
    print(f"{wpm} words per minute")

speed_check()