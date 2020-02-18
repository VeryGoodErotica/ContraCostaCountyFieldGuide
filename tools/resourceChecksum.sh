#!/bin/bash

# not finished - needs to verify resources without a checksum
#  against the filename
#

if [ ! -f resources.sha256 ]; then
  echo "Please run me from within the OriginalResources directory."
  exit 1
fi

find . -print |grep "~$" |while read file; do
  rm -f $file
done

sha256sum -c resources.sha256

if [ $? -ne 0 ]; then
  echo "checking existing resources failed"
  exit 1
fi

sha256sum * |grep -v "\.xml$" |grep -v "\.md$" |grep -v "\.sha256$" \
> resources.sha256

sleep 2

sha256sum -c resources.sha256

