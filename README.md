# 🔘 Deep Focus System 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://share.streamlit.io/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **A High-Contrast, Minimalist Productivity Suite.**
> 这是一个为深度工作者设计的极简主义习惯追踪与专注系统。拒绝花哨，回归专注本质。

---

## ✨ 核心特性 / Features

* **🌑 Immersive Focus Mode**: 140px 巨型黑白对比番茄钟，极致沉浸，消除视觉干扰。
* **📊 Dynamic Task Classification**: 
    * **专注型 (Focus)**: 关联时长目标，自动计算完成度进度条。
    * **打卡型 (Check-off)**: 适用于简单日常习惯（如：做饭、早起）。
* **🔔 Smart Pomodoro Segments**: 默认 30 分钟一轮，支持自动切换 **5 分钟绿色休息模式**，伴有中断提示音。
* **📉 GitHub-Style Heatmap**: 自动生成年度打卡贡献图，见证每一天的坚持。
* **⚙️ Live Management**: 支持在运行中实时修改习惯名称、目标时长及任务类型。
* **💾 Auto-Persistence**: 本地 JSON 自动存储，数据永远掌握在自己手中。

---

## 🚀 快速开始 / Quick Start

### 1. 克隆仓库
```bash
git clone https://github.com/daoyuanw/daily-habit-tracker.git
cd daily-habit-tracker
```

### 2. 安装依赖
```bash
pip install streamlit pandas plotly
```

### 3. 启动程序
```bash
streamlit run habit_tracker.py
```
---

## 🛠️ 技术栈 / Tech Stack

- **Frontend/Backend**: [Streamlit](https://streamlit.io/)
- **Data Viz**: [Plotly](https://plotly.com/)
- **Storage**: Local JSON

---

## 📄 开源协议 / License

Distributed under the **MIT License**. See \`LICENSE\` for more information.