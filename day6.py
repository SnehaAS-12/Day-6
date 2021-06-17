dict= {"a": 10, "b": 20}
dict1 = {"c": 30, "d": 40}
d = dict.copy()
d.update(dict1)
print(d)


Dict = {"a":0,"b":1,"c":2,"d":3,"e":4}
if 'a' in Dict: 
    del Dict["b"]
print(Dict)


chocolates = ["cadbury","5 star","dark chocolate",]
values = ["00","01","02",]
d1 = {chocolates[i]: values[i] for i in range(len(chocolates))}
print("After mapping lists to dictionary:",d1)


s = len({0,1, 2, 3, 4, 5}) 
print("The length of set is:", s) 


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print("After removing the intersection of a 2nd set from the 1st :")
s1.difference_update(s2)
print("s1: ",s1)
print("s2: ",s2)