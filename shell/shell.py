
import os, sys, re
from myReadline import myReadlines

while(1):
    os.write(1, "$ ".encode())
    ibuf = myReadlines()

    if len(ibuf) == 0 or ibuf.lower() == "exit":     # No characters left in read
        os.write(2, "Shell exited!\n".encode())
        sys.exit(1)

    lines = ibuf.split()  # tokenize user input
    rc = os.fork()        

    if rc < 0:
        os.write(2, ("Fork failed, returning.. %d\n" % rc).encode()) 
        sys.exit(1)

    elif rc == 0:
        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir, lines[0])
            try:
                os.execve(program, lines, os.environ) # attempt to execute program
            except FileNotFoundError:
                pass
        os.write(2, ("Command failed\n").encode())
        sys.exit(1)

    else:
        childPidCode = os.wait() # parent waits for child
