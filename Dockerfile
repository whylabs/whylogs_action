FROM python:3.8-buster

COPY requirements.txt /

# Container image that runs your code
RUN python -m pip install --no-cache-dir -r requirements.txt

RUN python -m pip install whylogs==0.3.1

# Use these commands to run the latest whylogs directly from the github repo.
#RUN apt update && apt install -y protobuf-compiler
#
#RUN git clone https://github.com/whylabs/whylogs-python.git
#
#RUN cd whylogs-python && git submodule update --init --recursive
#
#RUN cd whylogs-python && pip install --no-cache-dir -r requirements-dev.txt
#
#RUN cd whylogs-python && make develop
# end development part

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /
COPY main.py /

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
