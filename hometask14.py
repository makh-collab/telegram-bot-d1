   #! Mix
   
#  #1
# keys=['Ten', 'Twenty', 'Thisrty']
# values=[10, 20, 30]
# c={}
# c=dict(zip(keys, values))
# print(c)
#   #1.2
# keys=['Ten', 'Twenty', 'Thisrty']
# values=[10, 20, 30]
# c={}
# for i in range(len(keys)):
#     c.update({keys[i]:values[i]})
# print(c)

#   #2
# dict1={'ten':10, 'twenty':20, 'thirty':30}
# dict2={'thirty':30, 'fourty':40, 'fifty':50}
# dict1.update(dict2)
# print(dict1)

#   #3
# sampleDict = { 
# "class": { 
# "student": { 
# "name": "Mike", 
# "marks": { 
# "physics": 70, 
# "history": 80 
# } 
# } 
# } 
# } 
# print(sampleDict["class"]['student']["marks"]['history'])   #.keys()

#   #4
# sample={'name':'Kelly', 'age':25, 'salary':8000, 'city':"New York"}
# c={}
# for i in sample:
#     if i=='name' or i=='salary':
#         c.update({i:sample[i]}) 
# print(c)  

#   #5
# sd={'a':100, 'b':200, 'c':300}
# if 200 in sd.values():
#     print('Dictda 200 ta mavjud')
# else:
#     print('Dictda 200 ta mavjud emas')
    
#   #6
# sd={'name':'Kelly',"age":25, "salary": 8000, "city": "New york"}

#   #7
# sd={'emp1':{'name': 'Jhon', 'salary': 7500}, 'emp2':{'name': 'Emma', 'salary': 8000}, 'emp3':{'name': 'Brad', 'salary': 500}}         
# for i in sd.values():
#     for j in i.values():
#         # print(j)
#         if j == "Brad":
#             i['salary'] = 8500
# print(sd)

#   #8
# l1=['M', 'na', 'i', 'Ke']
# l2=['y', 'me', 's', 'lly']
# sd=[]
# for i in range(len(l1)):
#   res=l1[i]+l2[i]
#   sd.append(res)
# print(sd)

#   #9
# l1=[10, 20, 30, 40]
# l2=[100, 200, 300, 400]
# rl=l2[::-1]
# for i in range(len(l1)):
#   print(l1[i], rl[i])
  
#   #10.1
# l1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
# sl= ["h", "i", "j"] 
# for i in l1:
#   if type(i)==list:
#     for j in i:
#       if type(j)==list:
#         for o in j:
#           if type(o)==list:
#             o.append(sl)    
#             print(l1)

#   #10.2
# l1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
# sl=["h", "i", "j"] 
# l1[2][1][2].extend(sl)
# print(l1)

  #11
l1=[5, 10, 15, 20, 25, 50, 20]
for i in l1:
  if i==20:
     i=200
print(l1)