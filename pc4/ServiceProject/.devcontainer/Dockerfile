FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install basic packages
RUN apt-get update && \
    apt-get install -y sudo vim git zip tree curl wget python3.10 python3.10-dev python3-pip && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 && \
    apt-get autoremove -y && \
    apt-get clean -y

# Create the user 'andre' and add to sudo group
ARG USERNAME=andre
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    && usermod -aG sudo $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

WORKDIR /project

RUN python3 -m pip install --upgrade pip && \
    pip3 install --upgrade wheel

ENV TERM=xterm-256color

EXPOSE 5000

USER $USERNAME
