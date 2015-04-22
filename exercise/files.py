import sys
import time

#from optparse import OptionParser
#parser = OptionParser()
#(opts, args) = parser.parse_args()

'''
Implement Unix Tail command
'''
def tail_file(myfile):

    while True:
        current = myfile.tell()
        line = myfile.readline()
        if not line:
            time.sleep(1)
            myfile.seek(current)
        else:
            yield line

with open(sys.argv[1]) as myfile:
    
    for line in tail_file(myfile):
        sys.stdout.write(line)


