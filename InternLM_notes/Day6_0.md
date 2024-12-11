# Day 6-作业

**基础作业**

- [x]  使用 OpenCompass 评测 InternLM2-Chat-7B 模型在 C-Eval 数据集上的性能

**进阶作业**

- [ ]  使用 OpenCompass 评测 InternLM2-Chat-7B 模型使用 LMDeploy 0.2.0 部署后在 C-Eval 数据集上的性能

### 1. OpenCompass 评测 InternLM2-Chat-7B 模型在 C-Eval 数据集上的性能

- 命令行，修改目录为 InternLM2-Chat-7B 模型所在地址
    
    `python [run.py](http://run.py/) --datasets ceval_gen --hf-path /share/model_repos/internlm2-chat-7b/ --tokenizer-path /share/model_repos/internlm2-chat-7b/ --tokenizer-kwargs padding_side='left' truncation='left' trust_remote_code=True --model-kwargs trust_remote_code=True device_map='auto' --max-seq-len 2048 --max-out-len 16 --batch-size 4 --num-gpus 1 --debug`
    
- 结果

![Untitled](../figs/d6_0/Untitled.png)

![Untitled](../figs/d6_0/Untitled%201.png)

![Untitled](../figs/d6_0/Untitled%202.png)
