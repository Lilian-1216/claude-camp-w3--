# Claude Camp W3 — Python 实战练习

这是 Claude Camp 第三周的作业仓库，包含 3 个独立的 Python 项目，覆盖了文件读写、JSON 处理、命令行交互、数据验证、单元测试等核心技能。

## 🛠 环境要求

- Python 3.10+
- pytest（仅 Project 3 需要）

安装 pytest：
```bash
pip install pytest
```

---

## 📦 Project 1: CSV 学员数据分析器

**功能**：读取学员 CSV 文件，统计总人数、各国家分布、对赌完成率，并把结果保存为 JSON。

**文件**：
- `csv-analyzer.py` — 主程序
- `students.csv` — 输入数据（20 行测试数据）
- `students_analysis.json` — 输出结果

**运行方式**：
```bash
cd project-1-csv-analyzer
python csv-analyzer.py
```

**预期输出**：
- 控制台打印总人数、国家分布、对赌状态分布
- 生成 `students_analysis.json` 文件

---

## ⚙️ Project 2: JSON 配置文件读写器

**功能**：读取 `config.json` 配置文件，让用户通过命令行修改任意一项设置（主题、语言、字体大小），并保存回文件。`font_size` 带数据验证（必须在 8-32 之间），输入不合法会循环重试。

**文件**：
- `config_tool.py` — 主程序
- `config.json` — 配置文件

**运行方式**：
```bash
cd project-2-config-tool
python config_tool.py
```

**交互示例**：
```
Current settings:
  theme: dark
  language: zh-CN
  font_size: 14

Which setting would you like to change? (theme/language/font_size): font_size
New font_size (8-32, or 'q' to quit): 20
✅ Changed to 20
✅ Settings saved successfully!
```

---

## 🧪 Project 3: 带单元测试的字符串工具库

**功能**：实现 3 个字符串处理函数，并用 pytest 写了 13 个单元测试。

**文件**：
- `string_utils.py` — 工具库
  - `reverse_words(s)` — 反转单词顺序
  - `count_vowels(s)` — 统计元音字母数量
  - `is_palindrome(s)` — 判断是否回文
- `test_string_utils.py` — pytest 测试

**测试方式**：
```bash
cd project-3-string-utils
pytest
```

**预期结果**：
```
========== 13 passed in 0.05s ==========
```

---

## 🌿 分支结构

每个项目使用独立分支开发，完成后合并回 `main`：

- `main` — 主分支，包含所有完成的项目
- `project-1-csv-analyzer` — Project 1 开发分支
- `project-2-config-tool` — Project 2 开发分支
- `project-3-string-utils` — Project 3 开发分支