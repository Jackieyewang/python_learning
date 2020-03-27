import os
import pdb

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
# pdb.set_trace()
pid = os.fork()
# pdb.set_trace()

if pid == 0:
    # print(pid)
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

