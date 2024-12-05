FROM ubuntu:latest
RUN apt-get update \
    && apt-get install -y python3 python3-pip openvswitch-switch iproute2 \
    && apt-get clean \
    && apt-get install iputils-ping -y \
    && rm -rf /var/lib/apt/lists/*
ENV PIP_BREAK_SYSTEM_PACKAGES 1
RUN pip3 install scapy
COPY requirements.txt requirements.txt
#COPY topologie_reseau_mininet.py topologie_reseau_mininet.py
#COPY poison_h2.py poison_h2.py
RUN service openvswitch-switch start

EXPOSE 6634
ENTRYPOINT ["sh"]
