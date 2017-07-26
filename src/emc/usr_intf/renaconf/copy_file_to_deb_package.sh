#!/bin/bash
D=deb_package
cp *.glade ${D}/usr/share/linuxcnc/renaconf
cp renaconf.py ${D}//usr/bin/renaconf
#cp *.py ${D}//usr/lib/pymodules/python2.7/renaconf/
cp *.py ${D}//usr/share/pyshared/renaconf/
