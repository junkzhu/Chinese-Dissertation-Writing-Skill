---
description: 中文毕业论文写作闭环（风格→框架→起草→检阅）
---

# AI Vibe Writing - 毕业论文写作流程

面向中文学位论文的多步骤写作流程。

## 前置条件
- `.ai_context` 已配置：`style_profile.md`、`custom_specs.md`
- `资料/03_我的内容/`、`资料/04_我的小论文/` 或 `资料/提取/` 中有可参考文本（用于风格提取）

## 步骤

1. **分析请求**
   - 读取 `.ai_context/custom_specs.md`、`style_profile.md`、`error_log.md`

2. **文档规范**（可选）
   - 参考 `document_spec_template.md` 创建 `document_spec.md`
   - 用户批准后继续

3. **框架创建**（新建项目时）
   - 读取 `prompts/3_section_builder.md`
   - 根据参考论文生成 `chapters/*.tex` 与 `main.tex`

4. **内容起草**
   - 读取 `prompts/4_content_writer.md`
   - 按大纲与 style_profile 生成正文

5. **自检**
   - 读取 `prompts/6_consistency_checker.md` 做术语、格式审计
   - 发现 AI 味或违例则修订

6. **输出**
   - 呈现终稿，询问是否追加 error_log 规则
