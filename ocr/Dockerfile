FROM ubuntu:16.04

MAINTAINER Ben Willett "benw@techcamp.com.au"

RUN apt-get update -y && \
	apt-get install -y apt-utils && \
	apt-get install -y autoconf automake libtool && \
	apt-get install -y libpng12-dev && \
	apt-get install -y libjpeg62-dev && \
	apt-get install -y g++ && \
	apt-get install -y libtiff4-dev && \
	apt-get install -y libopencv-dev libtesseract-dev && \
	apt-get install -y git && \
	apt-get install -y cmake && \
	apt-get install -y build-essential && \
	apt-get install -y libleptonica-dev && \
	apt-get install -y liblog4cplus-dev && \
	apt-get install -y libcurl3-dev && \
	apt-get install -y python2.7-dev && \
	apt-get install -y tk8.5 tcl8.5 tk8.5-dev tcl8.5-dev && \
	apt-get build-dep python-imaging --fix-missing