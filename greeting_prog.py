import time
name=input("your name:")
timestamp=time.strftime("%H:%M")
# print(timestamp,type(timestamp))
# hour=time.strftime("%H")
# print(hour)
# minute=time.strftime("%M")
# print(minute)
# print(type(minute))
if(timestamp<"12:00"and timestamp>"00:00" ):
    print(f"Good morning {name}")
elif(timestamp<"16:00" and timestamp>"12:00"):
    print(f"Good afternoon {name}")
else:
    print(f"Good evening {name}")