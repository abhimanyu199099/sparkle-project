import pandas as pd

file_names = [str(i) for i in range(10, 101)]

def fix_numeric(value):
    if isinstance(value, str):
        try:
            # Convert the string to a float after replacing the comma with a dot
            return float(value.replace(',', '.'))
        except ValueError:
            # If conversion fails, return the value as is (e.g., for non-numeric columns)
            return value
    else:
        return value
    

for i in range (len(file_names)):
# Read the file with semicolon as the delimiter
    input_file_path = rf"C:\Users\Abhim\Documents\Python_Programs\materna_trace_set\GWA-T-13_Materna-Workload-Traces\Materna-Trace-1\{file_names[i]}.csv"
    output_file_path = rf"C:\Users\Abhim\Documents\Python_Programs\materna_trace_set\GWA-T-13_Materna-Workload-Traces\Materna-Trace-1\{file_names[i]}.csv"
    df = pd.read_csv(input_file_path, sep=';', quotechar='"')
    df = df.applymap(fix_numeric)

# Save the corrected dataframe to a new CSV file
    df.to_csv(output_file_path, index=False)
    print (f"Fixed file {file_names[i]}")