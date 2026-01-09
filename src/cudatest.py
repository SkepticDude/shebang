import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))  # Shows your GPU model   
x = torch.randn(3, 3).to('cuda')
print(x.device)  # Should output: cuda:0   