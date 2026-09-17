<p align="center">
  <img src="assets/hero.svg" width="100%" alt="Adwait Desai - AI Engineer, Backend and Cloud Systems" />
</p>

<p align="center">
  <a href="https://linkedin.com/in/adwaitpdesai"><img src="https://img.shields.io/badge/LinkedIn-161b22?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>&nbsp;
  <a href="mailto:adwaitd393@gmail.com"><img src="https://img.shields.io/badge/Email-161b22?style=for-the-badge&logo=gmail&logoColor=EA4335" alt="Email" /></a>&nbsp;
  <a href="https://github.com/adwait39?tab=repositories"><img src="https://img.shields.io/badge/Repositories-161b22?style=for-the-badge&logo=github&logoColor=white" alt="Repositories" /></a>&nbsp;
  <img src="https://komarev.com/ghpvc/?username=adwait39&label=Profile%20views&color=1f6feb&style=for-the-badge" alt="profile views" />
</p>

<br/>

<img src="assets/section-about.svg" width="100%" alt="About" />

<table>
<tr>
<td width="60%" valign="top">

I am a Master's student in Computer Science at the **University of Colorado Boulder** (May 2027) and an **AI Engineer Intern at C-Suite Comp**, where I design and operate production data and LLM pipelines on Google Cloud.

I like problems that sit between machine learning and infrastructure: making retrieval systems fast and traceable, moving heavy compute off the request path, and putting guardrails and approval gates around agents so they can be trusted with real systems.

**Currently building:** an agentic incident-response platform that works an outage the way an on-call engineer does — triage, diagnose, verify, fix — and requires human approval before touching anything live.

</td>
<td width="40%" valign="top">

<table>
  <tr><td><b>Role</b></td><td>AI Engineer Intern, C-Suite Comp</td></tr>
  <tr><td><b>Education</b></td><td>M.S. CS, CU Boulder (GPA 3.72)<br/>B.E. IT, PICT Pune (8.23/10)</td></tr>
  <tr><td><b>Research</b></td><td>Patent co-author, 2 publications</td></tr>
  <tr><td><b>Impact</b></td><td>Data behind research cited by Bloomberg and CFO.com</td></tr>
  <tr><td><b>Location</b></td><td>Boulder, CO (remote-friendly)</td></tr>
  <tr><td><b>Contact</b></td><td><a href="mailto:adwaitd393@gmail.com">adwaitd393@gmail.com</a></td></tr>
</table>

</td>
</tr>
</table>

<br/>

<img src="assets/section-experience.svg" width="100%" alt="Experience" />

<table>
  <tr>
    <th align="left" width="24%">Role</th>
    <th align="left" width="18%">Period</th>
    <th align="left">What I did</th>
  </tr>
  <tr>
    <td><b>AI Engineer Intern</b><br/><sub>C-Suite Comp · Houston, TX (remote)</sub></td>
    <td>Jul 2026 – Present</td>
    <td>
      Built and operate 4 production data and LLM pipelines on GCP (Cloud Run, Scheduler, Cloud Build, Secret Manager, Pub/Sub) over <b>609K+ SEC filings across 4,850+ companies</b>.<br/>
      Rebuilt the RAG document-search to answer across 10–30 companies at once: a 20-company build went from <b>15 min to 3</b>, request latency from <b>108 s to 18.5 s</b>, repeat loads under 1 s via cached FAISS indexes that merge in 0.01 s.<br/>
      Designed sharded, checkpointed, idempotent processing with distributed locking on Cloud Storage; cut projected annual AI cost from <b>~$20K to $75</b>. The resulting dataset underpins research cited by Bloomberg and CFO.com.
    </td>
  </tr>
  <tr>
    <td><b>Graduate Research Assistant</b><br/><sub>Quantitative ML · CU Boulder</sub></td>
    <td>May 2026 – Aug 2026</td>
    <td>
      Built a dividend-announcement forecasting system over <b>340+ companies and 50K+ records</b> (LightGBM ranking, ensembles, calibrated hazard models): <b>83%</b> date accuracy, <b>91%</b> precision on rare events, 15+ pts over the best classical baseline.<br/>
      Separated offline computation from serving with versioned artifacts and statistically gated releases; built the React research dashboard on top.
    </td>
  </tr>
  <tr>
    <td><b>Graduate Teaching Assistant</b><br/><sub>Remote Sensing Data Analysis · CU Boulder</sub></td>
    <td>Aug 2026 – Present</td>
    <td>Help 100+ students debug Python/MATLAB implementations of 10+ ML algorithms (PCA, clustering, SVMs, random forests, neural networks) across 6 course modules; review code and run technical interviews for project work.</td>
  </tr>
  <tr>
    <td><b>Full Stack Engineer Intern</b><br/><sub>Techpeek · Bengaluru, India</sub></td>
    <td>Sep 2024 – Jan 2025</td>
    <td>
      Built the billing, usage-metering and LLM-gateway backend for a 3-tier AI subscription product: 25+ REST endpoints, idempotent webhook-driven payments (<b>10,000 replayed events, zero duplicate transitions</b>, 50+ integration tests), semantic caching and model routing that cut repeat model calls 30%+.<br/>
      Load-tested at <b>300+ req/s under 200 ms p95</b>; Redis caching took hot-path latency from 400 ms to 120 ms. Shipped the Svelte front end for the same flows.
    </td>
  </tr>
