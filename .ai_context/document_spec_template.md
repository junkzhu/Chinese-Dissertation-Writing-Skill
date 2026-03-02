# Document Spec (Master Thesis Single Source of Truth)

> 本文档为最高优先级契约。
> Outline Manager 与 Content Writer 必须严格遵守。
> 未经用户批准，不得开始写作。

---

## 1. Thesis Metadata（论文基本信息）

- **Thesis Title / 论文中文名称**: [论文题目]
  - 同时作为项目根目录文件夹名，内部由 chapters/ 存放各章节 .tex 内容
- **Degree Type**: 硕士学位论文
- **Discipline**: [学科]
- **Language**: 中文
- **Target Audience**: 硕士论文评审委员会

### 项目结构约定
- 根目录：`<论文中文名称>/`
- 章节存放：`<论文中文名称>/chapters/`（各章 .tex 文件）
- AI 上下文：`<论文中文名称>/.ai_context/`（style_profile、memory、config）
- 资料：`资料/01_格式要求/`（格式规范）、`02_参考毕业论文/`（他人论文）、`03_我的内容/`（中期报告等）、`04_我的小论文/`（小论文，可选）、`提取/`（抽取文本）

---

## 2. Core Research Objective（研究目标）

- 本论文旨在解决：[核心研究问题]
- 研究动机：[为什么重要]
- 预期贡献：
  1. [贡献1]
  2. [贡献2]
  3. [贡献3]

---

## 3. Global Structural Requirements（全局结构约束）

### 必须包含的章节

1. 绪论
2. 相关工作
3. 方法一
4. 方法二
5. 实验与结果分析
6. 讨论
7. 结论与展望
8. 致谢
9. 参考文献

---

## 4. Length & Distribution Control（字数与分配）

- **Total Target Words**: 40000
- **Minimum Total Words**: 35000

### 方法章节硬性要求

- 方法1 ≥ 15000 字
- 方法2 ≥ 15000 字
- 每个 subsection ≥ 1200 字
- 理论推导必须完整展开
- 不允许压缩式表达

---

## 5. Argument Logic Contract（论证逻辑契约）

每个方法章节必须包含：

1. 背景与问题定义
2. 理论基础
3. 数学建模
4. 推导过程
5. 算法流程
6. 模块分析
7. 复杂度分析
8. 与现有方法对比
9. 本节小结

---

## 6. Evidence Requirements（证据要求）

- 最少引用文献：20 篇
- 每个方法章节至少引用 5 篇
- 实验部分必须包含：
  - 定量结果
  - 消融实验
  - 对比实验

- **Citation Style**: IEEE
- **文中引用格式**: \cite{}

---

## 7. Formatting Compliance（格式强制约束）

- 所有章节必须符合学校格式规范
- 图编号按章节编号
- 公式必须编号
- 图表引用必须在正文中说明

---

## 8. Vocabulary & Terminology Constraints（术语约束）

### Hard Memory Terms（必须使用）
- [统一术语1]
- [统一术语2]

### Negative Constraints（禁止使用）
- 参考 error_log.md
- 禁止第一人称
- 禁止口语表达
- 禁止英文式总结句

---

## 9. Revision Control（修订机制）

- 未经批准，不得大幅改动结构
- 大范围修改必须先输出 Revision Plan
- 最大修订轮次：4

---

## 10. Final Contract

本 Document Spec 为全文最高优先级控制文件。

若与：
- Custom Specifications
- style_profile
- 其他记忆规则

发生冲突，

优先级顺序为：

Document Spec > Format Rules > Hard Memory > Custom Specs > Soft Memory