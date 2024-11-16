#!/bin/bash

# ./test.sh apps_new 1 default_config_4_mini.json # done ektos apo  missing
# ./test.sh apps 1 default_config_llama.json
# ./test.sh apps 1 default_config.json
# ./test.sh apps 2 default_config.json
# ./test.sh apps 3 default_config.json
# sleep 60
# ./test.sh apps 4 default_config.json
./test.sh apps 5 default_config.json
sleep 60
# ./test.sh apps 3 default_config.json
./test.sh apps 1 default_config_4_mini.json
./test.sh apps 2 default_config_4_mini.json
./test.sh apps 3 default_config_4_mini.json
# sleep 60
# ./test.sh apps 4 default_config_4_mini.json
# ./test.sh apps 5 default_config_4_mini.json

#  ./test.sh mbpp 1 default_config_4_mini.json # done ektos apo  missing

# ./test.sh mbpp 2 default_config.json

# ./test.sh mbpp 1 default_config_llama.json