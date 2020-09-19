#!/bin/bash

docker run \
    -it --rm \
    -v "$(pwd):/root/avocado-buffer" \
    -w /root/avocado-buffer \
    python \
    bash -c 'pip install avocado-framework aexpect &>/dev/null ; ./run.sh'
