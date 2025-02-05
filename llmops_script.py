# llmops_script.py
from transformers import pipeline

# Load the pre-trained model for text generation
generator = pipeline('text-generation', model='gpt2')

# Generate some text
prompt = "Once upon a time"
generated_text = generator(prompt, max_length=50)

print("Generated Text:")
print(generated_text[0]['generated_text'])
