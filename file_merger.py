import pandas as pd

def merge_files(file_list, output_file):

    # Initialize an empty list to hold the dataframes
    dataframes = []

    # Read the first file with header
    df_first = pd.read_csv(file_list[0])
    dataframes.append(df_first)

    # Read the rest of the files without header
    for file in file_list[1:]:
        df = pd.read_csv(file, header=0)  # Use header=0 to treat the first line as data
        dataframes.append(df)

    # Concatenate all dataframes
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged dataframe to a new CSV file
    merged_df.to_csv(output_file, index=False)

# Example usage
file_list = [rf"C:\Users\Abhim\Documents\Python_Programs\materna_trace_set\GWA-T-13_Materna-Workload-Traces\Materna-Trace-1\{i}.csv" for i in range(1, 101)]
output_file = "merged_output.csv"
merge_files(file_list, output_file)