</table>

<br/>

<img src="assets/section-projects.svg" width="100%" alt="Projects" />

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Distributed Data Drift Detection Platform</h3>
      <p><a href="https://github.com/adwait39/drift-detection-adwait"><img src="https://img.shields.io/badge/Source-161b22?style=flat-square&logo=github&logoColor=white" /></a> <img src="https://img.shields.io/badge/Jan_–_Mar_2026-161b22?style=flat-square" /></p>
      <p>Event-driven MLOps platform with a 5-service architecture (API, workers, message broker, object storage, dashboard) that runs four drift detectors per dataset: <b>semantic, lexical, topic and out-of-distribution</b>. Uploads return immediately; background workers compute transformer embeddings, persist metrics to Postgres, and raise alerts with retries, idempotency and dead-letter queues.</p>
      <p>
        <img src="https://img.shields.io/badge/FastAPI-161b22?style=flat-square&logo=fastapi&logoColor=009688" />
        <img src="https://img.shields.io/badge/Pub%2FSub-161b22?style=flat-square&logo=googlecloud&logoColor=4285F4" />
        <img src="https://img.shields.io/badge/RabbitMQ-161b22?style=flat-square&logo=rabbitmq&logoColor=FF6600" />
        <img src="https://img.shields.io/badge/MinIO-161b22?style=flat-square&logo=minio&logoColor=C72E49" />
        <img src="https://img.shields.io/badge/PostgreSQL-161b22?style=flat-square&logo=postgresql&logoColor=4169E1" />
        <img src="https://img.shields.io/badge/Terraform-161b22?style=flat-square&logo=terraform&logoColor=844FBA" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>Music Separation as a Service</h3>
      <p><a href="https://github.com/adwait39/Music-separation-as-a-Service"><img src="https://img.shields.io/badge/Source-161b22?style=flat-square&logo=github&logoColor=white" /></a> <img src="https://img.shields.io/badge/Sep_–_Dec_2025-161b22?style=flat-square" /></p>
      <p>Distributed audio-processing backend on <b>Kubernetes / GKE</b> that splits songs into four stems with Meta's Demucs. Jobs run 3–4x the audio duration, so they are pushed through Redis queues to worker containers and results land in MinIO; API, queue, storage and model workers scale independently. Instrumented CPU, memory, queue depth, latency and failure rate with Prometheus and Grafana.</p>
      <p>
        <img src="https://img.shields.io/badge/Kubernetes-161b22?style=flat-square&logo=kubernetes&logoColor=326CE5" />
        <img src="https://img.shields.io/badge/GKE-161b22?style=flat-square&logo=googlecloud&logoColor=4285F4" />
        <img src="https://img.shields.io/badge/Redis-161b22?style=flat-square&logo=redis&logoColor=DC382D" />
        <img src="https://img.shields.io/badge/MinIO-161b22?style=flat-square&logo=minio&logoColor=C72E49" />
        <img src="https://img.shields.io/badge/Prometheus-161b22?style=flat-square&logo=prometheus&logoColor=E6522C" />
        <img src="https://img.shields.io/badge/Grafana-161b22?style=flat-square&logo=grafana&logoColor=F46800" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Agentic AI Incident Response Platform</h3>
      <p><img src="https://img.shields.io/badge/In_progress-161b22?style=flat-square&logo=githubactions&logoColor=d29922" /> <img src="https://img.shields.io/badge/Design_doc_first-161b22?style=flat-square" /></p>
      <p>An on-call copilot. An Alertmanager webhook lands in FastAPI and a <b>LangGraph</b> state machine works the incident in four stages — triage, diagnose, verify, fix — reading logs, metrics, Kubernetes state, deployment history and runbooks, ranking root-cause hypotheses against real evidence, and proposing a remediation that runs only after <b>explicit human approval</b>. Then it verifies recovery and writes the post-mortem.</p>
      <p>
        <img src="https://img.shields.io/badge/LangGraph-161b22?style=flat-square&logo=langchain&logoColor=1C3C3C" />
        <img src="https://img.shields.io/badge/FastAPI-161b22?style=flat-square&logo=fastapi&logoColor=009688" />
        <img src="https://img.shields.io/badge/Prometheus-161b22?style=flat-square&logo=prometheus&logoColor=E6522C" />
        <img src="https://img.shields.io/badge/Kubernetes-161b22?style=flat-square&logo=kubernetes&logoColor=326CE5" />
        <img src="https://img.shields.io/badge/PostgreSQL-161b22?style=flat-square&logo=postgresql&logoColor=4169E1" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>Multi-Agent Financial Research System</h3>
      <p><img src="https://img.shields.io/badge/Private-161b22?style=flat-square&logo=github&logoColor=8b949e" /> <img src="https://img.shields.io/badge/May_–_Aug_2026-161b22?style=flat-square" /></p>
      <p>Four cooperating agents research a company end to end: a planner, an evidence-gatherer wired to 8+ tools (SEC filings, market data, financial APIs), an analyst, and a fact-checker. Against a single-agent baseline on 100+ research questions it completed <b>87% of tasks (+15 pts)</b> with <b>95% of claims backed by a source citation</b>.</p>
      <p>
        <img src="https://img.shields.io/badge/Python-161b22?style=flat-square&logo=python&logoColor=3776AB" />
        <img src="https://img.shields.io/badge/Tool_calling-161b22?style=flat-square" />
        <img src="https://img.shields.io/badge/MCP-161b22?style=flat-square" />
        <img src="https://img.shields.io/badge/FAISS-161b22?style=flat-square&logo=meta&logoColor=0467DF" />
        <img src="https://img.shields.io/badge/LLM--as--a--Judge-161b22?style=flat-square" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>AI Resume Screening and Candidate Matching</h3>
      <p><img src="https://img.shields.io/badge/Private-161b22?style=flat-square&logo=github&logoColor=8b949e" /> <img src="https://img.shields.io/badge/May_–_Aug_2026-161b22?style=flat-square" /></p>
      <p>Multi-stage matcher over <b>5M+ candidate–job interactions and 100K+ postings</b>: two-tower embedding retrieval with FAISS narrows the pool by 99.9% while keeping 97% of true matches in the top 100, then LightGBM reranks on 30+ behavioral, contextual and profile features (<b>+18% NDCG@10</b> over baselines). Served under 80 ms p95 at 1,000+ req/s via FastAPI, Redis and precomputed embeddings.</p>
      <p>
        <img src="https://img.shields.io/badge/PyTorch-161b22?style=flat-square&logo=pytorch&logoColor=EE4C2C" />
        <img src="https://img.shields.io/badge/FAISS-161b22?style=flat-square&logo=meta&logoColor=0467DF" />
        <img src="https://img.shields.io/badge/LightGBM-161b22?style=flat-square" />
        <img src="https://img.shields.io/badge/FastAPI-161b22?style=flat-square&logo=fastapi&logoColor=009688" />
        <img src="https://img.shields.io/badge/Redis-161b22?style=flat-square&logo=redis&logoColor=DC382D" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>Network Protocol Regression and Failure-Validation Platform</h3>
      <p><img src="https://img.shields.io/badge/Private-161b22?style=flat-square&logo=github&logoColor=8b949e" /> <img src="https://img.shields.io/badge/Oct_–_Dec_2025-161b22?style=flat-square" /></p>
      <p>A routing testbed of <b>20+ containerized routers</b> implementing OSPF-style link-state routing, neighbor discovery, topology flooding and automatic recomputation, validated by 100+ PyTest/Scapy regression tests and 50+ injected link and node failures. An Angular + RxJS + WebSockets dashboard renders the live topology and replaces CLI setup for failure scenarios with one or two clicks.</p>
      <p>
        <img src="https://img.shields.io/badge/Angular-161b22?style=flat-square&logo=angular&logoColor=DD0031" />
        <img src="https://img.shields.io/badge/TypeScript-161b22?style=flat-square&logo=typescript&logoColor=3178C6" />
        <img src="https://img.shields.io/badge/RxJS-161b22?style=flat-square&logo=reactivex&logoColor=B7178C" />
        <img src="https://img.shields.io/badge/Docker-161b22?style=flat-square&logo=docker&logoColor=2496ED" />
        <img src="https://img.shields.io/badge/Scapy-161b22?style=flat-square&logo=python&logoColor=3776AB" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Automated Cloud Infrastructure Deployment</h3>
      <p><a href="https://github.com/adwait39/automated-cloud-infra-deployment"><img src="https://img.shields.io/badge/Source-161b22?style=flat-square&logo=github&logoColor=white" /></a></p>
      <p>Google Cloud automation through the Compute Engine Python API: provisions a VM, installs an app from git, opens firewall rules, snapshots the VM into a reusable image, benchmarks cold-start across instances, and uses IAM service accounts so a VM can create further VMs.</p>
      <p>
        <img src="https://img.shields.io/badge/Google_Cloud-161b22?style=flat-square&logo=googlecloud&logoColor=4285F4" />
        <img src="https://img.shields.io/badge/IAM-161b22?style=flat-square&logo=googlecloud&logoColor=EA4335" />
        <img src="https://img.shields.io/badge/Python-161b22?style=flat-square&logo=python&logoColor=3776AB" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>Next Play — Kanban Task Board</h3>
      <p><a href="https://github.com/adwait39/next-play"><img src="https://img.shields.io/badge/Source-161b22?style=flat-square&logo=github&logoColor=white" /></a></p>
      <p>Linear-style board with drag-and-drop columns, priorities, due dates and overdue indicators. Anonymous guest auth with per-user isolation through <b>Supabase Row Level Security</b>; responsive from 320 px to ultrawide with dark and light modes.</p>
      <p>
        <img src="https://img.shields.io/badge/React_19-161b22?style=flat-square&logo=react&logoColor=61DAFB" />
        <img src="https://img.shields.io/badge/TypeScript-161b22?style=flat-square&logo=typescript&logoColor=3178C6" />
        <img src="https://img.shields.io/badge/Supabase-161b22?style=flat-square&logo=supabase&logoColor=3ECF8E" />
        <img src="https://img.shields.io/badge/Vite-161b22?style=flat-square&logo=vite&logoColor=646CFF" />
      </p>
    </td>
  </tr>
