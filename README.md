<div align="center">
<a href="https://darukaa-biodiversity-intelligence.vercel.app/">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#166534" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="100" height="100">
    <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.4 19 2c2 2 2.6 3.5 3.7 9.2a7 7 0 0 1-13.9 8.8z"></path>
    <path d="M2 21c0-3 1.85-5.36 5.08-6"></path>
  </svg>
</a>

<h1 style="font-size: 40px; color: #166534; margin-top: 10px;">Darukaa.Earth | AI Biodiversity Intelligence</h1>

<p align="center" style="font-size: 1.1rem; margin-top: 10px;">
<b>We are building an AI Environmental Scientist, not a generic chatbot.</b><br>
A knowledge-driven Agentic RAG system that reasons about real-world environmental problems.
</p>

<p align="center">
<a href="https://darukaa-biodiversity-intelligence.vercel.app/">
<img src="https://img.shields.io/badge/🚀_Launch-Live_App-166534?style=for-the-badge&logoColor=white" height="35" />
</a>
&nbsp;&nbsp;
<a href="https://darukaa-biodiversity-intelligence-d8m7.onrender.com/docs">
<img src="https://img.shields.io/badge/⚙️_Backend-API_Docs-0891b2?style=for-the-badge&logo=fastapi&logoColor=white" height="35" />
</a>
</p>
</div>

<br />

<div align="center">
<h2 style="font-size: 28px; margin-bottom: 5px;">The Objective</h2>
<p style="font-size: 16px; font-style: italic; margin-bottom: 30px; max-width: 800px;">
To evaluate multi-metric environmental data (soil health, climate, land use) and generate actionable, evidence-backed recommendations grounded in scientific guidelines (FAO, IPCC, UNEP).
</p>
</div>

<br />
<hr />
<br />

<div align="center">
<h2 style="font-size: 34px; color: #1F2933; margin-bottom: 10px;">🚀 Core Capabilities </h2>
<p style="color: #666; font-size: 18px; max-width: 800px;">
Directly addressing the Darukaa Hackathon Evaluation Criteria.
</p>
</div>
<br />

<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tr>
<td width="45%" valign="middle" style="padding-right: 20px;">
<h3 style="font-size: 24px; color: #1F2933; margin-bottom: 8px;">🧠 1. Conversational Intelligence</h3>
<p style="margin-bottom: 15px;">
<code style="background: #eff6ff; color: #1d4ed8; padding: 4px 8px; border-radius: 4px; font-weight: bold;">Multi-turn Memory</code>
<code style="background: #eff6ff; color: #1d4ed8; padding: 4px 8px; border-radius: 4px; font-weight: bold;">Context Validator</code>
</p>
<p style="font-size: 16px; color: #555; line-height: 1.6;">
<b>No Premature Advice.</b><br>
The system actively identifies missing environmental variables (like rainfall, SOC %, or land use). If a user inputs an incomplete query (e.g., <i>"Biodiversity is declining"</i>), the AI intelligently asks clarifying follow-up questions before ever providing a recommendation.
</p>
</td>
<td width="55%" valign="middle" style="padding-left: 10px;">
<div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 15px; background: #f8fafc; font-family: monospace;">
<b>User:</b> Biodiversity is declining on my land.<br><br>
<b>AI Scientist:</b> To give you a scientifically accurate recommendation, I need a bit more context. Could you share your soil organic carbon percent and soil moisture level?
</div>
</td>
</tr>
</table>

<br /><br />

