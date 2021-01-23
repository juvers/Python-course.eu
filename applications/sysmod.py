#!/anaconda3/bin/python
import sys

#print(sys.version)
"""sys.argv is a list, which contains the command-line arguments 
    passed to the script. The first item of this list 
    contains the name of the script itself."""
for i in range(len(sys.argv)):
    if(i == 0):
        print ("Function Name: %s" % sys.argv[0])
    else: 
        print ("%d. argument: %s" % (i,sys.argv[i]))

x = 42
def my_display(x):
    print("Out:")
    print(x)

sys.displayhook = my_display
sys.displayhook(x)
