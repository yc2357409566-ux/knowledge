#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成365天法语学习日计划脚本
"""

from datetime import datetime, timedelta
import os

# 定义学习计划数据
LEARNING_PHASES = {
    "A1_phase1": {
        "months": [3, 4, 5],  # 3月, 4月, 5月
        "focus": "发音与基础",
        "weekly_hours": 30,
        "daily_hours": 4,
    },
    "A2_phase2": {
        "months": [6, 7, 8],  # 6月, 7月, 8月
        "focus": "日常对话与过去式",
        "weekly_hours": 35,
        "daily_hours": 4.3,
    },
    "B1_phase3": {
        "months": [9, 10, 11],  # 9月, 10月, 11月
        "focus": "流利交流与深化",
        "weekly_hours": 40,
        "daily_hours": 4.5,
    },
    "B1_phase4": {
        "months": [12, 1, 2],  # 12月, 1月, 2月
        "focus": "专业表达与冲刺",
        "weekly_hours": 35,
        "daily_hours": 4.3,
    }
}

DAILY_ACTIVITIES = {
    "A1_phase1": [
        ("晨间基础", 40, "字母发音反复练习 + Forvo听原音"),
        ("Pimsleur课程", 60, "Pimsleur第X课 - 互动式语音学习"),
        ("Anki词汇学习", 60, "学习20个新词汇"),
        ("晚间应用", 40, "看视频 + 写日记 + 跟读练习"),
    ],
    "A2_phase2": [
        ("晨间复习", 40, "前一天词汇复习 + 发音练习"),
        ("Pimsleur课程", 70, "Pimsleur课程 - 过去式和对话"),
        ("语法学习", 50, "学习新语法点或动词变位"),
        ("听力与对话", 70, "听力练习 + Tandem对话"),
        ("阅读与写作", 40, "读简单文章 + 写日记"),
    ],
    "B1_phase3": [
        ("晨间复习", 40, "词汇和语法复习"),
        ("听力突破", 80, "看新闻、播客或电视节目"),
        ("语法深化", 50, "虚拟式、条件式等高级语法"),
        ("阅读挑战", 60, "阅读法语文学或文章"),
        ("口语练习", 70, "Tandem对话 + 讨论话题"),
        ("写作提高", 40, "写文章、邮件或评论"),
    ],
    "B1_phase4": [
        ("晨间复习", 40, "快速词汇和语法复习"),
        ("新闻和时事", 80, "看法国新闻和时事节目"),
        ("专业表达", 60, "学习商务法语或专业术语"),
        ("深度阅读", 70, "阅读报纸、杂志或书籍"),
        ("口语流利度", 80, "Tandem对话 + 自言自语练习"),
        ("写作精进", 50, "写论文、评论或正式文件"),
    ]
}

def get_phase_for_date(year, month, day):
    """根据日期确定学习阶段"""
    if month in [3, 4, 5]:
        return "A1_phase1"
    elif month in [6, 7, 8]:
        return "A2_phase2"
    elif month in [9, 10, 11]:
        return "B1_phase3"
    else:  # 12, 1, 2
        return "B1_phase4"

def get_week_number(year, month, day):
    """获取当年的周数"""
    date = datetime(year, month, day)
    return date.isocalendar()[1]

def get_day_of_year(year, month, day):
    """获取当年的第几天"""
    date = datetime(year, month, day)
    return date.timetuple().tm_yday

def generate_daily_plan(year, month, day, day_of_year):
    """生成单日计划"""
    phase = get_phase_for_date(year, month, day)
    date_str = f"{year}-{month:02d}-{day:02d}"

    # 计算周一至周日
    date = datetime(year, month, day)
    weekday_name = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"][date.weekday()]
    week_number = get_week_number(year, month, day)

    # 确定每月的第几周
    first_day = datetime(year, month, 1)
    week_of_month = (day + first_day.weekday()) // 7 + 1

    content = f"""# {year}年{month}月{day}日 - 第{day_of_year}天：法语学习

> **日期信息**
>
> 日期：{year}年{month}月{day}日 ({weekday_name})
> 学习第{day_of_year}天 / 365天
> 当月第{week_of_month}周 / 全年第{week_number}周
> 当前阶段：{phase}

