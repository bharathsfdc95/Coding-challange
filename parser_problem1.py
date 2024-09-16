import csv

def read_spec(spec_file):
    """Read the spec file to get field widths."""
    with open(spec_file, 'r') as f:
        field_lengths = [int(line.strip()) for line in f]
    return field_lengths

def parse_fixed_width_file(input_file, field_lengths):
    """Parse the fixed width file based on field lengths."""
    parsed_data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            record = []
            start = 0
            for length in field_lengths:
                end = start + length
                record.append(line[start:end].strip())
                start = end
            parsed_data.append(record)
    return parsed_data

def write_to_csv(parsed_data, output_file):
    """Write the parsed data to a CSV file."""
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(parsed_data)

if __name__ == "__main__":
    # File paths (Change the paths)
    spec_file = 'C:\\Users\\bhara\\OneDrive\\Documents\\field_lengths.txt'
    input_file = 'C:\\Users\\bhara\\OneDrive\\Documents\\input.txt'
    output_file = 'C:\\Users\\bhara\\OneDrive\\Documents\\output.csv'
    
    field_lengths = read_spec(spec_file)
    
    parsed_data = parse_fixed_width_file(input_file, field_lengths)
    
    write_to_csv(parsed_data, output_file)
    
    print(f"CSV file '{output_file}' has been generated.")
