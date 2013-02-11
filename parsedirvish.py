#!/usr/bin/python

import sys

config = {}

with open('/etc/dirvish/master.conf') as f:
    key = None
    val = None
    for line in f:
        if line.lstrip().startswith('#'): continue
        if not line.strip(): continue
        #print repr(line)
        #print "key:", key, "val:", val

        if key and (line.startswith(' ') or line.startswith('\t')):
            #print 'item in a list for', key
            # item in a list
            # eg '    /srv/backup'
            val.append(line.strip())
        elif line.strip().split(':', 1)[1]:
            #print 'single item param'
            # single item parameter
            # eg 'image-temp: current'
            if key:
                config[key] = val
            key = line.strip().split(':', 1)[0]
            val = line.strip().split(':', 1)[1].lstrip()
            config[key] = val
        elif not line.strip().split(':', 1)[1]:
            #print 'value'
            if key:
                config[key] = val
            key = line.strip().rstrip(':')
            val = []

if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
    print "usage: %s <key>" % sys.argv[0]
    sys.exit(1)

if sys.argv[1] in config:
    if isinstance(config[sys.argv[1]], list):
        for item in config[sys.argv[1]]:
            print item
    else:
        print config[sys.argv[1]]
else:
    sys.exit(1)