---

## 📅 今日日期与进度

| 项目 | 信息 |
|------|------|
| **日期** | {year}年{month}月{day}日 |
| **周几** | {weekday_name} |
| **学习第几天** | 第{day_of_year}天 |
| **当月进度** | {day}天 |
| **全年进度** | {day_of_year}/365天 |
| **当月第几周** | 第{week_of_month}周 |
| **全年第几周** | 第{week_number}周 |
| **当前阶段** | {phase} - {LEARNING_PHASES[phase]["focus"]} |

---

## 🎯 今日目标

学完今天，你应该能够：
- ✅ [目标1 - 根据阶段]
- ✅ [目标2 - 根据阶段]
- ✅ [目标3 - 根据阶段]

**今日学习时长**：{LEARNING_PHASES[phase]["daily_hours"]}小时

---

## ⏰ 今日学习时间表

### 晨间基础（[时间]）：[活动]
**时长**：[X分钟]
**任务**：
1. [任务1]
2. [任务2]
3. [任务3]

**检查点**：
- [ ] 完成任务1
- [ ] 完成任务2
- [ ] 完成任务3

---

## 📊 今日学习成果总结

| 类别 | 成果 | 检查 |
|------|------|------|
| **听力** | | [ ] |
| **口语** | | [ ] |
| **词汇** | | [ ] |
| **阅读** | | [ ] |
| **写作** | | [ ] |
| **语法** | | [ ] |

**今日总学习时间**：{LEARNING_PHASES[phase]["daily_hours"]}小时 ✅

---

## 💡 今日学习技巧

1. **保持专注**
   - 关闭所有干扰
   - 使用番茄工作法（25分钟专注 + 5分钟休息）

2. **重复是关键**
   - 至少听3遍新内容
   - 跟读10遍才能形成记忆

3. **说出来很重要**
   - 不要只是看和听
   - 大声说出来

4. **记录很关键**
   - 写下新词汇
   - 记录学习笔记
   - 追踪你的进度

---

## 📝 学习日记

**今天我学到的最有趣的东西**：
```
_______________________________________________________
```

**今天最困难的部分**：
```
_______________________________________________________
```

**明天我想重点学的**：
```
_______________________________________________________
```

**总体感受 (1-10分)**：___ /10

---

## 📚 相关链接

### 周计划
- [[第{week_number}周计划|第{week_number}周详细计划]]

### 月计划
- [[第{month}个月计划|{month}月完整计划]]

### 资源库
- [[动词变位表|法语语法快查]]
- [[{phase}_词汇库|{phase}词汇库]]

### 进度追踪
- [[学习进度追踪|查看整体进度]]

---

**学习日期**：{year}年{month}月{day}日
**完成时间**：_________

"""

    return content

def generate_all_daily_plans(start_date, end_date, output_dir):
    """生成所有日计划"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    current_date = start_date
    day_count = 1

    while current_date <= end_date:
        year = current_date.year
        month = current_date.month
        day = current_date.day
        day_of_year = get_day_of_year(year, month, day)

        # 生成计划内容
        content = generate_daily_plan(year, month, day, day_of_year)

        # 保存为文件
        filename = f"{current_date.strftime('%Y-%m-%d')}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ 已生成 {filename}")

        current_date += timedelta(days=1)
        day_count += 1

    print(f"\n✨ 成功生成 {day_count} 个日计划文件！")

if __name__ == "__main__":
    # 设置起始和结束日期
    start_date = datetime(2026, 3, 21)
    end_date = datetime(2027, 3, 20)

    # 输出目录
    output_dir = "/Users/mac/Desktop/knowledge/法语学习/日计划"

    # 生成所有日计划
    print("开始生成365天法语学习日计划...")
    print(f"从 {start_date.strftime('%Y年%m月%d日')} 到 {end_date.strftime('%Y年%m月%d日')}")
    print("-" * 50)

    generate_all_daily_plans(start_date, end_date, output_dir)

    print("-" * 50)
    print("✨ 所有日计划生成完毕！")
    print(f"保存位置：{output_dir}")
