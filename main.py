#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)

# Load the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("pegasus-samsum-model")
tokenizer = AutoTokenizer.from_pretrained("tokenizer")

@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the input text from the request
    input_data = request.json
    input_text = input_data.get('text', '')

    # Tokenize the input
    inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=128, early_stopping=True)

    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Adjust the port as needed

