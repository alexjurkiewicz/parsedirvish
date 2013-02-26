parsedirvish
============

Parse dirvish's configuration file and return parameters so you can use them elsewhere.

Reasonably primitive, but Correct. Patches welcome.

Usage
=====

./parsedirvish.py <variable>

eg:
$ ./parsedirvish.py banks
/srv/backup
/srv2/backup
$ echo $?
0
$ ./parsedirvish.py foo
$ echo $?
0
$ rm /etc/dirvish/master.conf
$ ./parsedirvish.py banks
Couldn't parse config file! ([Errno 2] No such file or directory: '/etc/dirvish/master.conf')
$ echo $?
1
