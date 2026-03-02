# AI 中文毕业论文写作 Skill - 能力总览

面向中文学位论文的 AI 写作能力、Prompts 与配置说明。

---

## 1. 系统级工作流

采用 **规范驱动** 写作：

1. **规范**：`document_spec.md` 约定核心论据与约束
2. **规划**：大纲含 `definition_of_done`，先结构后内容
3. **分析**：读取 style_profile、error_log、memory
4. **起草**：按 DoD 与风格生成 LaTeX
5. **审计**：consistency-checker 做术语/格式校验
6. **迭代**：用户反馈 → 更新 error_log / memory

---

## 2. Prompts 与能力

| 编号 | 名称 | 用途 |
|------|------|------|
| 0 | PDF Reader | 读取 PDF → reference_library、memory |
| 1 | Format Spec Reader | 格式规范 PDF → hard_memory |
| 2 | Style Extractor | 资料/ → style_profile |
| 3 | Section Builder | 参考论文 → chapters/*.tex 框架 |
| 4 | Content Writer | 按大纲起草正文 |
| 5 | Error Logger | 纠正 → error_log + 重写 |
| 6 | Consistency Checker | 术语、格式一致性审计 |
| 7 | Subsection Builder | 章节内小标题结构 |

---

## 3. 项目结构

- 根目录 = 论文中文名称
- `chapters/`：各章 .tex
- `.ai_context/`：style_profile、error_log、memory
- `资料/01_格式要求/`：格式规范；`02_参考毕业论文/`：他人论文；`03_我的内容/`：中期报告等；`04_我的小论文/`：小论文（可选）；`提取/`：抽取文本

详见 `.ai_context/project_structure.md`。

---

## 4. 配置入口

- `style_profile.md`：风格指纹
- `error_log.md`：错题本
- `custom_specs.md`：主题、受众、阈值
- `document_spec_template.md`：文档契约模板
- `outline_template.md`：大纲模板
- `memory/*.json`：硬性/柔性记忆、参考文献库
- `reference_learning.md`：参考文献学习流程
- `pdf_ingestion_template.md`：PDF 入库模板

---

## 5. 自动化流程

`.agents/workflows/`：

- **ai_vibe_writing**：写作闭环（分析→框架→起草→检阅）
- **pdf_ingestion**：PDF 解析与入库
