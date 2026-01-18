import torch

# Check if CUDA is available
print("CUDA Available:", torch.cuda.is_available())

# Set device to GPU if available, otherwise CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)   
print("GPU Name:", torch.cuda.get_device_name(0))