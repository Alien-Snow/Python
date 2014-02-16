import sys
import getopt
from PriorityQ import PriorityQ

class Usage(Exception) :
    def __init__(self, msg) :
        self.msg = msg

def main(argv = None) :
    if argv is None :
        argv = sys.argv
    try :
        try :
            opts, args = getopt.getopt(argv[1: ], "h", ["help"])
        except getopt.error, msg :
            raise Usage(msg)
        # Driver goes here
        data = ' '
        input = PriorityQ()
        print 'To quit press <Enter key>'
        while data != '' :
            print '\nEnter in a string followed by a positive number.\'Bob 2\'\n'
            data = sys.stdin.readline()
            if data == '\n' :
                return 0
            temp = data.split()
            my = {"name": temp[0], "priority": temp[1]}
            input.push(my)
            out = [e["name"] for e in input.q]
            i = 0
            print '\n'
            while i < len(out) :
                print out[i]
                i += 1
    except Usage, err :
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__" :
    sys.exit(main())
