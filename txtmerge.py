#!/usr/bin/env python
# usage: txtmerge.py <input_dir> <output_file_name> 
# does the exact opposite of txtsplit.py

import os
import sys
import re
import io 

assert len(sys.argv) == 3, "usage:\ntxtmerge.py <input_dir> <output_file_name>"
idir = str(sys.argv[1])
oname = str(sys.argv[2])


ofile = io.open(oname, 'w', encoding='utf-16', newline='\r\n')

for location in os.listdir(idir):
   
    try:
        ifile = io.open(os.path.join(idir, location), 'rt', encoding='utf-8')
        text = ifile.read()

        # make sure there's a line at the end of file
        # (why wouldn't there be one? WINDOWS!
        if text[-1] != u'\n':
            text += u'\n\n'

        ofile.write(text)
        ifile.close()
    except IOError:
        print("WARNING: missing location %s" % location)
        pass
    except:
        print("error in file %s" % location)
        pass

ofile.close()
    
        