<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tr>
<td width="55%" valign="middle" style="padding-right: 20px;">
<div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 15px; background: #f8fafc; font-family: monospace;">
<b>Input Variables:</b><br>
- Rainfall: Low (< 600mm)<br>
- SOC: 0.3% (Critical)<br>
- Crop: Monoculture Wheat<br><br>
<b>Action:</b> Agroforestry + Legumes<br>
<b>Impact:</b> +15-25% SOC over 3-5 yrs.
</div>
</td>
<td width="45%" valign="middle" style="padding-left: 10px;">
<h3 style="font-size: 24px; color: #1F2933; margin-bottom: 8px;">📊 2. Multi-Metric Reasoning</h3>
<p style="margin-bottom: 15px;">
<code style="background: #ecfdf5; color: #047857; padding: 4px 8px; border-radius: 4px; font-weight: bold;">Cross-variable Analysis</code>
<code style="background: #ecfdf5; color: #047857; padding: 4px 8px; border-radius: 4px; font-weight: bold;">Non-Obvious Actions</code>
</p>
<p style="font-size: 16px; color: #555; line-height: 1.6;">
<b>Connecting the Dots.</b><br>
The reasoning engine explicitly connects multiple variables to avoid single-variable shallow answers. It understands that high rainfall + healthy soil requires different interventions than semi-arid degraded land.
</p>
</td>
</tr>
</table>

<br /><br />

<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tr>
<td width="45%" valign="middle" style="padding-right: 20px;">
<h3 style="font-size: 24px; color: #1F2933; margin-bottom: 8px;">📚 3. Evidence-Backed RAG</h3>
<p style="margin-bottom: 15px;">
<code style="background: #fef2f2; color: #b91c1c; padding: 4px 8px; border-radius: 4px; font-weight: bold;">ChromaDB</code>
<code style="background: #fef2f2; color: #b91c1c; padding: 4px 8px; border-radius: 4px; font-weight: bold;">Scientific Grounding</code>
</p>
<p style="font-size: 16px; color: #555; line-height: 1.6;">
<b>Zero Hallucinations.</b><br>
Recommendations are powered by a strictly constrained Retrieval-Augmented Generation pipeline. Every actionable insight is directly cited from indexed global guidelines (FAO, IPCC, UNEP), complete with measurable impacts and time horizons.
</p>
</td>
<td width="55%" valign="middle" style="padding-left: 10px;">
<div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 15px; background: #f8fafc; font-family: monospace;">
<b>Expected Output Format:</b><br>
- Recommendation<br>
- Scientific Reasoning (Why it works)<br>
- Impacted Metrics<br>
- Time Horizon<br>
- Authoritative Sources (Citations)
</div>
</td>
</tr>
</table>


<br />
<hr />
<br />

<div align="center">
  <h2 style="font-size: 34px; color: #1F2933; margin-bottom: 10px;">🛠️ Tech Stack & System Architecture</h2>
  <p style="color: #666; font-size: 18px; max-width: 800px;">
    A purpose-built <b>Agentic RAG architecture</b> designed for complex environmental reasoning, structured knowledge retrieval, and edge-optimized delivery.
  </p>
</div>
<br />

<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tr>
<td width="50%" valign="top" style="padding-right: 10px; padding-bottom: 20px;">
<div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%;">
<h3 style="font-size: 20px; color: #1F2933; margin-bottom: 15px; border-bottom: 3px solid #61DAFB; display: inline-block; padding-bottom: 5px;">💻 Client-Side (Frontend)</h3>

<ul style="color: #555; line-height: 1.6; margin-left: -20px; list-style-type: none;">
<li style="margin-bottom: 12px;">
<code style="background: #e0f2fe; color: #0284c7; padding: 3px 6px; border-radius: 4px;">React.js (Vite)</code><br>
<span style="font-size: 14px;">Delivers a lightning-fast Single Page Application (SPA) experience with dynamic state management for multi-turn conversational context.</span>
</li>

<li style="margin-bottom: 12px;">
<code style="background: #e0f2fe; color: #0284c7; padding: 3px 6px; border-radius: 4px;">Dynamic Sidebar Sync</code><br>
<span style="font-size: 14px;">Automatically extracts and tracks environmental parameters (pH, SOC, Rainfall, etc.) from the ongoing conversation to visualize the AI's current understanding.</span>
</li>
</ul>
</div>
</td>

<td width="50%" valign="top" style="padding-left: 10px; padding-bottom: 20px;">
<div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%;">
<h3 style="font-size: 20px; color: #1F2933; margin-bottom: 15px; border-bottom: 3px solid #68A063; display: inline-block; padding-bottom: 5px;">⚙️ Server-Side (Backend)</h3>

