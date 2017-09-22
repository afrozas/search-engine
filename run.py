import textract, re
txt = textract.process("BITS.pdf") # returns byte text

txt = txt.decode() # converts bytes to string
				   # printing here leads to non-printable characters also being displayed
txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '',txt)	# removes escape characters using regex
txt = txt.encode('ascii','ignore') # removes unicode characters like \u0097 and type(txt) is bytes
txt = txt.decode('unicode_escape') # conversion to desired string 

print(' '.join(txt.split()))

""" ISSUES:
-> in .doc files, pipes are being extracted from table borders.
"""

""" Installing textract:
$ sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig

$ sudo apt-get install build-essential autoconf libtool pkg-config python-opengl libpulse-dev python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev

$ sudo apt-get install libpulse-dev

$ sudo pip3 install textract

"""
