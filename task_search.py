from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.utils.data import Dataset

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausaML.from_pretrained("google/gemma-2b", device = "auto")


#float 16

input_text = "" #add path to dataset
input_ids = tokenizer(input_text, return_tensors = "pt").input_ids

#Custom Dataset inheriting from torch.utils.data.Dataset
class CustomFinetuningDataset(Dataset):
    def __init__(self, text_file_pathj, tokenizer_name, propmpt, target_generator_fn):

        pass
    def __len__(self):

        pass
    def __getitem__(self, idx):

        pass

    

