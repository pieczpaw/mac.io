FROM centos
MAINTAINER Pawel Pieczkowski "p.pieczkowski@gmail.com"
LABEL version="1.0"
LABEL description="Pawel Pieczkowski PoC"
RUN dnf -y install python3
RUN pip3 install requests
RUN dnf -y install git
RUN cd /
RUN git clone https://github.com/pieczpaw/mac.io.git
CMD /bin/bash