<ul style="color: #555; line-height: 1.6; margin-left: -20px; list-style-type: none;">
<li style="margin-bottom: 12px;">
<code style="background: #dcfce7; color: #166534; padding: 3px 6px; border-radius: 4px;">FastAPI (Python 3.11)</code><br>
<span style="font-size: 14px;">High-performance, async RESTful API architecture handling session states, prompt orchestration, and vector search operations.</span>
</li>

<li style="margin-bottom: 12px;">
<code style="background: #dcfce7; color: #166534; padding: 3px 6px; border-radius: 4px;">Multipart Form Handlers</code><br>
<span style="font-size: 14px;">Robust middleware supporting complex data payloads and file ingestion pipelines for dynamic knowledge base expansion.</span>
</li>
</ul>
</div>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="padding-right: 10px; padding-bottom: 20px;">
<div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #faf5ff; height: 100%;">
<h3 style="font-size: 20px; color: #1F2933; margin-bottom: 15px; border-bottom: 3px solid #8E75B2; display: inline-block; padding-bottom: 5px;">🧠 AI Core & Orchestration</h3>

<ul style="color: #555; line-height: 1.6; margin-left: -20px; list-style-type: none;">
<li style="margin-bottom: 12px;">
<code style="background: #f3e8ff; color: #6b21a8; padding: 3px 6px; border-radius: 4px;">Cohere Semantic API</code><br>
<span style="font-size: 14px;">Powers the core reasoning engine. Used for intent classification (Recommendation Request vs. Context Update) and generating strictly constrained JSON schemas.</span>
</li>

<li style="margin-bottom: 12px;">
<code style="background: #f3e8ff; color: #6b21a8; padding: 3px 6px; border-radius: 4px;">Agentic Gateway</code><br>
<span style="font-size: 14px;">A custom middleware that blocks premature recommendations, forcing the LLM to request critical missing variables (e.g., soil moisture) before executing a semantic search.</span>
</li>
</ul>
</div>
</td>

<td width="50%" valign="top" style="padding-left: 10px; padding-bottom: 20px;">
<div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%;">
<h3 style="font-size: 20px; color: #1F2933; margin-bottom: 15px; border-bottom: 3px solid #FFCA28; display: inline-block; padding-bottom: 5px;">🗄️ Database & Schema Design</h3>

<ul style="color: #555; line-height: 1.6; margin-left: -20px; list-style-type: none;">
<li style="margin-bottom: 12px;">
<code style="background: #fffbeb; color: #b45309; padding: 3px 6px; border-radius: 4px;">ChromaDB (Vector DB)</code><br>
<span style="font-size: 14px;">Stores highly dense, multi-metric embeddings of global environmental reports.</span>
</li>
<li style="margin-bottom: 12px;">
<code style="background: #fffbeb; color: #b45309; padding: 3px 6px; border-radius: 4px;">Chunking & Metadata Schema</code><br>
<span style="font-size: 14px;">Documents are ingested using precise chunking (800 tokens, 150 overlap). Each vector is strictly mapped to a metadata schema: <code>{ source_id: string, organization: string, url: string }</code> ensuring zero-hallucination citation traceability.</span>
</li>
</ul>
</div>
</td>
</tr>
</table>

<br />
<hr />

<br />
<div align="center">
  <h2 style="font-size: 34px; color: #1F2933; margin-bottom: 10px;">⚡ CI/CD & Production Pipeline</h2>
  <p style="color: #666; font-size: 18px; max-width: 800px;">
    Automated zero-downtime deployment strategy.
  </p>
</div>
<br />

<table border="0" width="100%" cellspacing="0" cellpadding="0">
<tr>
<td width="100%" valign="top">
<ul style="color: #555; line-height: 1.8; font-size: 16px;">
  <li><b>Version Control:</b> GitHub acts as the single source of truth for the monorepo architecture.</li>
  <li><b>Frontend Pipeline (Vercel):</b> Webhook triggers an automated Vite build process upon every push to the <code>main</code> branch, deploying to Edge networks.</li>
  <li><b>Backend Pipeline (Render):</b> Continuous integration initiates a fresh Python environment build, package installation via <code>requirements.txt</code>, and Uvicorn container restart.</li>
  <li><b>Availability:</b> An external HTTP ping monitor (UptimeRobot) actively pings the backend every 5 minutes to prevent cold-starts on the free-tier container.</li>
