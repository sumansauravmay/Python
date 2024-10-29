import time;
timestamp=time.strftime('%H:%M:%S');
print(timestamp);

hour=time.strftime('%H');
print(hour);

# hour=input("Put hours ");
hour=int(hour);

minute=time.strftime('%M');
print(minute);


second=time.strftime('%S');
print(second);




if(hour>=0 and hour<12):
    print("Good Morning!")
elif (hour>=12 and hour<15):
    print("Good Afternoon!")
elif(hour>=15 and hour<21):
    print("Good Evening!")
elif(hour>=21 and hour<=0):
    print("Good Night!")
else:
    print("Invalid Hours")
    
    
    
    