from transformers import AutoModelForCausalLM, AutoTokenizer
    
model_path = "quant_path"
quant_path_final = "save_path"   

custom_model = AutoModelForCausalLM.from_pretrained(model_path)
custom_model.save_pretrained(quant_path_final, max_shard_size='4GB')#max_shard_size

tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.save_pretrained(quant_path_final)
