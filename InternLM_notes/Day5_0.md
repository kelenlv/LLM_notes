# Day 5-作业

**基础作业：**

- [x]  使用 LMDeploy 以本地对话、网页Gradio、API服务中的一种方式部署 InternLM-Chat-7B 模型，生成 300 字的小故事（需截图）

**进阶作业（可选做）**

- [ ]  将第四节课训练自我认知小助手模型使用 LMDeploy 量化部署到 OpenXLab 平台。
- [ ]  对internlm-chat-7b模型进行量化，并同时使用KV Cache量化，使用量化后的模型完成API服务的部署，分别对比模型量化前后（将 bs设置为 1 和 max len 设置为512）和 KV Cache 量化前后（将 bs设置为 8 和 max len 设置为2048）的显存大小。
- [ ]  在自己的任务数据集上任取若干条进行Benchmark测试，测试方向包括：（1）TurboMind推理+Python代码集成（2）在（1）的基础上采用W4A16量化（3）在（1）的基础上开启KV Cache量化（4）在（2）的基础上开启KV Cache量化（5）使用Huggingface推理

### 1. **TurboMind 推理+命令行本地对话**

![Untitled](../figs/d5_0/Untitled.png)

Reference:

[文档](https://github.com/InternLM/tutorial/blob/main/lmdeploy/lmdeploy.md)

[视频](https://www.bilibili.com/video/BV1iW4y1A77P)
