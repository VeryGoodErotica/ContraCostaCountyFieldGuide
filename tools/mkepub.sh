#!/bin/bash

CWD=`pwd`

TMP=`mktemp -d /tmp/CCCFG.XXXXXXXX`

pushd ${TMP}

git clone https://github.com/VeryGoodErotica/ContraCostaCountyFieldGuide.git

cd ContraCostaCountyFieldGuide/TheBook/OEBPS
python3 ../../tools/updateTimestamp.py content.opf
cd ..

echo -n application/epub+zip >mimetype

zip -r -X youBook.zip mimetype META-INF EPUB

sh ../tools/epubcheck.sh yourBook.epub


mv yourBook.epub ${CWD}/

popd

# rm -rf ${TMP}



[ ! -d EPUB ] && exit 1

# run accessibility check if available
#if hash ace 2>/dev/null; then
#  ace -f -s -o AceReport yourBook.epub
#  echo "Accessibility report written to AceReport directory"
#fi
