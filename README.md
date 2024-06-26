# Contribution
This project exists thanks to the extraordinary people who contributed to it.
-  Muhammad Daniyal Haider (i222042@nu.edu.pk)
-  Muhammad Anas Khan (i221987@nu.edu.pk)


# Combined CSV Processor and TF-IDF Search Engine

## Introduction

Managing and analyzing large volumes of textual data is a common challenge across various domains, from academia to industry. In many scenarios, this involves processing CSV files containing textual information and extracting meaningful insights from them. Additionally, users often require efficient mechanisms to search through this data to find relevant information quickly. To address these needs, we present a combined solution comprising a CSV data cleaning tool and a TF-IDF-based search engine.

## Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Advantages](#advantages)
- [Installation](#installation)
- [Example](#example)
- [Dependencies](#dependencies)
- [Instructions](#Instructions (Execution))
- [Contributing](#contributing)
- [License](#license)

## Usage

1. **Data Cleaning**:
    - Run the provided Python script `DataCleaningCode.py`.
    - Ensure that you have the necessary libraries installed (e.g., pandas, dask).
    - Specify the input CSV file containing data to be cleaned.
    - The script reads the CSV file, drops specified columns, and preprocesses text data (lowercase, remove punctuation).
    - The cleaned data is saved to a new CSV file.

2. **TF-IDF Search Engine**:
    - Execute the Python script `SearchEngineCode.py`.
    - Make sure the required dependencies are installed (e.g., mrjob).
    - The search engine processes the preprocessed CSV file.
    - It calculates TF-IDF scores for each document and term.
    - Provide a query in the `query.txt` file.
    - The engine ranks documents based on their relevance to the query.

## Advantages

- **Scalability**: Utilizes Dask for processing large CSV files in chunks, making it suitable for handling big data.
- **Flexibility**: Can be easily adapted to different CSV structures and search requirements.
- **Efficiency**: Implements TF-IDF efficiently using the MapReduce paradigm, enabling quick retrieval of relevant documents.
- **Modularity**: The project is structured into separate components for data cleaning and search, promoting code reusability and maintainability.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/SahilKumar729/SearchEngine.git
    ```

2. Navigate to the project directory:

    ```
    cd combined-csv-processor-tfidf-search
    ```

3. Install dependencies:

    ```
    pip install pandas dask mrjob
    ```

## Example

1. **Data Cleaning**:
    ```
    python DataCleaningCode.py
    ```

2. **TF-IDF Search Engine**:
    ```
    python SearchEngineCode.py CleanedData.csv
    ```

# Instructions (Execution):
-  **Execute Data Cleaning Script**: Run `DataCleaningCode.py` file to clean the data.
-  **Provide Query Text**: Write your query in the `query.txt` file.
-  **Execute Search Engine Script**: Run the `SearchEngineCode.py` file.
-  **Query Processing**: The search engine will process the query to identify relevant terms and calculate their TF-IDF scores.
-  **Document Ranking**: Based on the TF-IDF scores, the search engine will rank the documents in the dataset according to their similarity to the query.
-  **Result Presentation**: The search engine will provide the result, presenting the most similar documents based on the query.

## Dependencies

- **Pandas**: A powerful data manipulation library in Python, used for reading and processing CSV files.
- **Dask**: Provides advanced parallelism for analytics, enabling efficient processing of large datasets.
- **MRJob**: A Python framework for writing MapReduce jobs, used here to implement the TF-IDF search engine.

## Contributing
Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests.



