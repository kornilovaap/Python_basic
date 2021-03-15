# V.1
# import time
#
# start = time.time()
# print(f"Start at {start}")
#
# time.sleep(2)
#
# end = time.time()
# print(f"End at {end}")

# V.2
# from time import time, sleep
#
# start = time()
# print(f"Start at {start}")
#
# sleep(2)
#
# end = time()
# print(f"End at {end}")

# V.3
from time import time as std_time, sleep as std_sleep

start = std_time()
print(f"Start at {start}")

std_sleep(2)

end = std_time()
print(f"End at {end}")