</ul>
</td>
</tr>
</table>

<br />
<hr />

<br />
<div align="center">
  <h2 style="font-size: 34px; color: #1F2933; margin-bottom: 10px;">⚡ Getting Started & Local Setup</h2>
  <p style="color: #666; font-size: 18px; max-width: 800px;">
    Follow this step-by-step guide to run the <b>Darukaa AI Scientist Ecosystem</b> on your local machine.
  </p>
</div>
<br />

<h3 style="font-size: 24px; color: #1F2933; border-left: 5px solid #166534; padding-left: 10px;">📋 Prerequisites</h3>
<p style="color: #555; font-size: 16px;">Before you begin, ensure you have the following installed:</p>
<ul style="color: #555; line-height: 1.8;">
  <li><b>Python (v3.11+):</b> <a href="https://www.python.org/downloads/" target="_blank">Download Here</a></li>
  <li><b>Node.js (v18+):</b> <a href="https://nodejs.org/" target="_blank">Download Here</a></li>
  <li><b>Git:</b> <a href="https://git-scm.com/" target="_blank">Download Here</a></li>
</ul>

<br />

<h3 style="font-size: 24px; color: #1F2933; border-left: 5px solid #2ea44f; padding-left: 10px;">🚀 Step 1: Clone the Repository</h3>
<p style="color: #555;">Open your terminal and run the following commands:</p>



git clone [https://github.com/srishtiii2108/darukaa-biodiversity-intelligence.git](https://github.com/srishtiii2108/darukaa-biodiversity-intelligence.git)
```
cd darukaa-biodiversity-intelligence
```
```
cd backend
python -m venv venv
```
Activate the virtual environment:
```
Windows: venv\Scripts\activate
```
```
Mac/Linux: source venv/bin/activate
```
Install Dependencies:

```
pip install -r requirements.txt
```
🔑 Configuring Backend Environment Variables
Create a file named .env in the backend directory.

Copy this into your backend/.env file:

Code snippet
```
COHERE_API_KEY=your_cohere_api_key_here
```
Start the Backend Server:

```
uvicorn main:app --reload --port 8000
```
Terminal should say: Uvicorn running on http://127.0.0.1:8000

```
cd frontend
```
```
npm install
```
🔑 Configuring Frontend Environment Variables
Create a file named .env in the frontend directory and add the backend URL:
```
VITE_API_BASE_URL=http://127.0.0.1:8000
```
Start the Frontend:
```
npm run dev
```

<br />
<hr style="border: 1px solid #ddd;" />
<br />

<div align="center">
  <h2 style="font-size: 30px; color: #1F2933; margin-bottom: 20px;">🎯 Conclusion: What We Achieved</h2>
  <p style="color: #555; font-size: 16px; line-height: 1.6; max-width: 800px;">
    I successfully engineered a system that transcends standard LLM wrappers. By integrating a <b>strict Agentic RAG architecture</b>, the Darukaa AI Scientist evaluates up to four distinct environmental variables simultaneously, refuses to hallucinate generic advice, and proactively demands missing context. Every recommendation is anchored in credible, retrieved scientific literature, fulfilling the exact mandate of creating an intelligent, reasoning-driven environmental engine.
  </p>
</div>

<br />

<div align="center">
  <h3 style="font-size: 24px; color: #1F2933; margin-bottom: 10px;">🏆 Hackathon Context</h3>
  <p style="color: #555; font-size: 16px; line-height: 1.6; max-width: 700px;">
    This repository serves as the official submission for the <b>Darukaa.Earth AI Biodiversity Intelligence Chatbot Challenge</b>. All deliverables, including the live Vercel frontend, Render backend, and complete source code, have been deployed and documented as per the strict evaluation criteria. 
  </p>
</div>

<br />
<br />

<div align="center">
  <p style="font-size: 12px; color: #999;">
    Licensed under the <b>MIT License</b>. Copyright © 2026 Darukaa AI Scientist | Akshat Sharma.
  </p>
</div>
<br />
