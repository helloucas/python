__author__ = 'jmq'

def shout(word='yes'):
    return  word.capitalize()+"!"

print shout()
# outputs yes!

"""
as  an object you can assign the function to a variable like any other object

"""

scream=shout()

print(scream)


del  shout
try:
    print shout()
except  NameError,e:
    print e
print scream
