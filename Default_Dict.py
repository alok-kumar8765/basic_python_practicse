'''
This default dict never rises keyerror, let suppose we are using for loop and quickly adding print(c.most_common())resent in dic
in this condition this defalut dict very much help full it will assign defalut value when there is some how key is not present
'''
from collections import defaultdict
d =defaultdict(lambda:0)
d['correct'] = 100
print(d['wrong']) #Notice it will show 0 as Default value

#Example 2
# Defining the dict and passing 
# lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])

#Same example with normal function
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])