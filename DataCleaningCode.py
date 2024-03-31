import pandas as pd
import dask.dataframe as dd
import string

# Define function to read first 1000 rows of CSV file in chunks and handle parsing errors
def read_csv_with_errors(filename):
    chunks = pd.read_csv(filename, nrows=150, chunksize=1000)
    dfs = []
    for chunk in chunks:
        try:
            df = dd.from_pandas(chunk, npartitions=1)
            # Drop columns 2 and 3 (index 1 and 2) from the Dask dataframe
            df = df.map_partitions(lambda partition: partition.drop(columns=partition.columns[1:3]))
            
            # Fill missing values in the fourth column with an empty string
            df['SECTION_TEXT'] = df['SECTION_TEXT'].fillna('').map(lambda x: x.lower().translate(str.maketrans('', '', string.punctuation)), meta=('SECTION_TEXT', 'object'))
            
            dfs.append(df)
        except pd.errors.ParserError:
            pass  # Skip chunk if parsing error occurs
    return dd.concat(dfs)

# Define function to replace newlines with spaces in text
def replace_newlines(text):
    return ' '.join(text.split('\n'))

# Read the first 1000 rows of the CSV file with error handling, drop middle two columns, and apply text processing
df = read_csv_with_errors('Data.csv')

# Group the preprocessed dataset based on ARTICLE_ID and concatenate SECTION_TEXT for each ARTICLE_ID
grouped_df = df.groupby('ARTICLE_ID')['SECTION_TEXT'].apply(lambda x: ' '.join(x)).reset_index()

# Replace newlines with spaces in SECTION_TEXT
grouped_df['SECTION_TEXT'] = grouped_df['SECTION_TEXT'].apply(replace_newlines)

# Now save the grouped dataframe to a single CSV file
grouped_df.to_csv('CleanedData.csv', index=False, single_file=True)
