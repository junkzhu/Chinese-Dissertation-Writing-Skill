# 论文项目存储结构 / Thesis Project Storage Structure

> 本规范定义以**论文中文名称**为根目录的毕业论文项目存储结构。
> 智能体（Style Extractor、Framework Builder、PDF Reader 等）必须遵守此规范。

---

## 完整目录结构

```
<论文中文名称>/
├── main.tex                    # LaTeX 主文件
├── chapters/                   # 各章节内容
│   ├── introduction.tex
│   ├── related_work.tex
│   ├── method_1.tex
│   ├── method_2.tex
│   ├── experiments.tex
│   ├── discussion.tex
│   └── conclusion.tex
│
├── .ai_context/                # AI 写作上下文（风格、记忆、配置）
│   ├── style_profile.md       # 风格指纹（Style Extractor 生成）
│   ├── custom_specs.md        # 自定义规范
│   ├── document_spec.md       # 文档契约
│   ├── error_log.md           # 错题本
│   ├── reference_learning.md  # 参考文献学习流程
│   ├── pdf_ingestion_template.md
│   ├── outline_template.md
│   ├── memory/
│   │   ├── hard_memory.json   # 硬性记忆（术语、单位）
│   │   ├── soft_memory.json   # 柔性记忆（偏好、措辞）
│   │   └── reference_library.json  # 参考文献库
│   ├── prompts/               # 或软链接到 Skills 仓库
│   └── scripts/
│       └── parse_pdf.py       # PDF 文本提取脚本
│
└── 资料/                      # 论文相关参考资料
    ├── 01_格式要求/            # 毕业论文格式规范
    │   └── 毕业论文格式要求.pdf   # 若无则参考 02 中其他毕业论文
    ├── 02_参考毕业论文/        # 他人的已通过毕业论文（结构、写法参考）
    │   └── xxx_硕士论文.pdf
    ├── 03_我的内容/            # 本人的相关内容
    │   ├── 中期报告.pdf
    │   ├── 初审稿.pdf
    │   └── ...
    ├── 04_我的小论文/          # 本人的小论文（可选，可扩写/翻译为毕业论文）
    │   └── xxx.pdf
    └── 提取/                  # 从上述 PDF 抽取的文本（parse_pdf / PDF Reader 输出）
        ├── 格式要求.txt
        ├── 参考论文_xxx.txt
        ├── 中期报告.txt
        └── ...
```

---

## 各目录说明

| 路径 | 用途 | 生成方式 |
|------|------|----------|
| `chapters/` | 各章节 .tex 内容 | Framework Builder、Content Writer |
| `.ai_context/style_profile.md` | 写作风格指纹 | Style Extractor 从 资料/ 分析生成 |
| `.ai_context/custom_specs.md` | 自定义规范 | 用户手动配置 |
| `.ai_context/error_log.md` | 错题本 | Error Logger |
| `.ai_context/memory/*.json` | 长期记忆与参考文献库 | 用户、PDF Reader、Reference Learning |
| `资料/01_格式要求/` | 学校/学院毕业论文格式规范 | 用户放入，若无则参考 02 中其他论文 |
| `资料/02_参考毕业论文/` | 他人已通过的毕业论文 | 用户放入 |
| `资料/03_我的内容/` | 本人的中期报告、初审稿等 | 用户放入 |
| `资料/04_我的小论文/` | 本人的小论文（可选，可扩写为毕业论文） | 用户放入 |
| `资料/提取/` | 从 PDF 抽取的文本 | parse_pdf.py 或 PDF Reader 输出 |

---

## 路径约定

- **Format Spec Reader 输入**：`资料/01_格式要求/*.pdf`；若无则从 `02_参考毕业论文/` 抽取格式规律
- **Style Extractor 输入**：`资料/03_我的内容/`、`资料/04_我的小论文/`（优先）及 `资料/提取/` 中的文本
- **Style Extractor 输出**：`.ai_context/style_profile.md`
- **Framework Builder 输入**：`资料/04_我的小论文/` 或 `02_参考毕业论文/` 作为结构参考
- **PDF Reader / parse_pdf 输出**：`资料/提取/*.txt`
- **Framework Builder 输出**：`chapters/*.tex`、`main.tex`

---

## 初始化步骤

1. 以论文中文名称为文件夹名创建项目根目录
2. 创建 `chapters/`、`.ai_context/`、`资料/01_格式要求/`、`资料/02_参考毕业论文/`、`资料/03_我的内容/`、`资料/04_我的小论文/`、`资料/提取/`
3. 将 AI-Vibe-Writing-Skills 中的 `.ai_context` 模板复制到项目
4. 放入资料：
   - **01_格式要求**：学校格式规范 PDF（若无则跳过，参考 02 中其他论文）
   - **02_参考毕业论文**：1–2 篇他人已通过论文
   - **03_我的内容**：你的中期报告、初审稿等
   - **04_我的小论文**（可选）：你的小论文，可扩写/翻译为毕业论文
5. 使用 Format Spec Reader 解析格式要求 → hard_memory
6. 使用 Style Extractor 分析 03、04 中的文本，生成 `style_profile.md`
