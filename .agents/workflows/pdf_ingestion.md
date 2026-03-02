---
description: 解析 PDF 并更新参考文献库
---

# PDF 入库流程

读取本地或在线 PDF，提取结构化证据并写入 reference_library。

## 步骤

1. **分析输入**
   - 确认用户提供的是本地路径或 URL
   - 读取 `.ai_context/custom_specs.md` 的 PDF Reading Settings
   - 读取 `.ai_context/pdf_ingestion_template.md`

2. **解析 PDF**
   - 本地文件：可用 `.ai_context/scripts/parse_pdf.py` 抽取文本
   - 输出建议保存至 `资料/提取/`（可按来源命名，如 `03_中期报告.txt`）

3. **执行 PDF Reader 逻辑**
   - 读取 `.ai_context/prompts/0_pdf_reader.md`
   - 提取摘要、方法、结果、术语、可引用片段

4. **更新知识库**
   - `reference_library.json`：新增条目
   - `hard_memory.json`：术语、单位、事实
   - `soft_memory.json`：风格偏好

5. **汇报**
   - 简述入库结果并确认已更新
