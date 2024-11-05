#!/bin/bash

# Define the base path for the data and log directories
DATA_DIR="/home/jim/HoarePrompt-data/PilotData/data"
LOG_DIR="/home/jim/HoarePrompt-data/Results/pilot"

# Array of data files to process
data_files=("pilot_mbpp1.json" "pilot_mbpp2.json","pilot_mbpp3.json" "pilot_mbpp4.json" "pilot_mbpp5.json")
echo "Processing ${#data_files[@]} data files..."
# Loop over each data file and run the command
for data_file in "${data_files[@]}"; do
    echo "Processing $data_file..."
    python3 -m src.main --data "$DATA_DIR/$data_file" --log "$LOG_DIR"
done