</table>

<p align="right"><sub>Also on GitHub: <a href="https://github.com/adwait39/Elite-Estate">Elite Estate</a> (MERN real-estate marketplace) · <a href="https://github.com/adwait39/evenza">Evenza</a> (Angular)</sub></p>

<br/>

<img src="assets/section-skills.svg" width="100%" alt="Skills" />

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,ts,js,java,cpp,go,matlab,bash,fastapi,flask,django,nodejs,express,react,angular,svelte,redux,rxjs,tailwind,postgres,mongodb,redis,rabbitmq,pytorch,sklearn,tensorflow,gcp,aws,docker,kubernetes,terraform,prometheus,grafana,githubactions,git,linux&theme=dark&perline=12" alt="tech stack icons" />
</p>

<table>
  <tr>
    <td width="25%" valign="top"><b>LLM and Agentic AI</b><br/><sub>RAG · multi-agent orchestration · tool calling · MCP · structured outputs · guardrails and approval gates · semantic caching · model routing · LLM inference gateways · LLM-as-a-Judge · human-agreement scoring · regression testing for LLM systems</sub></td>
    <td width="25%" valign="top"><b>Retrieval and ML</b><br/><sub>FAISS · BM25 · dense embeddings · hybrid retrieval · reranking · chunking strategy · deduplication and data-quality gates · LightGBM · ensembles and ranking models · calibrated probabilities · hazard modeling · time-aware validation · feature ablation · PyTorch · scikit-learn · Pandas · NumPy</sub></td>
    <td width="25%" valign="top"><b>Backend and Data</b><br/><sub>Python · TypeScript · Java · C++ · Go · SQL · FastAPI · Flask · Django · Node.js · Express · REST · webhooks · auth · rate limiting · idempotency · pagination · PostgreSQL · MongoDB Atlas · Redis · MinIO · RabbitMQ · Google Pub/Sub · worker queues · event-driven architecture · query batching</sub></td>
    <td width="25%" valign="top"><b>Cloud, DevOps and Frontend</b><br/><sub>GCP (Cloud Run, Scheduler, Cloud Build, Artifact Registry, Secret Manager, VPC) · AWS · Docker · Kubernetes / GKE · Terraform · CI/CD · autoscaling · distributed locking · checkpointing · dead-letter queues · OpenTelemetry · Prometheus · Grafana · React · Angular · Svelte/SvelteKit · Redux Toolkit · RxJS · WebSockets · Tailwind · PyTest · Playwright · React Testing Library · load testing · fault injection</sub></td>
  </tr>
