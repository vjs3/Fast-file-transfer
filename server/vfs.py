#!/usr/bin/python
import sys,subprocess,os
if len(sys.argv) != 5:
    print "Invalid Argument!!\n"
    sys.exit(-1)
else:
    if not os.path.exists(sys.argv[4]):
        os.makedirs(sys.argv[4])
    f = open(sys.argv[1],"w")
    if sys.argv[3] =="b":
        size = float(sys.argv[2])
    elif sys.argv[3] == "kb":
        size = float(sys.argv[2]) * 1000
    elif sys.argv[3] == "mb":
        size = float(sys.argv[2]) * 1000000
    else:
        print "Wrong block type!! \n"
        print "Supported block are : \n1. Bytes identified here as 'b'"
        print "\n2. KiloBytes identified here as 'kb'"
        print "\n3. MegaBytes identified here as 'mb'"
        sys.exit(1)
    f.seek(size)
    f.write("\0")
    f.close()
    mkfs = "mkfs -t ext3 -q " + sys.argv[1]
    subprocess.check_call(mkfs, shell = True)
    x=0
    while True:
        freeloop = "loop" + str(x)
        check = "grep -c '" + freeloop + "' /proc/mounts"
        down = subprocess.call(check, shell = True)
        if down == 1:
            break
        else:
            x = x + 1
    mount = "mount -o loop=/dev/" + freeloop + " " + sys.argv[1] + " " + sys.argv[4]  
    flag = subprocess.check_call(mount, shell = True)
    if flag == 0:
        print "Virtual device " + sys.argv[1] + " created successfully at " + sys.argv[4] + "!!\n"
        print "Details about the created file system !!\n"
        subprocess.check_call('df -hT ' + sys.argv[4],shell = True)
    else:
        print "Failed!!"; 