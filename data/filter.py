import json
import os

def process_raw_data():
    # Define paths relative to this script location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_file_path = os.path.join(base_dir, 'store', 'raw.jsonl')
    commands_dir = os.path.join(base_dir, 'commands')

    # Ensure the output directory exists
    if not os.path.exists(commands_dir):
        os.makedirs(commands_dir)

    # Check if input file exists
    if not os.path.exists(raw_file_path):
        print(f"Error: Input file not found at {raw_file_path}")
        return

    # Cache to store existing inputs per command to prevent duplicates
    existing_inputs_map = {}

    with open(raw_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            try:
                data = json.loads(line)
                output_str = data.get('output', '').strip()
                input_str = data.get('input', '').strip()
                
                if output_str:
                    # Get the first word as the command prefix (e.g., "cp", "ls")
                    command_prefix = output_str.split()[0]
                    output_file_path = os.path.join(commands_dir, f"{command_prefix}.jsonl")
                    
                    # Initialize cache for this command if not present
                    if command_prefix not in existing_inputs_map:
                        existing_inputs_map[command_prefix] = set()
                        if os.path.exists(output_file_path):
                            with open(output_file_path, 'r', encoding='utf-8') as existing_f:
                                for ex_line in existing_f:
                                    try:
                                        ex_data = json.loads(ex_line)
                                        existing_inputs_map[command_prefix].add(ex_data.get('input', '').strip())
                                    except json.JSONDecodeError:
                                        continue

                    if input_str in existing_inputs_map[command_prefix]:
                        print(f"duplicate {data}")
                        continue

                    with open(output_file_path, 'a', encoding='utf-8') as out_f:
                        out_f.write(json.dumps(data) + '\n')
                    
                    existing_inputs_map[command_prefix].add(input_str)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line}")

if __name__ == "__main__":
    process_raw_data()