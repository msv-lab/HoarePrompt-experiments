#!/bin/bash
DATA_DIR="/home/jim/HoarePrompt-data/PilotData/data/pilot_apps5.json"
LOG_DIR="/home/jim/HoarePrompt-data/Results/Pilot_new1/4mini_2_apps_completion"
CONFIG=default_config_4_mini.json
python3 -m src.main --config "$CONFIG" --data "$DATA_DIR" --log "$LOG_DIR"
# Get the input arguments as variables

