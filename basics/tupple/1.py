# Tupple is immutable



# tup =(1,2,3);
# print(type(tup), tup);

# x =(1,);
# print(type(x), x);

# y =(1);
# print(type(y), y);

# tup[0]=90;
# print(type(tup), tup); #error-can't reassign

tup2=(1,2,3,"green", True);
# print(type(tup2));
# print(len(tup2))
# print(tup2[0])
# print(tup2[1])
# print(tup2[2])
# print(tup2[3])
# print(tup2[4])
# print(tup2[-1])
# print(tup2[5]) #error



if 342 in tup2:
    print("Yes 342 present!");
    
else:
    print("Not present!");

tup3=tup2[1:4];
print(tup3);





