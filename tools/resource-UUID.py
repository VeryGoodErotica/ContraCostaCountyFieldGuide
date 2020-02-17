#!/usr/bin/env python3
import sys
import os
import hashlib
import pathlib
from shutil import copyfile

# This script generates a UUID that validates as a Type 4 (random) UUID although the UUID that
#  is generates is actually not random.
#
# The first hex digit of the third field of a UUID specifies the version of UUID being used. For
#  a Type 4 UUID that will be the digit 4.
#
# The first hex digit of the fourth field of a UUID specifies the variant. With a Type 4 UUID
#  this typically is 8, 9, a, or b to indicate a variant 1 UUID however the values c, d, and e
#  are legal though they imply a variant 2 UUID.
#
# This script uses an 8 for the first hex digit of the fourth field but not to indicate a variant
#  but rather to indicate the generation method used was a SHA-384 checksum of the data file
#  followed by an MD5 checksum of the SHA-384.
#
# A hex digest of the MD5 checksum is then used as the UUID, replacing the 13th digit with a 4
#  and the 17th digit with an 8. And of course breaking the hex digest up into UUID like fields.
#
# If and when SHA-384 is suspected of being broken, a new hash algorithm can be used replacing
#  but using a 9 instead of an 8, and so on until e is used. I will probably be dead by then
#  so I will not care about what to do to generate a non-random UUID that looks like a Tyoe 4
#  random UUID but serves a validation purpose.
#
# The script copies the source file to a new file using the UUID plus the file extension of the
#  original file as the file name. This allows the integrity of the copied file to easily be
#  verified as the filename itself is generated in a repeatable method from the file data.
#
# Any change to the file data will result in a different UUID being generated from the file
#  data.
#
# TODO: properly validate the file was copied correctly and warn if a copying error was
#  detected.

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
    # 4 in third indicates random UUID even though this isn't one,
    # 8 in fourth indicates SHA-384 was used for the hash of the file.
    # Thus a UUID is produced that would "validate" as a random UUID even though it isn't actually random.
    return(myhash[0:8] + "-" + myhash[8:12] + "-4" + myhash[13:16] + "-8" + myhash[17:20] + "-" + myhash[20:32])

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
