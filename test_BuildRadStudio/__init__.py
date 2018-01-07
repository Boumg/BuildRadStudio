#-*- coding: utf-8 -*-

print("---init test---")
import sys
for f in sys.path:
    print(f)
print ("file", __file__)
print ("__name__", __name__)
print ("__package__", __package__)
print ("__path__", __path__)



