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
# python3 -m src.main_confidence_simple --config default_config_4_mini.json --data /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_mbpp_4mini_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot9/mbpp_4_mini_2
# python3 -m src.main_confidence_simple --config default_config_llama.json --data /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_mbpp_llama_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot9/mbpp_llama_2
# python3 -m src.main_confidence_simple --config default_config_qwen.json --data /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_mbpp_qwen_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot9/mbpp_4_qwen_2
# Start both commands in the background
# ./test_confidence.sh apps 1 default_config_4_mini.json &
python3 -m src.main_confidence_simple --config default_config_4_mini.json --data /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_mbpp_4mini_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot9/mbpp_4_mini_2 &
PID1=$!
# ./test_confidence.sh apps 1 default_config_llama.json &
python3 -m src.main_confidence_simple --config default_config_llama.json --data /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_mbpp_llama_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot9/mbpp_llama_2 &
PID2=$!
# ./test_confidence.sh apps 1 default_config_qwen.json &
python3 -m src.main_confidence_simple --config default_config_qwen.json --data /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_mbpp_qwen_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_confidence_simple_pilot9/mbpp_4_qwen_2 &
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
 python3 -m src.main_verify --config default_config_llama.json --data /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_apps_llama_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_new10/apps_llama_4
  python3 -m src.main_verify --config default_config_qwen.json --data  /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_apps_qwen_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_new10/apps_qwen_2
  puthon3 -m src.main_verify --config default_config_4_mini.json --data /home/jim/HoarePrompt-data/PilotData/data/selected_pilot_75_apps_4mini_temp.json --log /home/jim/HoarePrompt-data/Results/Pilot_new11/apps_4_mini_2