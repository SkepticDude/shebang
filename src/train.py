import os
import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    Trainer,
    TrainingArguments,
    DataCollatorForSeq2Seq,
)

MODEL_NAME = "google/flan-t5-small"
DATA_PATH = "data/input/train.jsonl"
OUTPUT_DIR = "models/flan-t5-linux"

MAX_INPUT_LENGTH = 128
MAX_OUTPUT_LENGTH = 64


def preprocess(example):
    model_inputs = tokenizer(
        example["input"],
        max_length=MAX_INPUT_LENGTH,
        truncation=True,
    )

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            example["output"],
            max_length=MAX_OUTPUT_LENGTH,
            truncation=True,
        )

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    dataset = load_dataset("json", data_files=DATA_PATH)["train"]
    dataset = dataset.map(preprocess, remove_columns=dataset.column_names)

    data_collator = DataCollatorForSeq2Seq(
        tokenizer,
        model=model,
    )

    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=5,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=20,
        save_strategy="epoch",
        save_total_limit=2,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        # tokenizer=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
