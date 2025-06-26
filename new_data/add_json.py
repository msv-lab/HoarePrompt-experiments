import json
import os


def add_to_jsonl(num: int, alp: str, input_data: str, output_data: str) -> None:
    """
    向指定的jsonl文件添加数据

    参数:
    num (int): 数字部分，用于生成文件名
    alp (str): 字母部分，用于生成文件名
    input_data (str): 要添加的JSON对象的input键的值
    output_data (str): 要添加的JSON对象的output键的值
    """
    filename = f"./test/{num}_{alp}.jsonl"

    # 创建要添加的数据对象
    data = {
        "input": input_data,
        "output": output_data
    }

    try:
        # 写入数据到文件。使用a模式，确保追加到文件末尾
        with open(filename, 'a', encoding='utf-8') as f:
            # 确保中文等非ASCII字符能正确写入，同时保留换行符
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
        print(f"成功添加数据到 {filename}")
    except Exception as e:
        print(f"添加数据时出错: {e}")


def get_multiline_input(prompt: str) -> str:
    """获取多行输入，直到用户输入空行为止"""
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == '':  # 空行表示输入结束
            break
        lines.append(line)
    # 使用换行符连接所有行
    return '\n'.join(lines)


if __name__ == "__main__":
    # 从键盘获取输入
    try:
        num = int(input("请输入数字部分 (num): "))
        alp = input("请输入字母部分 (alp): ")

        input_data = get_multiline_input("请输入input字段的值（空行结束输入）:")
        output_data = get_multiline_input("请输入output字段的值（空行结束输入）:")

        add_to_jsonl(num, alp, input_data, output_data)
    except ValueError:
        print("错误: 数字部分必须是整数")
    except Exception as e:
        print(f"发生未知错误: {e}")