# 🌟Day 4: XTuner 大模型单卡低成本微调实践

# 1. 🌟Finetune简介：针对LLM构建下游应用

![Untitled](../figs/d4/Untitled.png)

1. **增量预训练微调**
    1. 扩大知识面
    2. system&input 留空
        
        ![Untitled](../figs/d4/Untitled%201.png)
        
    3. LoRA & QLoRA
        1. LoRA模型：Adapter
            
            ![Untitled](../figs/d4/Untitled%202.png)
            
            ![Untitled](../figs/d4/Untitled%203.png)
            
- 2.  **指令跟随微调**
    1. 规范答题格式/指令
        
        ![Untitled](../figs/d4/Untitled%204.png)
        
    2. 具体实施（微调阶段）
        1. **对话模板的角色指定**（由微调框架实施）
            
            ![Untitled](../figs/d4/Untitled%205.png)
            
            ![Untitled](../figs/d4/Untitled%206.png)
            
        2. 微调原理
            
            ![Untitled](../figs/d4/Untitled%207.png)
            

# 2. XTuner简介

![Untitled](../figs/d4/Untitled%208.png)

# 3. XTuner功能：8GB显存玩转LLM

![Untitled](../figs/d4/Untitled%209.png)

1. Flash Attention
2. DeepSpeed ZeRO

# 4. 🌟动手实战环节

1. **安装**
    1. 环境+微调框架
2. **准备配置文件**
    1. 模型名+使用算法+数据集+跑几次
3. **模型下载**
4. **数据集下载**
    1. **将数据转为 XTuner 的数据格式（.xlsx→ .jsonL）**
    2. **划分训练集和测试集**
5. **修改配置文件中的本地路径**
6. **开始微调**
7. **将得到的 PTH 模型转换为 HuggingFace 模型，即：生成 Adapter 文件夹（LoRA 模型文件 = Adapter）**
8. **部署与测试**

Reference：

[手册](https://github.com/InternLM/tutorial/blob/main/xtuner/README.md)

[视频](https://www.bilibili.com/video/BV1yK4y1B75J)
