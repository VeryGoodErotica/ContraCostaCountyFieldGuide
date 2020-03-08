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
  if [ ! -f ${CWD}/AceReport/noace.tmp ]; then
    ace -f -s -o AceReport ContraCostaCountyFieldGuide.epub
    rm -rf ${CWD}/AceReport/data
    [ ! -d ${CWD}/AceReport ] && mkdir ${CWD}/AceReport
    mv AceReport/data ${CWD}/AceReport/
    mv AceReport/report.html ${CWD}/AceReport/
    mv AceReport/report.json ${CWD}/AceReport/
    echo "Accessibility report written to AceReport directory"
    echo `pwd`
  fi
fi


mv ContraCostaCountyFieldGuide.epub ${CWD}/

popd

if hash ace 2>/dev/null; then
  if [ -f AceReport/.gitignore ]; then
    if [ ! -f AceReport/noace.tmp ]; then
      git commit -m "update AceReport" AceReport/report.*
    fi
  fi
fi

#rm -rf ${TMP}



# run accessibility check if available
#if hash ace 2>/dev/null; then
#  ace -f -s -o AceReport yourBook.epub
#  echo "Accessibility report written to AceReport directory"
#fi
