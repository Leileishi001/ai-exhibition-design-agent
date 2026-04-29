# 🎨 AI Exhibition Design Agent

> 一个基于多Agent协作的展览与快闪店设计生成系统  
> A multi-agent system for automated exhibition & pop-up store design

---

## 🚀 项目简介（Overview）

本项目是一个面向展览设计、商业空间与快闪店的 AI 设计辅助系统。  
通过构建多Agent协同工作流，将传统“人工主导”的设计前期流程拆解并自动化，实现从设计需求输入到概念方案输出的完整闭环。

该系统重点解决以下问题：
-
 前期方案构思耗时长
-
 创意方向依赖个人经验
-
 提案效率低、沟通成本高

👉 使用 AI Agent 后：
-
 快速生成多个设计方向
-
 提高方案多样性
-
 缩短提案周期

---

## 🧠 核心能力（Key Features）

-
 ✨ 多Agent协同（Multi-Agent Collaboration）
-
 🔗 长链推理（Long-chain reasoning）
-
 🧩 模块化设计流程（Modular Workflow）
-
 🎯 面向设计行业定制（Design-specific prompts）
-
 ⚡ 快速生成设计提案初稿

---

## ⚙️ 工作流程（Workflow）

系统由四个核心 Agent 构成：

### 1️⃣ Brief Parsing Agent（需求解析）
输入：用户设计需求  
输出：结构化信息

-
 品牌定位
-
 目标人群
-
 核心诉求
-
 场地条件
-
 关键词提取

---

### 2️⃣ Concept Generation Agent（创意生成）

基于需求解析结果，生成：

-
 概念主题（Concept）
-
 设计故事（Narrative）
-
 视觉关键词（材质 / 灯光 / 风格）

---

### 3️⃣ Spatial Planning Agent（空间规划）

输出空间结构方案：

-
 功能分区（入口 / 展示 / 互动 / 打卡）
-
 动线设计
-
 区域重点说明

---

### 4️⃣ Render Prompt Agent（渲染提示生成）

生成适用于 AI 绘图 / 3D 渲染的提示词：

-
 场景描述
-
 材质与光影
-
 风格控制
-
 Midjourney / Stable Diffusion Prompt

---

## 🔄 Agent 协作逻辑（System Flow）

User Input
↓
Brief Parser
↓
Concept Generator
↓
Spatial Planner
↓
Render Prompt Generator
↓
Design Output
yaml
复制代码
👉 每个 Agent 输出作为下一个 Agent 的输入  
👉 形成完整“设计推理链路”

---

## 📂 项目结构（Project Structure）

ai-exhibition-design-agent/
│
├── app.py # 主程序入口
├── README.md # 项目说明
│
├── prompts/ # Prompt 模块（核心逻辑）
│ ├── brief_parser.txt
│ ├── concept_generator.txt
│ ├── spatial_planner.txt
│ └── render_prompt.txt
│
├── examples/ # 示例输入输出
│ ├── demo_input.txt
│ └── demo_output.txt
yaml
复制代码
---

## 🧪 示例（Demo）

### 输入（Input）

品牌：隐形眼镜
主题：沙漠中的绿洲
场地：商场快闪店（80㎡）
目标：吸引年轻女性打卡
yaml
复制代码
---

### 输出（Output）

**概念主题：**  
沙漠中的绿洲（Oasis in the Desert）

**设计逻辑：**  
通过极端干燥环境隐喻用眼疲劳，将产品比喻为“舒适绿洲”

**空间结构：**
- 入口：沙漠通道
- 中心：水体装置（核心视觉）
- 打卡区：环绕绿洲

**渲染关键词：**
futuristic pop-up store, desert oasis theme, circular water installation, warm sand texture, soft lighting, cinematic composition
yaml
复制代码
---

## 🛠️ 使用方式（How to Run）

### 1️⃣ 安装依赖

```bash
pip install openai
￼
2️⃣ 配置 API Key
bash
复制代码
export
 OPENAI_API_KEY=your_api_key
（Windows 用户可使用 set 命令）
￼
3️⃣ 运行项目
bash
复制代码
python app.py
输入设计需求即可获得完整设计方案。
￼
📈 实际应用价值（Real-world Impact）
在实际设计流程中，该系统可：
• ⏱ 提案准备时间：1-2天 → 数小时
• 🎨 创意产出：显著提升多样性
• 🔄 沟通效率：减少反复修改成本
• 🧠 降低经验依赖：新人也可快速产出方案
￼
🌟 应用场景（Use Cases）
• 展览设计
• 快闪店设计
• 商业空间设计
• 品牌活动策划
• 3D视觉方案生成
￼
🔮 未来优化方向（Future Work）
• 与 Blender / 3ds Max 集成
• 自动生成平面布局图
• 引入用户行为模拟（动线优化）
• 接入图像生成模型实现一键出图
• Web UI（在线设计工具）
￼
👨‍🎨 作者说明（Author）
本项目由一名具有展览与空间设计经验的设计师开发，
结合实际项目流程，将 AI 引入设计生产环节，探索设计自动化的可能性。
