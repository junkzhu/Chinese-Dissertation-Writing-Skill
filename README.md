# AI 中文毕业论文写作 Skill

> 一个为**中文学位论文**定制的 AI 写作助手：风格迁移 + 错题本 + 长期记忆，让你用 AI 写论文，却保留你的语气和习惯。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 它能做什么

| 能力 | 说明 |
|------|------|
| **风格迁移** | 从你的过往文章（中期报告、初审稿等）提取「风格 DNA」，生成 `style_profile.md`，后续写作自动模仿你的语气与句式 |
| **错题本** | 记住你的每次纠正，写入 `error_log.md`，避免「我们提出」→「本文提出」类错误重复出现 |
| **长期记忆** | 术语、单位、参考文献存入 `hard_memory` / `soft_memory` / `reference_library`，全文保持一致 |
| **论文工程生成** | 根据参考论文自动创建 LaTeX 项目结构（`chapters/*.tex`、`main.tex`） |

---

### 1. 克隆并打开

```bash
git clone https://github.com/junkzhu/Chinese-Dissertation-Writing-Skill.git
```

在 **Cursor / VS Code / Trae** 中打开该文件夹。

### 2. 初始化论文项目结构

以**论文中文名称**为根目录，创建：

```
<论文中文名称>/
├── main.tex
├── chapters/
├── .ai_context/     ← 从 Skill 复制 .ai_context 模板
└── 资料/
    ├── 01_格式要求/     ← 毕业论文格式规范（若无则参考 02）
    ├── 02_参考毕业论文/ ← 他人的已通过论文
    ├── 03_我的内容/     ← 中期报告、初审稿等
    ├── 04_我的小论文/   ← 小论文（可选，可扩写为毕业论文）
    └── 提取/           ← parse_pdf 输出
```

### 3. 阅读毕业论文格式要求
> @1_format_spec_reader 请解析格式规范

### 4. 提取风格

将他人通过的毕业论文放入 `资料/02_参考毕业论文/`
将你的中期报告、初审稿、小论文等放入 `资料/03_我的内容/` 和 `资料/04_我的小论文/`

> @2_style_extractor 请提取 资料/02_参考毕业论文/，资料/03_我的内容/ 和 资料/04_我的小论文/ 中的文章 的写作风格


### 5. 审核全文一致性

> @6_consistency_checker 请检查全文一致性；

> @6_consistency_checker 请检查参考文献 xxx.bib 的格式；

---

## 核心 Prompts

| 文件 | 作用 |
|------|------|
| `0_pdf_reader` | 读取 PDF，提取证据入库 |
| `1_format_spec_reader` | 解析格式规范 PDF → hard_memory |
| `2_style_extractor` | 资料 → style_profile |
| `3_section_builder` | 参考论文 → chapters 框架 |
| `4_subsection_builder` | 生成章节内小标题结构 |
| `5_content_writer` | 按大纲起草正文 |
| `6_consistency_checker` | 术语 / 格式一致性审计 |
| `7_error_logger` | 纠正 → error_log + 重写 |

---

## 常用指令

**编译论文（在项目根目录）：**
```bash
xelatex main && bibtex main && xelatex main && xelatex main
```
或用 latexmk：`latexmk -xelatex main`

**对 AI 的常用提示：**
- `@.ai_context/prompts/1_format_spec_reader.md` 阅读格式要求
- `@.ai_context/prompts/2_style_extractor.md` 提取写作风格（资料/03、04）
- `@.ai_context/prompts/3_section_builder.md` 参考范文创建 chapters 框架
- `@.ai_context/prompts/4_subsection_builder.md` 生成章节内小标题结构
- `@.ai_context/prompts/5_content_writer.md` 按大纲起草正文
- `@.ai_context/prompts/6_consistency_checker.md` 检查全文术语/格式一致性
- `@.ai_context/prompts/7_error_logger.md` 纠错入错题本并重写

---

## 项目结构约定

```
<论文中文名称>/
├── main.tex
├── chapters/           # 各章节 .tex
├── .ai_context/        # 风格、错题本、记忆
│   ├── style_profile.md
│   ├── error_log.md
│   ├── custom_specs.md
│   └── memory/
└── 资料/
    ├── 01_格式要求/     # 格式规范（若无则参考 02）
    ├── 02_参考毕业论文/ # 他人已通过论文
    ├── 03_我的内容/     # 中期报告、初审稿等
    ├── 04_我的小论文/   # 小论文（可选）
    └── 提取/            # 抽取文本
```

详见 `.ai_context/project_structure.md`。

---

## 文件结构

```
<项目根目录>/
├── README.md
├── LICENSE
├── .ai_context/
│   ├── style_profile.md      # 风格指纹（可由 Style Extractor 生成）
│   ├── error_log.md          # 错题本
│   ├── custom_specs.md       # 自定义规范
│   ├── project_structure.md  # 存储结构规范
│   ├── document_spec_template.md
│   ├── outline_template.md
│   ├── reference_learning.md
│   ├── pdf_ingestion_template.md
│   ├── memory/               # hard / soft / reference_library
│   ├── prompts/              # 0–7 号 prompts
│   └── scripts/
│       ├── parse_pdf.py           # PDF 文本抽取
│       └── create_placeholder_image.py #创建空白占位图
├── .traerules                # 系统级工作流配置（可选）
└── .agents/workflows/        # 自动化流程
```

---

## 设计理念

**不替代，只辅助。**  
把格式整理、风格统一、术语校对、错题积累交给 AI，把创意、论证与深度留给你。

---

## 致谢与衍生

本 Skill 基于 [AI-Vibe-Writing-Skills](https://github.com/donghuixin/AI-Vibe-Writing-Skills) 定制，聚焦中文学位论文写作场景。

---

## License

MIT License
