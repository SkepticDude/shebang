import os

def combine_jsonl_files():
    # Define paths relative to this script location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    commands_dir = os.path.join(base_dir, 'commands')
    input_dir = os.path.join(base_dir, 'input')
    output_file = os.path.join(input_dir, 'pretrain.jsonl')

    # Ensure the input directory exists
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    if not os.path.exists(commands_dir):
        print(f"Error: Commands directory not found at {commands_dir}")
        return

    print(f"Combining files from {commands_dir} into {output_file}...")
    
    # Open output file in write mode to overwrite/replace existing file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate over files in the commands directory
        for filename in os.listdir(commands_dir):
            if filename.endswith('.jsonl'):
                file_path = os.path.join(commands_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        outfile.write(line)

if __name__ == "__main__":
    combine_jsonl_files()