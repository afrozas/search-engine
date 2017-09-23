## Search Engine for Course Management Systems

Search engine built from scratch for searching resources( Powerpoint presentations, PDFs, Word documents, etc) for different courses on BITS Course Management System.

This repo uses python3.5 as textract library is not available for python2.7 .
Install all the other dependencies using pip3.

### Installation:

Run the follwing in terminal.
```
$ sudo pip install -r requirements.txt
```
If you face any problem, install `textract` and `nltk` separately.

#### Installing `textract`

```
$ sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev

$ sudo pip3 install textract
```

#### Installing `nltk`

```
$ pip3 install nltk
$ python3
>>> import nltk
>>> nltk.download()
	[Press 'd' for download]
	Download() d

	Packages: all
```

### Issues:
- In .doc files, pipes are being extracted from table borders.
- .ppt is not currently supported by textract, hence unoconv is to be used for .ppt files specifically