</table>

<br/>

<img src="assets/section-achievements.svg" width="100%" alt="Research and Achievements" />

<table>
  <tr>
    <td width="50%" valign="top">
      <b>Patent</b> — co-author of patented research on NLP and information-retrieval systems, filed by the sponsoring company and shipped as a live commercial product.<br/><br/>
      <b>Publications</b> — two international publications: <i>Journal of Scientific Computing</i> and <i>Delving Deeper into Semantic Web and Ontologies</i>.<br/><br/>
      <b>Research impact</b> — built the data infrastructure behind executive-compensation research cited by <b>Bloomberg</b> and <b>CFO.com</b>.
    </td>
    <td width="50%" valign="top">
      <b>Competitions</b> — Top 10, AWS GameDay (Feb 2026) · 3rd place, PICT Hackathon (Mar 2025) · Finalist, PICT poster competition.<br/><br/>
      <b>Teaching</b> — Course Assistant, MCEN 3030 at CU Boulder (200+ students) · ML instructor for 80+ juniors at PICT · Graduate TA, Remote Sensing Data Analysis.<br/><br/>
      <b>Education</b> — M.S. Computer Science, University of Colorado Boulder, 2025–2027 (GPA 3.72) · B.E. Information Technology, Pune Institute of Computer Technology, 2021–2025 (8.23/10).
    </td>
  </tr>
</table>

<br/>

<img src="assets/section-github.svg" width="100%" alt="GitHub Activity" />

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=adwait39&theme=github_dark" alt="profile details" />
</p>
<p align="center">
  <img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=adwait39&theme=github_dark" alt="stats" />
  <img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=adwait39&theme=github_dark" alt="repos per language" />
  <img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=adwait39&theme=github_dark" alt="most commit language" />
</p>

<p align="center">
  <img src="https://github.com/adwait39/adwait39/blob/output/github-contribution-grid-snake-dark.svg" alt="contribution snake" />
</p>

<br/>

<p align="center">
  <img src="assets/footer.svg" width="100%" alt="Open to AI, backend and platform engineering roles" />
</p>
