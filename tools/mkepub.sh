#!/bin/bash

CWD=`pwd`

TMP=`mktemp -d /tmp/CCCFG.XXXXXXXX`

pushd ${TMP}

git clone https://github.com/VeryGoodErotica/ContraCostaCountyFieldGuide.git

cd ContraCostaCountyFieldGuide/TheBook/OEBPS
python3 ../../tools/updateTimestamp.py content.opf
cd fonts
rm -f .gitignore
cp -p /usr/local/ePubFonts/*.ttf .
cd ../..

echo -n application/epub+zip >mimetype

zip -r -X Book.zip mimetype META-INF OEBPS
mv Book.zip ContraCostaCountyFieldGuide.epub


sh ../tools/epubcheck.sh ContraCostaCountyFieldGuide.epub

if hash ace 2>/dev/null; then
  ace -f -s -o AceReport ContraCostaCountyFieldGuide.epub
  echo "Accessibility report written to AceReport directory"
  echo `pwd`
fi


mv ContraCostaCountyFieldGuide.epub ${CWD}/

popd

#rm -rf ${TMP}



# run accessibility check if available
#if hash ace 2>/dev/null; then
#  ace -f -s -o AceReport yourBook.epub
#  echo "Accessibility report written to AceReport directory"
#fi
