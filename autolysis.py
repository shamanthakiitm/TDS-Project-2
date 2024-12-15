# /// script
# requires-python="\u003e=3.9"
# dependencies = [
#     "pandas",
#     "numpy",
#     "matplotlib",
#     "seaborn",
#     "requests",
#     "openai",
#     "scikit-learn",
#     "tabulate",
#     "chardet",
#     "asyncio",
# ]
# ///

import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import httpx
import chardet

# Constants
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
AIPROXY_TOKEN = os.getenv('AIPROXY_TOKEN', "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDE5NDJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.I8IkdGIUiqJf35Ewq0ugD-TO0UV_knI7nUN7zTEnq2k")  # Use environment variable or set directly

# Function to load CSV data with encoding detection
def load_csv_data(file_path):
    """Load CSV data, automatically detecting file encoding."""
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    with open(file_path, 'rb') as file_handle:
        encoding_result = chardet.detect(file_handle.read())
    detected_encoding = encoding_result['encoding']
    print(f"Detected file encoding: {detected_encoding}")
    return pd.read_csv(file_path, encoding=detected_encoding)

# Function to perform basic data analysis
def perform_data_analysis(data_frame):
    """Perform basic data analysis, including summary stats and correlations."""
    if data_frame.empty:
        print("Error: Dataset is empty.")
        sys.exit(1)
    numeric_data_frame = data_frame.select_dtypes(include=['number'])  # Select only numeric columns
    analysis_results = {
        'summary': data_frame.describe(include='all').to_dict(),
        'missing_values': data_frame.isnull().sum().to_dict(),
        'correlation': numeric_data_frame.corr().to_dict()  # Compute correlation only on numeric columns
    }
    print("Data analysis complete.")
    return analysis_results

# Function to create visualizations
def create_visualizations(data_frame):
    """Generate and save visualizations for numeric columns."""
    sns.set(style="whitegrid")
    numeric_columns = data_frame.select_dtypes(include=['number']).columns
    if numeric_columns.empty:
        print("No numeric columns found for visualization.")
        return
    for numeric_column in numeric_columns:
        plt.figure()
        sns.histplot(data_frame[numeric_column].dropna(), kde=True)
        plt.title(f'Distribution of {numeric_column}')
        file_name = f'{numeric_column}_distribution.png'
        plt.savefig(file_name)
        print(f"Saved distribution plot: {file_name}")
        plt.close()

# Function to generate a narrative using the LLM
def generate_analysis_narrative(analysis_data):
    """Use the LLM to generate a narrative based on the analysis."""
    headers = {
        'Authorization': f'Bearer {AIPROXY_TOKEN}',
        'Content-Type': 'application/json'
    }
    prompt_message = f"Provide a detailed analysis based on the following data summary: {analysis_data}"
    request_data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt_message}]
    }
    try:
        response = httpx.post(API_URL, headers=headers, json=request_data, timeout=30.0)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except httpx.HTTPStatusError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except httpx.RequestError as request_error:
        print(f"Request error occurred: {request_error}")
    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")
    return "Narrative generation failed due to an error."

# Main processing function
def main_process(file_path):
    """Coordinate the process: load data, analyze, visualize, and generate narrative."""
    print("Starting autolysis process...")
    
    # Load data
    data_frame = load_csv_data(file_path)
    print("Dataset loaded successfully.")
    
    # Analyze data
    print("Analyzing data...")
    analysis_data = perform_data_analysis(data_frame)
    
    # Generate visualizations
    print("Generating visualizations...")
    create_visualizations(data_frame)
    
    # Generate narrative
    print("Generating narrative...")
    narrative_output = generate_analysis_narrative(analysis_data)
    
    if narrative_output != "Narrative generation failed due to an error.":
        with open('README.md', 'w') as readme_file:
            readme_file.write(narrative_output)
        print("Narrative successfully written to README.md.")
    else:
        print("Narrative generation failed. Skipping README creation.")
    
    print("Autolysis process completed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"Processing file: {file_path}")
    main_process(file_path)
