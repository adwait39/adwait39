<h1 align="center">Hi 👋, I'm Adwait Desai</h1>
<h3 align="center">I build cloud-native ML systems and the tooling that keeps them healthy in production.</h3>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=adwait39&label=Profile%20views&color=0e75b6&style=flat" alt="profile views" />
</p>

<p align="center">
  <img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="480" alt="coding" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/YOUR-LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:adwaitd393@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://YOUR-PORTFOLIO-URL"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" /></a>
</p>

---

## 🧑‍💻 About me

- 🎓 Master's student in Computer Science — focused on **distributed systems, MLOps and cloud infrastructure**
- 🔭 Currently building an **Agentic AI Incident Response Platform** — a LangGraph agent that triages Prometheus alerts, forms hypotheses from logs/metrics/traces, and proposes a fix behind a human-in-the-loop approval gate
- 🌱 Deepening my skills in **Kubernetes, observability (Prometheus / Grafana / OpenTelemetry) and LLM agents**
- 💬 Ask me about FastAPI, Kubernetes, GCP, React, and turning ML research into services
- 📫 Reach me at **adwaitd393@gmail.com**
- ℹ️ Some of the projects on my resume are private (client / coursework) — happy to walk through them on a call

---

## 🚀 Featured projects

<table>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🔍 Data Drift Detection System</h3>
      <p align="center">
        <a href="https://github.com/adwait39/drift-detection-adwait"><img src="https://img.shields.io/badge/View_Repo-181717?style=for-the-badge&logo=github" /></a>
      </p>
      <p>Production-style MLOps pipeline that watches for <b>semantic, lexical, topic and out-of-distribution drift</b> between a baseline dataset and new incoming data. Jobs are queued through Google Pub/Sub, datasets live in MinIO, workers compute transformer embeddings, and results land in Postgres with optional Gemini summaries and email/Slack alerts.</p>
      <p align="center">
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white" />
        <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" />
        <img src="https://img.shields.io/badge/Google_Pub%2FSub-4285F4?style=flat&logo=googlecloud&logoColor=white" />
        <img src="https://img.shields.io/badge/MinIO-C72E49?style=flat&logo=minio&logoColor=white" />
        <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white" />
        <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🎵 Music Separation as a Service</h3>
      <p align="center">
        <a href="https://github.com/adwait39/Music-separation-as-a-Service"><img src="https://img.shields.io/badge/View_Repo-181717?style=for-the-badge&logo=github" /></a>
      </p>
      <p>Kubernetes microservice that splits songs into vocals / drums / bass / other using Meta's <b>Demucs</b>. A REST frontend accepts MP3s and queues work in Redis; compute-heavy workers pull jobs, run separation, and cache stems in MinIO object storage. Deployed locally and on <b>GKE</b>.</p>
      <p align="center">
        <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white" />
        <img src="https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white" />
        <img src="https://img.shields.io/badge/MinIO-C72E49?style=flat&logo=minio&logoColor=white" />
        <img src="https://img.shields.io/badge/GKE-4285F4?style=flat&logo=googlecloud&logoColor=white" />
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">☁️ Automated Cloud Infra Deployment</h3>
      <p align="center">
        <a href="https://github.com/adwait39/automated-cloud-infra-deployment"><img src="https://img.shields.io/badge/View_Repo-181717?style=for-the-badge&logo=github" /></a>
      </p>
      <p>Infrastructure automation on <b>Google Cloud</b> using the Compute Engine Python API: programmatically provisions a VM, installs an app from git, opens firewall rules, snapshots the VM into a reusable image, benchmarks cold-start time across instances, and uses <b>IAM service accounts</b> so a VM can spawn further VMs.</p>
      <p align="center">
        <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=flat&logo=googlecloud&logoColor=white" />
        <img src="https://img.shields.io/badge/Compute_Engine-4285F4?style=flat&logo=googlecloud&logoColor=white" />
        <img src="https://img.shields.io/badge/IAM-EA4335?style=flat&logo=googlecloud&logoColor=white" />
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">📋 Next Play — Kanban Task Board</h3>
      <p align="center">
        <a href="https://github.com/adwait39/next-play"><img src="https://img.shields.io/badge/View_Repo-181717?style=for-the-badge&logo=github" /></a>
      </p>
      <p>Linear/Asana-style task board with drag-and-drop columns, priorities, due dates and overdue indicators. Anonymous guest auth and per-user data isolation via <b>Supabase Row Level Security</b>; fully responsive from 320px to ultrawide, with dark/light mode.</p>
      <p align="center">
        <img src="https://img.shields.io/badge/React_19-20232A?style=flat&logo=react&logoColor=61DAFB" />
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" />
        <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat&logo=supabase&logoColor=white" />
        <img src="https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white" />
        <img src="https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🏠 Elite Estate — Real Estate Platform</h3>
      <p align="center">
        <a href="https://github.com/adwait39/Elite-Estate"><img src="https://img.shields.io/badge/View_Repo-181717?style=for-the-badge&logo=github" /></a>
      </p>
      <p><b>MERN</b> stack marketplace for buying, selling and renting property. User auth, listing management, and a filtering engine by city, amenities and price range, with a rich property-details page.</p>
      <p align="center">
        <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white" />
        <img src="https://img.shields.io/badge/Express-000000?style=flat&logo=express&logoColor=white" />
        <img src="https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB" />
        <img src="https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white" />
        <img src="https://img.shields.io/badge/Redux-764ABC?style=flat&logo=redux&logoColor=white" />
        <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat&logo=tailwindcss&logoColor=white" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🚨 Agentic AI Incident Response Platform</h3>
      <p align="center">
        <img src="https://img.shields.io/badge/In_Progress-F59E0B?style=for-the-badge" />
      </p>
      <p>An on-call copilot: Alertmanager webhooks land in FastAPI, a <b>LangGraph</b> state machine gathers evidence from Prometheus, logs, Kubernetes and deployment history, ranks root-cause hypotheses, and proposes a remediation that only runs after <b>explicit human approval</b>. Full design doc written before the first line of code.</p>
      <p align="center">
        <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat&logo=langchain&logoColor=white" />
        <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white" />
        <img src="https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white" />
        <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white" />
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white" />
      </p>
    </td>
  </tr>
</table>

---

## 🛠️ Tech stack

**Languages**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" />
</p>

**Cloud & Infrastructure**

<p>
  <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" />
</p>

**Backend, Data & ML**

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
</p>

**Frontend**

<p>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
</p>

---

## 📊 GitHub stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=adwait39&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true" alt="GitHub stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=adwait39&layout=compact&theme=tokyonight&hide_border=true&langs_count=8&hide=jupyter%20notebook,html,css" alt="Top languages" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=adwait39&theme=tokyonight&hide_border=true" alt="GitHub streak" />
</p>

<p align="center">
  <img src="https://github.com/adwait39/adwait39/blob/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only" alt="contribution snake" />
  <img src="https://github.com/adwait39/adwait39/blob/output/github-contribution-grid-snake.svg#gh-light-mode-only" alt="contribution snake" />
</p>

---

<p align="center"><i>"Ship the boring, simple option first — then earn the complexity."</i></p>
