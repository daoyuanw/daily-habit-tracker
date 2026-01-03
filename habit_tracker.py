import streamlit as st
import pandas as pd
import datetime
import json
import os
import plotly.express as px
import time

# --- 1. 数据持久化与配色方案 ---
DB_FILE = "habit_data.json"
# 预设酷炫色盘
COOL_COLORS = ["#2E3440", "#5E81AC", "#81A1C1", "#88C0D0", "#4C566A", "#B48EAD", "#A3BE8C", "#D08770"]

def load_data():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                # 补全可能缺失的字段
                for h in data:
                    if "type" not in data[h]: data[h]["type"] = "打卡型"
                    if "daily_goal_h" not in data[h]: data[h]["daily_goal_h"] = 2.0
                    if "total_minutes" not in data[h]: data[h]["total_minutes"] = 0
                    if "log" not in data[h]: data[h]["log"] = {}
                return data
        except: return {}
    return {}

def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def play_bell():
    """注入音频HTML"""
    st.markdown("""
        <audio autoplay>
            <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
        </audio>
    """, unsafe_allow_html=True)

# --- 2. 状态初始化 ---
if 'habits' not in st.session_state:
    st.session_state.habits = load_data()
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'is_break' not in st.session_state:
    st.session_state.is_break = False

st.set_page_config(page_title="Deep Focus System", layout="wide")

