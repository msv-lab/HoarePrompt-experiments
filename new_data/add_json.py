import json
import os

def add_to_jsonl(num: int, alp: str, input_data: str, output_data: str) -> None:
    """
    Append data to a specified JSONL file.

    Args:
    num (int): Numeric part, used to generate the filename.
    alp (str): Alphabetic part, used to generate the filename.
    input_data (str): Value for the 'input' key in the JSON object.
    output_data (str): Value for the 'output' key in the JSON object.
    """
    filename = f"./test/{num}_{alp}.jsonl"

    # Create the data object to add
    data = {
        "input": input_data,
        "output": output_data
    }

    try:
        # Write data to the file in append mode
        with open(filename, 'a', encoding='utf-8') as f:
            # Ensure non-ASCII characters (like Chinese) are written correctly
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
        print(f"Successfully added data to {filename}")
    except Exception as e:
        print(f"Error while adding data: {e}")

def get_multiline_input(prompt: str) -> str:
    """Get multiline input from the user until an empty line is entered."""
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == '':  # Empty line indicates end of input
            break
        lines.append(line)
    # Join all lines with newline characters
    return '\n'.join(lines)

if __name__ == "__main__":
    # Get input from keyboard
    try:
        num = int(input("Enter numeric part (num): "))
        alp = input("Enter alphabetic part (alp): ")

        input_data = get_multiline_input("Enter value for the 'input' field (finish with an empty line):")
        output_data = get_multiline_input("Enter value for the 'output' field (finish with an empty line):")

        add_to_jsonl(num, alp, input_data, output_data)
    except ValueError:
        print("Error: Numeric part must be an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
