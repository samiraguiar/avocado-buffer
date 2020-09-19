#!/bin/bash

readonly results_dir=$(avocado config | grep datadir.paths.logs_dir | awk '{ print $2 }')

echo "=> Running avocado"
python -m avocado run /root/avocado-buffer/test.py &>/dev/null &
pid=$!

echo "=> Tailing log until avocado ends"
tail --pid=$pid -F --retry "${results_dir}/latest/job.log" 2>/dev/null | grep "\[logme\]"
echo "=> Done"
