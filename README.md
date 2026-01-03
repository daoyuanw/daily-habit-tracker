🔘 Deep Focus System
A High-Contrast, Minimalist Productivity Suite. > 这是一个为深度工作者设计的极简主义习惯追踪与专注系统。拒绝花哨，回归专注本质。

✨ 核心特性 / Features
🌑 Immersive Focus Mode: 巨型黑白对比番茄钟，极致沉浸，消除视觉干扰。

📊 Dynamic Task Classification:

专注型 (Focus): 关联时长目标，自动计算完成度进度条。

打卡型 (Check-off): 适用于简单日常习惯（如：做饭、早起）。

🔔 Smart Pomodoro Segments: 默认 30 分钟一轮，支持自动切换 5 分钟绿色休息模式，伴有中断提示音。

📉 GitHub-Style Heatmap: 自动生成年度打卡贡献图，见证每一天的坚持。

⚙️ Live Management: 支持在运行中实时修改习惯名称、目标时长及任务类型。

💾 Auto-Persistence: 本地 JSON 自动存储，数据永远掌握在自己手中。

🚀 快速开始 / Quick Start
1. 克隆仓库
Bash

git clone https://github.com/daoyuanw/daily-habit-tracker.git
cd daily-habit-tracker
2. 安装依赖
Bash

pip install streamlit pandas plotly
3. 启动程序
Bash

streamlit run habit_tracker.py
🎨 预览 / UI Preview
功能模块	描述
Deep Timer	140px 巨型数字显示，支持工作/休息颜色动态切换
Progress Bar	基于每日目标时长的动态进度条，实时结算
Yearly Map	自动根据习惯主色调生成的 365 天热力图

导出到 Google 表格

🛠️ 技术栈 / Tech Stack
Frontend/Backend: Streamlit (The fastest way to build data apps)

Data Viz: Plotly (Interactive high-quality charts)

Logic: Python 3.x

Storage: Local JSON

🤝 贡献 / Contributing
如果你有更好的 UI 方案或功能创意，欢迎提交 Pull Request 或 Issue！

Fork 本仓库

创建你的特性分支 (git checkout -b feature/AmazingFeature)

提交你的改动 (git commit -m 'Add some AmazingFeature')

推送到分支 (git push origin feature/AmazingFeature)

开启 Pull Request

📄 开源协议 / License
Distributed under the MIT License. See LICENSE for more information.