from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model = AutoModelForSeq2SeqLM.from_pretrained(
    "stevhliu/t5-small-finetuned-billsum-ca_test")
tokenizer = AutoTokenizer.from_pretrained(
    "stevhliu/t5-small-finetuned-billsum-ca_test")
device = torch.device('cpu')

def summarize(text):
    print("Starting the summary...")
    
    preprocess_text = text.strip().replace("\n","")
    t5_prepared_Text = "summarize: "+preprocess_text
    print ("original text preprocessed: \n", preprocess_text)

    tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)


    # summmarize 
    summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=300,
                                    max_length=500,
                                    early_stopping=True)

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return str(output)
    