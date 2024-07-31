FROM public.ecr.aws/amazonlinux/amazonlinux:2

RUN yum -y install python37
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
WORKDIR /deploy
RUN yum -y install tar
RUN yum -y install xz
RUN curl https://nodejs.org/dist/v16.14.2/node-v16.14.2-linux-x64.tar.xz | tar -xJf -
ENV PATH="/deploy/node-v16.14.2-linux-x64/bin:${PATH}"
RUN npm install -g aws-cdk
COPY requirements.txt ./
RUN yes | pip --no-cache install -r requirements.txt
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN yum -y install unzip
RUN unzip awscliv2.zip
RUN ./aws/install

COPY . /deploy/
ENV LANG=C.UTF-8
WORKDIR /deploy
CMD [ "/bin/bash" ]