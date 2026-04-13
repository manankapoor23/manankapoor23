<div align="center">

# Manan Kapoor

### ML Systems Engineer | LLM Inference | Data Pipelines | AI Infrastructure

Designing and optimizing systems for large language models — focusing on inference performance, memory efficiency, scalability, and real-world deployment constraints.

<br/>

[LinkedIn](https://www.linkedin.com/in/manan-kapoor-8545002a0/) • 
[Email](mailto:23.kapoormanan@gmail.com) • 
[GitHub](https://github.com/manankapoor23)

</div>

---

## Summary

Computer Engineering student with a strong focus on **ML Systems Engineering, LLM inference optimization, and data pipeline design**.  

Experienced in building **end-to-end systems around large language models**, including:
- Transformer inference optimization (KV caching, memory management)
- Large-scale dataset engineering for LLM fine-tuning
- LLM-powered applications (RAG, NL → SQL systems)

Interested in solving problems related to **latency, memory constraints, throughput, and scalability** in modern AI systems.

---

## Core Competencies

**ML Systems & Infrastructure**
- Transformer inference optimization (KV cache, paging, prefix reuse)
- Memory-efficient model serving and execution
- Performance profiling (latency, memory, compute trade-offs)

**LLM Engineering**
- Fine-tuning workflows (instruction tuning, dataset preparation)
- Retrieval-Augmented Generation (RAG)
- Prompt engineering and structured generation

**Data Engineering for ML**
- Large-scale dataset cleaning, deduplication, and normalization
- JSONL dataset design for training pipelines
- Data validation and reproducibility

**Backend & Systems**
- API development (FastAPI)
- Pipeline orchestration concepts (Airflow, MLflow, DVC)
- Dockerized workflows and reproducible environments

---

## Featured Projects

### KV-Paged Inference System for Transformer Models
Systems-level implementation of memory-efficient KV caching for transformer inference.

- Designed paging-based KV cache architecture decoupling logical token positions from physical memory
- Implemented **prefix reuse, reference counting, and copy-on-write semantics** for efficient memory sharing
- Reduced redundant allocations and improved memory efficiency in long-context decoding scenarios
- Validated numerical correctness against naive attention (<0.1% deviation)

**Keywords:** Transformer Inference, KV Cache, Memory Optimization, LLM Systems, PyTorch

---

### Punjabi LLM Dataset Engineering Pipeline (PLC-Rewrite)
Large-scale data engineering system for low-resource LLM fine-tuning.

- Processed **16M+ tokens (1.1M+ sentences)** with automated deduplication and noise filtering
- Built structured JSONL datasets for instruction tuning and evaluation
- Designed reproducible pipelines with schema validation and metadata annotation
- Improved data quality and reduced manual curation effort significantly

**Keywords:** Data Pipelines, NLP, LLM Fine-Tuning, Dataset Engineering

---

### Natural Language → SQL System (LLM Data Assistant)
LLM-powered system for querying structured databases using natural language.

- Built end-to-end pipeline: user query → SQL generation → execution → formatted response
- Integrated with Slack using FastAPI and LangChain
- Implemented schema-aware SQL generation for accurate query execution

**Keywords:** LLM Applications, LangChain, SQL, Backend Systems, API Integration

---

## Engineering Approach

- System-first mindset: design architecture before implementation
- Focus on **performance metrics**: memory usage, latency, throughput
- Explicit analysis of **trade-offs** (memory vs compute vs scalability)
- Emphasis on reproducibility and pipeline reliability
- Preference for understanding underlying systems over relying only on frameworks

---

## Tech Stack

**Languages:** Python, C++, JavaScript  
**ML/AI:** PyTorch, Transformers, Scikit-learn  
**LLM Tools:** Hugging Face, LangChain, OpenAI SDK  
**Data:** Pandas, NumPy, SQL (PostgreSQL, SQLite)  
**Backend:** FastAPI  
**Systems & Infra:** Docker, Linux, MLflow, DVC, Airflow  
**Tools:** Git, Jupyter Notebook, VS Code  

---

## Experience

**NLP Research Intern — Thapar Institute of Engineering & Technology (2025–Present)**  

- Built end-to-end data engineering pipelines for Punjabi LLM fine-tuning  
- Processed **16.2M+ tokens** with automated deduplication, normalization, and validation  
- Developed structured datasets for instruction tuning and evaluation workflows  
- Improved dataset quality and reproducibility for downstream training systems  

---

## Current Work & Interests

- LLM inference optimization (KV caching, memory-efficient decoding)
- Scalable ML systems and model serving architectures
- Dataset engineering for low-resource languages
- System-level aspects of AI safety, robustness, and reliability

---

## Links

- GitHub: https://github.com/manankapoor23  
- LinkedIn: https://www.linkedin.com/in/manan-kapoor-8545002a0/  
- Email: 23.kapoormanan@gmail.com
