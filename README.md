# Automated Data Analysis with Autolysis

## Overview

The `autolysis.py` script is a comprehensive tool designed to perform automated data analysis, generate visualizations, and create a narrative summary using a Large Language Model (LLM). This project is ideal for datasets stored as CSV files and offers:

- **Automated Data Analysis**: Provides insights such as summary statistics, missing values, and correlations.
- **Data Visualizations**: Creates clear and informative visualizations for numerical columns.
- **Narrative Generation**: Generates a descriptive and actionable report using GPT-4o-Mini via an API.

This script is designed for use in academic and professional settings and is optimized for compatibility with Python 3.9+.

---

## Features

### 1. Automated Data Analysis
- **Summary Statistics**: Automatically calculates essential metrics for numerical and categorical columns, such as mean, median, standard deviation, and frequency counts. These statistics help users quickly grasp the data's underlying patterns and trends.
- **Missing Value Detection**: Identifies missing or incomplete data in each column. This feature is critical for pre-processing datasets and ensuring data quality before further analysis.
- **Correlation Analysis**: Computes correlation coefficients between numerical variables to uncover potential relationships or dependencies within the data. A correlation heatmap provides a visual representation of these relationships, aiding exploratory data analysis.

### 2. Data Visualization
- **Distribution Plots**: Generates histograms and KDE (Kernel Density Estimation) plots for each numerical column to visualize data distribution.
- **Correlation Heatmaps**: Creates heatmaps for numerical columns to highlight the strength and direction of relationships between variables.
- **Easy Sharing**: All visualizations are saved as `.png` files, making them easy to include in reports and presentations.

### 3. Narrative Generation
- **AI-Powered Reports**: Leverages GPT-4o-Mini to automatically generate a narrative summary of the analysis. The narrative explains trends, highlights key findings, and provides actionable insights, saving time and effort in manual report writing.
- **Markdown Format**: The generated narrative is saved as a `README.md` file, making it accessible and easy to share or integrate into documentation.

---

## Datasets Analyzed

The tool has been applied to several datasets to demonstrate its capabilities:

1. **Goodreads Dataset**:
   - **Description**: Focuses on books, their ratings, genres, and authors.
   - **Insights**:
     - Analyzes the distribution of book ratings to identify trends in reader preferences.
     - Evaluates the popularity of various genres, helping publishers understand market demand.
     - Provides an overview of author contributions and their impact on ratings and reviews.

2. **Media Dataset**:
   - **Description**: Examines data on media consumption, including views, ratings, and genres.
   - **Insights**:
     - Identifies the most popular media genres and their respective audience demographics.
     - Highlights patterns in media ratings and trends over time, offering insights for content creators.
     - Evaluates audience preferences, helping media companies tailor their offerings.

3. **Happiness Dataset**:
   - **Description**: Analyzes global happiness indicators, including income, education, and social support.
   - **Insights**:
     - Reveals factors contributing to higher happiness scores in different countries.
     - Provides a comparative analysis of regions based on economic and social parameters.
     - Highlights actionable recommendations for improving happiness metrics globally.

---

## Usage

### 1. Command-Line Execution
Run the script by providing the path to a CSV file as input:
```bash
uv run autolysis.py <file_path>
```
For example:
```bash
uv run autolysis.py goodreads.csv
```

### 2. Outputs
- **Visualizations**: Saved as PNG files in the same directory as the dataset.
- **Narrative Report**: Saved as `README.md` in the same directory as the dataset.

---

## Example Workflow

1. **Input**: Provide a CSV file (e.g., `goodreads.csv`).
2. **Process**:
   - Load and analyze the dataset.
   - Generate visualizations for all numerical columns.
   - Use GPT-4o-Mini to create a narrative report.
3. **Output**:
   - Visualizations: `column_name_distribution.png`
   - Narrative Report: `README.md`

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


