# Hi, I'm Manan Kapoor   

 **Sophomore Engineering Student (COE)**  
 Thapar Institute of Engineering & Technology, India  
 Aspiring **Software Developer** | **AI/ML Research Enthusiast** | **Web Dev Explorer**

I love building things that *actually work* — from ML pipelines and datasets for LLMs to clean web projects and creative media.  
Currently exploring the intersection of **Machine Learning, LLMs, and real-world systems**.

---

##  Roles & Experience  

**Research Intern** — Thapar Institute of Engineering & Technology *(2025–Present)*  
- Built end-to-end **data engineering pipelines** for Punjabi LLM fine-tuning  
- Processed **16.2M+ tokens (1.1M sentences)** with deduplication & noise filtering  
- Designed **training-ready JSONL benchmarks** for instruction tuning & evaluation  
- Worked with NLP, statistics, hypothesis testing, and reproducible research workflows  

**Media Intern** — Escape Media Tech *(Jun–Jul 2025)*  
- Created 15+ short-form videos with **100K+ total views**  
- Handled on-ground media coverage across 3+ cities  
- Delivered end-to-end content from raw footage → platform-ready outputs  

**Clubs & Societies**  
- Core Member — **Echoes Club** (Creative Assistant) [2025]  
- Member — **Echoes Club** (Media & Content Team) [2024]  
- Core Member — **Saturnalia 2025** (Tech Team)  

 Photographer |  Videographer |  Creative Designer  

---

##  What I’m Currently Learning  

- **C++ & Data Structures / Algorithms**  
- **Machine Learning & Deep Learning**  
- **LLMs, Transformers, RAG & GenAI**  
- **Python for Data Science & Automation**  
- **SQL & Databases**  
- **Statistics & Hypothesis Testing**  
- **Photography & Cinematography**  
- Reducing my **Diet Coke dependency** (ongoing battle)

---
## 🛠 Tech Stack

### 💬 Languages
<p align="center">
  <img src="https://skillicons.dev/icons?i=cpp,python,js,r,html,css" />
</p>

### 🤖 ML / AI Frameworks
<p align="center">
  <img src="https://skillicons.dev/icons?i=pytorch,tensorflow" />
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
</p>

### 📊 Data Science
<p align="center">
  <img src="https://skillicons.dev/icons?i=matlab" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" />
  <img src="https://img.shields.io/badge/NLTK-154F5B?style=for-the-badge&logo=python&logoColor=white" />
</p>

### 🛠 Tools & DevOps
<p align="center">
  <img src="https://skillicons.dev/icons?i=git,github,docker,vscode,jupyter,postgres" />
</p>

### 🗄️ Databases
<p align="center">
  <img src="https://skillicons.dev/icons?i=mysql,sqlite,postgres" />
</p>
## 🧠 AI Systems & LLM Internals (Current Focus)

I’m exploring **how modern AI systems actually run under the hood** — not just how to call APIs.

My current focus is on **LLM inference, memory management, and production-scale design**, bridging **deep learning + systems engineering**.

### 🔍 What I’m Studying
- Autoregressive decoding in transformer models  
- **Key–Value (KV) cache mechanics**  
- Inference-time memory behavior  
- Latency vs throughput tradeoffs  
- Why naïve inference implementations break at scale  

I strongly believe **understanding inference is as important as training models**.

---

### 🔬 Recent Deep Dive: KV Cache (Hands-on)

I implemented and experimented with a **naive KV-cache** using open-source transformer models to understand real inference behavior.

**Key insights:**
- KV cache correctly avoids recomputing attention for past tokens  
- Naive KV cache **grows unbounded** in multi-turn conversations  
- In production:
  - Prompt & response lengths are unknown
  - Contiguous allocation becomes fragile
  - Memory fragmentation and waste increase over time
  - Decoder-side memory pressure continuously grows
- Framework-level KV caches abstract memory layout, limiting control  

 **Conclusion:** Naive KV caching is *correct*, but **not scalable**.

---

###  What I’m Exploring Next: Paged KV Cache

I’m now working on a **paged KV-cache design**, inspired by production inference engines, to understand:

- How fixed-size KV pages prevent fragmentation  
- Decoupling logical token order from physical memory  
- Prefix reuse: *compute once, reuse many times*  
- Reference counting & copy-on-write for safe sharing  
- How OS concepts (paging, virtual memory) apply directly to LLM inference  

> **KV cache enables reuse over time.  
> Paging enables reuse over space.**

---

### 🛠 Tech Stack (Systems + AI)
- Python  
- PyTorch  
- Hugging Face Transformers  
- Apple Silicon (CPU / MPS)  
- Inference debugging, profiling & benchmarking  
- API usage: **OpenAI SDK, Google APIs**, and modern ML tooling  

I prefer **correctness, clarity, and understanding** over chasing benchmarks.

---

###  What I Care About
- AI **systems**, not just AI models  
- How things **scale**, not just how they work once  
- Building mental models, not copying code  
- Treating CS fundamentals as **skills**, not subjects  

---

###  Philosophy
> *“Understanding how AI runs is as important as understanding how it learns.”*

## 🛠 Tech Stack  

### Languages
<p align="center">
  <img src="https://skillicons.dev/icons?i=cpp,python,js,r,html,css,sql" />
</p>

### ML / AI
- Machine Learning, Deep Learning, Neural Networks  
- Transformers, LLMs, RAG, Instruction Tuning  
- NLP, Dataset Engineering, Model Evaluation  

### Libraries & Tools
- Pandas, NumPy, Scikit-learn, PyTorch, Matplotlib  
- LangChain, OpenAI SDK, NLTK  
- Git, GitHub, Docker, VS Code, Jupyter, RStudio  

### CS Fundamentals
- DSA, OOP, OS, DBMS, Computer Networks  
- Probability & Statistics  

---

## 🧪 Featured Projects  

### 🔥 **Hestia — Fire Prediction & Analysis Model**
- End-to-end ML pipeline on environmental data  
- Feature analysis identified **temperature & RH** as key predictors  
- Focused on interpretability & early-warning insights  

### 🧾 **Punjabi Text Simplification Dataset (LLMs)**
- 16M+ token dataset built for supervised fine-tuning  
- Automated cleaning, deduplication & validation pipelines  
- Research-driven design based on peer-reviewed papers  

### 📊 **PunjabiSimplify-R**
- R-based framework to evaluate LLM text simplification  
- Used **paired t-tests**, descriptive statistics & readability metrics  

### 🎨 **Art Style Predictor**
- AI model for classifying artwork styles  
- Planned extensions to artist & emotion prediction  

### 📸 **Photography Portfolio**
- Experiments with light, framing, and visual storytelling  

---

## 📊 GitHub Stats  

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=manankapoor23&show_icons=true&theme=tokyonight" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=manankapoor23&theme=tokyonight" />
</p>

---

## 🌱 Currently Working On  

- Improving **GitHub repos & documentation**  
- Exploring **open-source contributions & hackathons**  
- Deep diving into **LLMs & Generative AI**  
- Building projects that combine **ML + systems + real data**

---

## 🤝 Connect With Me  

<p align="center">
  <a href="https://www.linkedin.com/in/manan-kapoor-8545002a0/">
    <img src="https://skillicons.dev/icons?i=linkedin" />
  </a>
  <a href="mailto:23.kapoormanan@gmail.com">
    <img src="https://skillicons.dev/icons?i=gmail" />
  </a>
  <a href="https://x.com/Manankap2311">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/x.svg" width="40" height="40"/>
  </a>
</p>

---

![snake gif](https://github.com/manankapoor23/manankapoor23/blob/output/github-snake-dark.svg)

