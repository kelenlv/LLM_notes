import torch
from torch.nn import functional as F

from transformers import AutoModelForCausalLM

# must use AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("model_path", torch_dtype="auto")

# this size is Qwen2.5-72B only:29568->29696
pad_size = 128

sd = model.state_dict()

for i, k in enumerate(sd):
    v = sd[k]
    print(k, i)
    # interleaving the padded zeros
    if ('mlp.up_proj.weight' in k) or ('mlp.gate_proj.weight' in k):
        prev_v = F.pad(v.unsqueeze(1), (0, 0, 0, 1, 0, 0)).reshape(29568*2, -1)[:pad_size*2]
        new_v = torch.cat([prev_v, v[pad_size:]], dim=0)
        sd[k] = new_v
    elif 'mlp.down_proj.weight' in k:
        prev_v= F.pad(v.unsqueeze(2), (0, 1)).reshape(8192, 29568*2)[:, :pad_size*2]
        new_v = torch.cat([prev_v, v[:, pad_size:]], dim=1)
        sd[k] = new_v

# this is a very large file; make sure your RAM is enough to load the model
torch.save(sd, '/save_path/pytorch_model.bin') #pytorch_model.bin or model.safetensors
