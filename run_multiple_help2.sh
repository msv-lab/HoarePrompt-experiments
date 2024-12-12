#!/bin/bash

# ./test.sh apps_new 1 default_config_4_mini.json # done ektos apo  missing
# ./test.sh apps 1 default_config_llama.json
# ./test.sh apps 1 default_config.json
# ./test.sh apps 2 default_config.json
# ./test.sh apps 3 default_config.json
# sleep 60
# ./test.sh apps 4 default_config.json
# ./test.sh apps 5 default_config.json
# sleep 60
# # ./test.sh apps 3 default_config.json
# ./test.sh apps 1 default_config_4_mini.json
# ./test.sh apps 2 default_config_4_mini.json
# ./test2.sh
# ./test.sh apps 3 default_config_4_mini.json
# sleep 60
# ./test.sh apps 4 default_config_4_mini.json
# ./test.sh apps 5 default_config_4_mini.json

#  ./test.sh mbpp 1 default_config_4_mini.json # done ektos apo  missing

# ./test.sh mbpp 1 default_config.json

#  ./test.sh mbpp 2 default_config_4_mini.json # done ektos apo  missing

# ./test.sh mbpp 2 default_config.json
#  ./test.sh mbpp 3 default_config_4_mini.json # done ektos apo  missing

# ./test.sh mbpp 3 default_config.json

# # ./test.sh mbpp 1 default_config_llama.json
# ./test_fast.sh apps 1 default_config_4_mini.json
# ./test_fast.sh apps 2 default_config_4_mini.json
# ./test_fast.sh apps 3 default_config_4_mini.json
# ./test_fast.sh apps 4 default_config_4_mini.json
# ./test_fast.sh apps 5 default_config_4_mini.json


!/bin/bash

# Start both commands in the background
./test_confidence.sh mbpp 1 default_config_4_mini.json &
PID1=$!
./test_confidence.sh mbpp 1 default_config_llama.json &
PID2=$!
./test_confidence.sh mbpp 1 default_config_qwen.json &
PID3=$!

# # Set up trap to kill both processes if Ctrl+C is pressed
trap "kill $PID1 $PID2 $PID3; exit" SIGINT

# # Wait for both processes to finish
wait $PID1
wait $PID2
wait $PID3

# ./test_fast.sh mbpp 2 default_config.json
# ./test_fast.sh mbpp 3 default_config.json
# ./test_fast.sh mbpp 4 default_config.json
# ./test_fast.sh mbpp 5 default_config.json