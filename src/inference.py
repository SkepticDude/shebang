from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "models/shebang-linux"

print(f"\nLoading model from {model_name}...\n")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

prompt = "Display the contents of the hosts file"
print(f"Prompt: {prompt}")

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=20)

print(f"Response: {tokenizer.decode(outputs[0], skip_special_tokens=True)}\n")
