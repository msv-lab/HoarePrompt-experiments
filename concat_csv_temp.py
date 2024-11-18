import pandas as pd

# Specify the paths of the input CSV files
csv_file1 = './combined_output_code_contests_4_mini_1.csv'
csv_file2 = './combined_output_code_contests_4_mini_2.csv'
csv_file3 = './combined_output_code_contests_4_mini_3.csv'
# csv_file1 = './combined_output_code_contests_3point5_1.csv'
# csv_file2 = './combined_output_code_contests_3point5_2.csv'
# csv_file3 = './combined_output_code_contests_3point5_3.csv'

# Specify the path of the output CSV file
output_csv = './combined_output_code_contests_4_mini_total_runs.csv'
# output_csv = './combined_output_code_contests_3point5_total_runs.csv'

# Read each CSV file into a DataFrame
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
df3 = pd.read_csv(csv_file3)

# Concatenate the DataFrames
concatenated_df = pd.concat([df1, df2, df3], ignore_index=True)

# Save the concatenated DataFrame to the output CSV
concatenated_df.to_csv(output_csv, index=False)

print(f'CSV files have been concatenated and saved to {output_csv}')