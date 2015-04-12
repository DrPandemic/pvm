#!/bin/sh

PVM=/tmp/pvm/$LOGNAME/$RANDOM/bin
if [ ! -d "$PVM" ]; then
    mkdir -p $PVM
fi

if [[ ":$PATH:" != *":$PVM:"* ]]; then
    export PATH=$PVM:$PATH
    pvm init
    hash -r
fi

export PVM=$PVM