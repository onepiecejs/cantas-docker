FROM fedora:20
MAINTAINER qcxhome@gmail.com

RUN yum install -y git make nodejs krb5-devel gcc gcc-c++ npm bzip2 && yum clean all
RUN git clone https://github.com/onepiecejs/nodejs-cantas.git
RUN cd nodejs-cantas && npm install --production

ADD ./entrypoint /

EXPOSE 3000

WORKDIR /nodejs-cantas
ENTRYPOINT ["../entrypoint"]
