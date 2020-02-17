#!/usr/bin/env python3
import sys
import os
import hashlib
import pathlib
from shutil import copyfile

# This does NOT generate a standard UUID. Specifically, the UUID version and UUID variant are
#  meaningless as this just produces a 128-bit number with the dashes in the same place as UUID.
#
# A SHA-384 hash is taken of the resource. From that SHA-384 hash, a md5sum hash is taken, and
#  the hex digest of the md5sum is used as the output.
#
# Before initial publication, I *may* (read probably) update this script to generate an actual
#  valid UUID for the filename, as well as a skeleton metadata XML file.

# takes md5sum of sha384sum and formats it for UUID
def getResourceUUID(input):
    BS = 65536
    hasher = hashlib.sha384()
    mdhasher = hashlib.md5()
    orig = pathlib.Path(input)
    with open(orig,'rb') as myresource:
        buf = myresource.read(BS)
        while len(buf) > 0:
            hasher.update(buf)
            buf = myresource.read(BS)
    mdhasher.update(hasher.digest())
    myhash = mdhasher.hexdigest()
    return(myhash[0:8] + "-" + myhash[8:12] + "-" + myhash[12:16] + "-" + myhash[16:20] + "-" + myhash[20:32])

def showUsage():
    print ("Usage: " + sys.argv[0] + " path/to/resource.ext")
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        showUsage()
    myUUID = getResourceUUID(sys.argv[1])
    origname, extension = os.path.splitext(sys.argv[1])
    myFilename = myUUID + extension
    if os.path.exists(myFilename):
        print("The file " + myFilename + " already exist. Doing nothing.")
        sys.exit(1)
    copyfile(sys.argv[1], myFilename)
    print("The file " + myFilename + " has been created.")
    sys.exit(0)

if __name__ == "__main__":
	main()
