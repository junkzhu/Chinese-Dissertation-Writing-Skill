## Custom Specifications

- **Thesis Title / 论文中文名称**: [论文题目]（用作项目根目录文件夹名）
- **Topic**: [你的论文方向]
- **Target Audience**: 硕士论文评审委员会

### 项目结构
- 根目录 = 论文中文名称
- `chapters/`：各章节 .tex 内容
- `.ai_context/`：style_profile、memory、config
- `资料/01_格式要求/`：格式规范；`02_参考毕业论文/`：他人论文；`03_我的内容/`：中期报告等；`04_我的小论文/`：小论文（可选）；`提取/`：抽取文本
- **Special Requirements**:
  - 方法章节必须深入理论推导
  - 每个核心模块必须包含动机、理论、实现与分析
  - 不允许压缩式表达
- **Writing Mode**: Structured Draft

---

## Length & Depth Control（新增关键部分）

- **Total Target Words**: 40000
- **Minimum Total Words**: 35000
- **Method Section Minimum Words**: 18000
- **Per Subsection Minimum Words**: 1200
- **Theory Expansion Required**: true
- **Derivation Detail Level**: high
- **Experiment Interpretation Depth**: detailed

---

## Context Budget

- **Max Context Tokens**: 16000
- **Target Utilization**: 0.75
- **Min Useful Tokens**: 3000
- **Compression Strategy**: outline_only

---

## Evidence Requirements

- **Minimum References**: 20
- **Evidence Coverage**: 0.8
- **Citation Style**: IEEE
- **Evidence Format**: Inline

---

## Citation Formatting

- **Author Format**: surname_initial
- **EtAl Threshold**: 3
- **Include DOI**: false
- **Include URL**: false

---

## Outline Validation

- **Word Deviation Tolerance**: 0.15
- **Core Point Coverage**: 0.95
- **Max Revision Rounds**: 4

---

## Review Settings

- **AI Tone Threshold**: 75
- **Detection Priority**: builtin
- **Disabled Detectors**: gptzero, originality

---

## Reference Learning Settings

- **Library Path**: .ai_context/memory/reference_library.json
- **Ingestion Mode**: summary_only
- **Deduplication Strategy**: title_year
- **Term Extraction**: enabled
- **Style Extraction Scope**: abstracts_only

---

## PDF Reading Settings

- **PDF Engine**: builtin
- **PDF Source**: local
- **Max Pages**: 30
- **Section Priority**: abstract, intro, method, results, conclusion
- **Extraction Mode**: text_first
- **Chunk Size**: 800
- **Chunk Overlap**: 120