#!/bin/bash

for I in $(find . ) ; do
    DIR=$(dirname ${I})
    FILE=$(basename ${I})
    RES=$( echo ${I} | egrep -wo ".*\.zip")
    pushd ${DIR}
    if [ ! "${RES}" = "" ] ; then
        unzip ${FILE}
    fi
    popd
done
