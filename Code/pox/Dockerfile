FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3 python3-pip mininet openvswitch-switch \
    && apt-get install -y git\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y iproute2
RUN git clone 'https://github.com/noxrepo/pox.git'
WORKDIR /pox
EXPOSE 6634
COPY . /pox

COPY fichier.py /pox/pox/forwarding/fichier.py
CMD ["./pox.py","of_tutorial","openflow.spanning_tree","openflow.discovery","openflow.of_01","--address=192.168.12.25","--port=6634","forwarding.l2_learning"]
#CMD ["./pox.py","forwarding.fichier"]

ENTRYPOINT ["sh"]
