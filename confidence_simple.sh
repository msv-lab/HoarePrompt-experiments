#!/bin/bash

./test_confidence.sh apps 2 default_config.json 
./test_confidence.sh apps 1 default_config_4_mini.json 
./test_confidence.sh mbpp 1 default_config.json 
./test_confidence.sh mbpp 1 default_config_4_mini.json 