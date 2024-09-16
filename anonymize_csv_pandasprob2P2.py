import pandas as pd
import hashlib

def anonymize_csv(input_file, output_file, chunksize=100000):
    def anonymize_value(value):
        return hashlib.sha256(value.encode()).hexdigest()

    # Columns to anonymize
    columns_to_anonymize = ['first_name', 'last_name', 'address']

    # Process the file in chunks
    reader = pd.read_csv(input_file, chunksize=chunksize)
    for chunk_num, chunk in enumerate(reader):
        for col in columns_to_anonymize:
            chunk[col] = chunk[col].apply(anonymize_value)
        if chunk_num == 0:
            chunk.to_csv(output_file, index=False, mode='w')
        else:
            chunk.to_csv(output_file, index=False, mode='a', header=False)
        print(f"Processed chunk {chunk_num + 1}")

if __name__ == '__main__':
    anonymize_csv('sample_data.csv', 'anonymized_data.csv')
