# Day 5: LMDeploy 大模型量化部署实践

# 1. 大模型部署背景

![Untitled](figs/d5/Untitled.png)

![Untitled](figs/d5/Untitled%201.png)

<aside>
💡 挑战：

- 部署：手机部署、工业终端无网部署 → llama.cpp
- 推理：动态推理 → continuous batch
- 内存：吞吐量，响应时间
</aside>

# 2. LMDeploy简介

- 非移动端
- 创新点：turbomind (C++)

![Untitled](figs/d5/Untitled%202.png)

![Untitled](figs/d5/Untitled%203.png)

![Untitled](figs/d5/Untitled%204.png)

![Untitled](figs/d5/Untitled%205.png)

<aside>
💡 量化好处

- 减少显存
- 加快推理速度
</aside>

![Untitled](figs/d5/Untitled%206.png)

- AWQ算法思想：重要参数不量化

![Untitled](figs/d5/Untitled%207.png)

![Untitled](figs/d5/Untitled%208.png)

![Untitled](figs/d5/Untitled%209.png)

![Untitled](figs/d5/Untitled%2010.png)

![Untitled](figs/d5/Untitled%2011.png)

![Untitled](figs/d5/Untitled%2012.png)

# 3. 实践环节

1. 安装
2. 部署
3. 量化

Reference:

[文档](https://github.com/InternLM/tutorial/blob/main/lmdeploy/lmdeploy.md)

[视频](https://www.bilibili.com/video/BV1iW4y1A77P)