# --- 3. 核心 CSS 样式 ---
st.markdown("""
    <style>
    .big-timer { font-family: 'Courier New', Courier, monospace; font-size: 140px !important; font-weight: bold; text-align: center; border-radius: 20px; padding: 40px; margin: 10px 0px; line-height: 1; }
    .work-mode { color: #FFFFFF; background-color: #000000; }
    .break-mode { color: #000000; background-color: #A3BE8C; }
    .habit-card { border-left: 5px solid #000; padding: 10px 15px; margin-bottom: 10px; background: #f9f9f9; border-radius: 0 10px 10px 0; }
    .stProgress > div > div > div > div { background-color: #000000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔘 SMART FOCUS SYSTEM")

# --- 4. 侧边栏：管理与修改 ---
with st.sidebar:
    st.header("⚙️ 习惯配置")
    
    # 添加新习惯
    with st.expander("➕ 添加新习惯"):
        new_h = st.text_input("习惯名称")
        new_t = st.selectbox("类型", ["专注型", "打卡型"])
        new_g = st.number_input("每日目标 (h)", 0.5, 12.0, 2.0) if new_t == "专注型" else 0.0
        if st.button("确认添加"):
            if new_h:
                color = COOL_COLORS[len(st.session_state.habits) % len(COOL_COLORS)]
                st.session_state.habits[new_h] = {"type": new_t, "daily_goal_h": new_g, "color": color, "log": {}, "total_minutes": 0}
                save_data(st.session_state.habits); st.rerun()

    # 修改/编辑习惯
    if st.session_state.habits:
        st.divider()
        st.subheader("📝 修改习惯")
        edit_target = st.selectbox("选择任务", list(st.session_state.habits.keys()))
        info = st.session_state.habits[edit_target]
        
        up_name = st.text_input("修改名称", value=edit_target)
        up_type = st.selectbox("修改类型", ["专注型", "打卡型"], index=0 if info["type"]=="专注型" else 1)
        up_goal = info["daily_goal_h"]
        if up_type == "专注型":
            up_goal = st.number_input("修改每日目标", 0.1, 12.0, float(info.get("daily_goal_h", 2.0)))
        
        c_up, c_del = st.columns(2)
        if c_up.button("保存修改", type="primary"):
            old_data = st.session_state.habits.pop(edit_target)
            st.session_state.habits[up_name] = {**old_data, "type": up_type, "daily_goal_h": up_goal}
            save_data(st.session_state.habits); st.rerun()
        if c_del.button("删除任务"):
            del st.session_state.habits[edit_target]
            save_data(st.session_state.habits); st.rerun()

# --- 5. 巨型多阶段番茄钟 ---
focus_list = [k for k, v in st.session_state.habits.items() if v['type'] == "专注型"]

if focus_list:
    st.subheader("⏱️ 专注时间")
    target_habit = st.selectbox("当前专注习惯", focus_list)
    
    # 初始化单轮时长
    if 'current_timer' not in st.session_state or not st.session_state.timer_running:
        st.session_state.current_timer = 30 * 60 if not st.session_state.is_break else 5 * 60

    timer_placeholder = st.empty()
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.session_state.is_break:
            st.success("☕ 休息时间 (5min)...")
            if st.button("跳过休息"): 
                st.session_state.is_break = False; st.session_state.current_timer = 30*60; st.rerun()
        else:
            btn_label = "停止" if st.session_state.timer_running else "开始专注 (30min)"
            if st.button(btn_label, use_container_width=True, type="primary"):
                st.session_state.timer_running = not st.session_state.timer_running
                st.rerun()

    if st.session_state.timer_running:
        while st.session_state.current_timer > 0 and st.session_state.timer_running:
            m, s = divmod(st.session_state.current_timer, 60)
            mode_style = "break-mode" if st.session_state.is_break else "work-mode"
            timer_placeholder.markdown(f'<div class="big-timer {mode_style}">{m:02d}:{s:02d}</div>', unsafe_allow_html=True)
            time.sleep(1)
            st.session_state.current_timer -= 1
        
        if st.session_state.current_timer <= 0:
            play_bell()
            if not st.session_state.is_break:
                # 结算
                today = str(datetime.date.today())
                h_data = st.session_state.habits[target_habit]
                if today not in h_data["log"]: h_data["log"][today] = {"status": True, "focus_mins": 30}
                else: h_data["log"][today]["focus_mins"] = h_data["log"][today].get("focus_mins", 0) + 30
                h_data["total_minutes"] += 30
                save_data(st.session_state.habits)
                st.session_state.is_break = True; st.session_state.current_timer = 5 * 60
            else:
                st.session_state.is_break = False; st.session_state.current_timer = 30 * 60
                st.session_state.timer_running = False
            st.rerun()
    else:
        m, s = divmod(st.session_state.current_timer, 60)
        mode_style = "break-mode" if st.session_state.is_break else "work-mode"
        timer_placeholder.markdown(f'<div class="big-timer {mode_style}" style="opacity:0.5;">{m:02d}:{s:02d}</div>', unsafe_allow_html=True)

# --- 6. 今日状态与热力图 ---
st.divider()
date_str = str(st.date_input("查看日期", datetime.date.today()))

for h_type in ["专注型", "打卡型"]:
    typed_habits = {k: v for k, v in st.session_state.habits.items() if v['type'] == h_type}
    if typed_habits:
        st.write(f"### {h_type}任务")
        cols = st.columns(max(len(typed_habits), 4))
        for i, (name, info) in enumerate(typed_habits.items()):
            with cols[i % 4]:
                h_color = info.get('color', '#000')
                st.markdown(f"<div class='habit-card' style='border-color:{h_color}'><b>{name}</b></div>", unsafe_allow_html=True)
                
                if h_type == "专注型":
                    today_m = info["log"].get(date_str, {}).get("focus_mins", 0)
                    goal_m = info["daily_goal_h"] * 60
                    st.progress(min(today_m/goal_m, 1.0))
                    st.caption(f"今日: {today_m/60:.1f} / {info['daily_goal_h']} h")
                
                if st.checkbox("完成", value=date_str in info["log"], key=f"cb_{name}_{date_str}"):
                    if date_str not in info["log"]:
                        info["log"][date_str] = {"status": True, "focus_mins": 0}
                        save_data(st.session_state.habits); st.rerun()
                elif date_str in info["log"]:
                    info["log"].pop(date_str)
                    save_data(st.session_state.habits); st.rerun()

# --- 7. 年度热力图 (保持原有的酷炫配色逻辑) ---
st.divider()
st.subheader("YEARLY PROGRESS")
if st.session_state.habits:
    sel_v = st.selectbox("选择习惯图谱", list(st.session_state.habits.keys()))
    h_info = st.session_state.habits[sel_v]
    
    # 构建数据矩阵... (此处略，保持与上一版相同的高质量绘图逻辑)
    df = pd.DataFrame({"date": pd.date_range(f"{datetime.date.today().year}-01-01", f"{datetime.date.today().year}-12-31")})
    df['date_str'] = df['date'].dt.strftime('%Y-%m-%d')
    df['week'] = df['date'].dt.isocalendar().week
    df['weekday'] = df['date'].dt.weekday
    df.loc[(df['date'].dt.month == 1) & (df['week'] > 50), 'week'] = 0
    df['status'] = df['date_str'].apply(lambda x: 1 if x in h_info["log"] else 0)
    pivot = df.pivot_table(index='weekday', columns='week', values='status', aggfunc='first').fillna(0)
    for j in range(7):
        if j not in pivot.index: pivot.loc[j] = 0
    pivot = pivot.sort_index()
    fig = px.imshow(pivot.values, x=pivot.columns, y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                    color_continuous_scale=['#F0F0F0', h_info.get('color', '#000')], range_color=[0, 1], aspect="auto")
    fig.update_layout(coloraxis_showscale=False, height=220, margin=dict(l=0,r=0,t=10,b=10))
    fig.update_traces(xgap=3, ygap=3)
    st.plotly_chart(fig, use_container_width=True)