#!/bin/bash

# Check if both arguments are provided
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <dataset> <time>"
    exit 1
fi

# Get the input arguments as variables
dataset=$1
time=$2
INPUT="${dataset}_${time}"

# Define the base path for the data and log directories
DATA_DIR="/home/jim/HoarePrompt-data/PilotData/data"
LOG_DIR="/home/jim/HoarePrompt-data/Results/$INPUT"

# Create the log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Array of data files to process, using correct syntax for variable expansion
data_files=("${DATA_DIR}/pilot_${dataset}1.json" "${DATA_DIR}/pilot_${dataset}2.json" "${DATA_DIR}/pilot_${dataset}3.json" "${DATA_DIR}/pilot_${dataset}4.json" "${DATA_DIR}/pilot_${dataset}5.json")

# Inform the user of the number of files being processed
echo "Processing ${#data_files[@]} data files..."

# Loop over each data file and run the command
for data_file in "${data_files[@]}"; do
    echo "Processing $data_file..."
    python3 -m src.main --data "$data_file" --log "$LOG_DIR"
    if [ $? -ne 0 ]; then
        echo "Error processing $data_file. Exiting."
        exit 1
    fi
done

echo "All files processed successfully. Logs saved in $LOG_DIR."
