#declaring dict
# d={}
# for i in range(3):
#      key=input()
#      val=input()
#      d[key]=val
# print(d)



# d={404:"Error",220:"Success"}
# d1=d.copy()
# d.update({404:"No Signal","A":"Apple"})
# print(d1)


#pop method
# d={1:"a",2:"b",3:"c"}
# d.popitem()
# print(d)

# #fromkeys
# d={'a','b','c','d'}
# d=dict.fromkeys(d,10)
# print(d)


#clear
# d={1:'hi','a':123,100:32.4}
# d.clear()
# print(d)


#setDefault
d={1:'hi','a':123,100:32.4}
print(d.setDefault('a'))
print(d.setDefault('b'))
print(d)
print(d.setDefault('c',200))
print(d)

