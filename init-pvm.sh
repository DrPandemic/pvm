#!/bin/sh

PVM=/tmp/pvm-$LOGNAME/bin
if [ ! -d "$PVM" ]; then
    mkdir -p $PVM
fi

if [[ ":$PATH:" != *":$PVM:"* ]]; then
    export PATH=$PVM:$PATH
fi

export PVM=$PVM