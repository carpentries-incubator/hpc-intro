#!/usr/bin/env bash
if [ $# -eq 0 ]
  then
    echo "No cluster name supplied, please give one argument!"
fi
sed -i s/custom/$1/g _config_options.yml 
sed -i s/custom/$1/g scheduler/runtime-exceeded-output.snip
