import os
import random

def shuffle_dataset():
    # Define paths relative to this script location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'input')
    pretrain_file = os.path.join(input_dir, 'pretrain.jsonl')
    train_file = os.path.join(input_dir, 'train.jsonl')

    if not os.path.exists(pretrain_file):
        print(f"Error: Pretrain file not found at {pretrain_file}")
        return

    print(f"Shuffling {pretrain_file} into {train_file}...")

    # Read all lines
    with open(pretrain_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Shuffle lines in place
    random.shuffle(lines)

    # Write shuffled lines to new file
    with open(train_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__ == "__main__":
    shuffle_dataset()