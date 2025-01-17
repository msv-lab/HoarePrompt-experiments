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



# python3 -m src.main_verify --config default_config_4_mini.json --data /home/dimitris/HoarePrompt-data/PilotData/data/selected_pilot_75_apps_4mini_temp.json  --log /home/dimitris/HoarePrompt-data/Results/Pilot_new12/apps_4_mini_2
# python3 -m src.main_verify --config default_config_llama.json  --data /home/dimitris/HoarePrompt-data/PilotData/data/selected_pilot_75_apps_llama_temp.json --log  /home/dimitris/HoarePrompt-data/Results/Pilot_new12/apps_llama_3
# Start both commands in the background
# ./test_verify.sh mbpp 2 default_config_4_mini.json 

# ./test_verify.sh mbpp 2 default_config_llama.json 

# ./test_verify.sh mbpp 2 default_config_qwen72.json 

# ./test_verify.sh mbpp 3 default_config_4_mini.json 

# ./test_verify.sh mbpp 3 default_config_llama.json 

# # ./test_verify.sh mbpp 3 default_config_qwen.json 


# # python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen.json --data /home/dimitris/HoarePrompt-data/PilotData/data/code_contests_first1000_under09.json --log /home/dimitris/HoarePrompt-data//Results/Pilot_code_contests_qwen1_lowconfidence_2
# python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen.json --data /home/dimitris/HoarePrompt-data/PilotData/data/code_contests_first1000_under09.json --log /home/dimitris/HoarePrompt-data//Results/Pilot_code_contests_qwen1_lowconfidence_3

# # /home/dimitris/HoarePrompt-data/PilotData/data/selected_pilot_75_apps_4mini_temp.json
# # # Set up trap to kill both processes if Ctrl+C is pressed
# # trap "kill $PI1 $PID2 $PID3; exit" SIGINT

# # # Wait for both processes to finish
# wait $PID1
# wait $PID2
# wait $PID3

# ./test_fast.sh mbpp 2 default_config.json
# ./test_fast.sh mbpp 3 default_config.json
# ./test_fast.sh mbpp 4 default_config.json
# ./test_fast.sh mbpp 5 default_config.json

python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen.json --data /home/dimitris/HoarePrompt-data/PilotData/data/apps_total_cleaned_low_qwen7.json --log /home/dimitris/HoarePrompt-data/Results/apps_new_low_qwen7  --run_number 1
python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen.json --data /home/dimitris/HoarePrompt-data/PilotData/data/apps_total_cleaned_low_qwen7.json --log /home/dimitris/HoarePrompt-data/Results/apps_new_low_qwen7  --run_number 2
python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen.json --data /home/dimitris/HoarePrompt-data/PilotData/data/apps_total_cleaned_low_qwen7.json --log /home/dimitris/HoarePrompt-data/Results/apps_new_low_qwen7  --run_number 3
python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen72.json --data /home/dimitris/HoarePrompt-data/PilotData/data/apps_total_cleaned_low_qwen72.json --log /home/dimitris/HoarePrompt-data/Results/apps_new_low_qw  --run_number 1

python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen.json --data /home/dimitris/HoarePrompt-data/PilotData/data/mbpp_total_cleaned_low_qwen7.json --log /home/dimitris/HoarePrompt-data/Results/mbpp_new_low_qwen7  --run_number 1
python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen.json --data /home/dimitris/HoarePrompt-data/PilotData/data/mbpp_total_cleaned_low_qwen7.json --log /home/dimitris/HoarePrompt-data/Results/mbpp_new_low_qwen7  --run_number 2
python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen.json --data /home/dimitris/HoarePrompt-data/PilotData/data/mbpp_total_cleaned_low_qwen7.json --log /home/dimitris/HoarePrompt-data/Results/mbpp_new_low_qwen7  --run_number 3

python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen72.json --data /home/dimitris/HoarePrompt-data/PilotData/data/mbpp_total_cleaned_low_qwen72.json --log /home/dimitris/HoarePrompt-data/Results/mbpp_new_low_qwen72  --run_number 1
python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen72.json --data /home/dimitris/HoarePrompt-data/PilotData/data/mbpp_total_cleaned_low_qwen72.json --log /home/dimitris/HoarePrompt-data/Results/mbpp_new_low_qwen72  --run_number 2
python3 -m src.main_verify --config /home/dimitris/HoarePrompt-experiments/default_config_qwen72.json --data /home/dimitris/HoarePrompt-data/PilotData/data/mbpp_total_cleaned_low_qwen72.json --log /home/dimitris/HoarePrompt-data/Results/mbpp_new_low_qwen72  --run_number 3


