#!/bin/bash

# Check if both arguments are provided
if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ]; then
    echo "Usage: $0 <name> <time> <config file> <dataset path>"
    exit 1
fi

# Get the input arguments as variables
dataset=$1
time=$2

CONFIG=$3
dataset_path=$4
#if config contains the word llamathen make variable model llama
if [[ $CONFIG == *"llama"* ]]; then
    model="llama"
#if it contains the word bert then make variable model bert
elif [[ $CONFIG == *"4_mini"* ]]; then
    model="4_mini"
elif [[ $CONFIG == *"4o"* ]]; then
    model="4o"
else 
    model="3point5"
fi
INPUT="${dataset}_${model}_${time}"
# Define the base path for the data and log directories
# DATA_DIR="/home/jim/HoarePrompt-data/PilotData/data" # here is where you will find the dataset
LOG_DIR="/home/jim/HoarePrompt-data/Results/Pilot_reruns/$INPUT"  #here is where you will store the results

# Create the log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# # Array of data files to process, using correct syntax for variable expansion
# data_files=("${DATA_DIR}/pilot_${dataset}1.json" "${DATA_DIR}/pilot_${dataset}2.json" "${DATA_DIR}/pilot_${dataset}3.json" "${DATA_DIR}/pilot_${dataset}4.json" "${DATA_DIR}/pilot_${dataset}5.json")

# # Inform the user of the number of files being processed
# echo "Processing ${#data_files[@]} data files..."

# Loop over each data file and run the command
# for data_file in "${data_files[@]}"; do
echo "Processing $dataset_path..."
python3 -m src.main --config "$CONFIG" --data "$dataset_path" --log "$LOG_DIR"
if [ $? -ne 0 ]; then
    echo "Error processing $dataset_path. Exiting."
    exit 1
fi
# done

echo "All files processed successfully. Logs saved in $LOG_DIR."
