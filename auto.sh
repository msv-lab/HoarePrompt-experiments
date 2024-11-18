#!/bin/bash

# 定义每组参数
commands=(
    "./test_yihan.sh code_contests 1 default_config_4_mini.json ./input_data/code_contests2.json"
    "./test_yihan.sh code_contests 1 default_config_4_mini.json ./input_data/code_contests3.json"
    "./test_yihan.sh code_contests 1 default_config_4_mini.json ./input_data/code_contests4.json"
    "./test_yihan.sh code_contests 1 default_config_4_mini.json ./input_data/code_contests5.json"
)

command2=(
    "./test_yihan.sh code_contests 2 default_config_3point5.json ./input_data/code_contests1.json"
    "./test_yihan.sh code_contests 2 default_config_3point5.json ./input_data/code_contests2.json"
    "./test_yihan.sh code_contests 2 default_config_3point5.json ./input_data/code_contests3.json"
    "./test_yihan.sh code_contests 2 default_config_3point5.json ./input_data/code_contests4.json"
    "./test_yihan.sh code_contests 2 default_config_3point5.json ./input_data/code_contests5.json"
)

# 循环执行每组命令
for cmd in "${commands[@]}"; do
    echo "正在运行: $cmd"
    $cmd
    if [ $? -ne 0 ]; then
        echo "命令执行失败: $cmd"
        exit 1
    fi
done

echo "所有命令已成功运行完毕！"