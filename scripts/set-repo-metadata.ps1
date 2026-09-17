# Sets a description + topics on each public repo so the "Repositories" tab reads well
# without opening any repo. Also adds a website URL where one exists.
#
# Usage (Windows PowerShell):
#   $env:GITHUB_TOKEN = "ghp_..."      # classic PAT with `repo` scope, or fine-grained with "Administration: write"
#   .\set-repo-metadata.ps1
#
# Create a token at https://github.com/settings/tokens. Delete it afterwards.

$ErrorActionPreference = "Stop"
if (-not $env:GITHUB_TOKEN) { throw "Set `$env:GITHUB_TOKEN first." }

$owner = "adwait39"
$headers = @{
    Authorization          = "Bearer $env:GITHUB_TOKEN"
    Accept                 = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
    "User-Agent"           = "adwait39-profile-script"
}

$repos = @(
    @{ name = "drift-detection-adwait"
       description = "MLOps data-drift detection pipeline: semantic / lexical / topic / OOD drift with FastAPI, Pub/Sub, MinIO, sentence-transformers and Postgres"
       topics = @("mlops", "data-drift", "fastapi", "streamlit", "minio", "google-pubsub", "sentence-transformers", "postgresql", "docker") },

    @{ name = "Music-separation-as-a-Service"
       description = "Kubernetes microservice that splits songs into stems with Demucs — REST API, Redis job queue, MinIO object storage, deployed on GKE"
       topics = @("kubernetes", "gke", "microservices", "redis", "minio", "demucs", "rest-api", "python", "docker") },

    @{ name = "automated-cloud-infra-deployment"
       description = "Programmatic GCP infrastructure: provision VMs, snapshot to images, benchmark cold-start, and chain VM creation via IAM service accounts (Compute Engine Python API)"
       topics = @("google-cloud", "gcp", "compute-engine", "infrastructure-automation", "iam", "python") },

    @{ name = "next-play"
       description = "Kanban task board with drag-and-drop, priorities and due dates — React 19 + TypeScript + Supabase (RLS) + Vite, deployed on Vercel"
       topics = @("react", "typescript", "supabase", "kanban", "vite", "dnd-kit", "vercel") },

    @{ name = "Elite-Estate"
       description = "MERN real-estate marketplace: auth, listing management and multi-criteria search (city, amenities, price) with Redux and Tailwind"
       topics = @("mern", "react", "nodejs", "express", "mongodb", "redux", "tailwindcss", "real-estate") },

    @{ name = "evenza"
       description = "Angular event-management front end"
       topics = @("angular", "typescript", "frontend") },

    @{ name = "Ready-to-Use-FrontEnd-pages"
       description = "Collection of reusable HTML/CSS landing and UI page templates"
       topics = @("html", "css", "templates", "frontend") },

    @{ name = "angular-project-1-intern-"
       description = "Angular application built during my internship"
       topics = @("angular", "typescript", "internship") },

    @{ name = "Machine-Learning-clg-"
       description = "Machine learning coursework notebooks (regression, classification, clustering)"
       topics = @("machine-learning", "jupyter-notebook", "coursework") },

    @{ name = "SPPU-BE-IT-Information-Storage-and-Retrieval"
       description = "Information Storage & Retrieval lab notebooks (indexing, ranking, text retrieval) — SPPU BE IT"
       topics = @("information-retrieval", "jupyter-notebook", "coursework") },

    @{ name = "33202_WAD"
       description = "Web Application Development lab assignments"
       topics = @("html", "coursework") }
)

foreach ($r in $repos) {
    $url = "https://api.github.com/repos/$owner/$($r.name)"
    Write-Host "Updating $($r.name) ..." -NoNewline

    $body = @{ description = $r.description } | ConvertTo-Json -Compress
    Invoke-RestMethod -Method Patch -Uri $url -Headers $headers -Body $body -ContentType "application/json" | Out-Null

    $topicsBody = @{ names = $r.topics } | ConvertTo-Json -Compress
    Invoke-RestMethod -Method Put -Uri "$url/topics" -Headers $headers -Body $topicsBody -ContentType "application/json" | Out-Null

    Write-Host " ok"
}

Write-Host ""
Write-Host "Done. Consider also:"
Write-Host "  - Deleting the empty 'TerraLens' repo (or push code to it):  https://github.com/adwait39/TerraLens/settings"
Write-Host "  - Pinning the 4-6 best repos on your profile:               https://github.com/adwait39  ->  'Customize your pins'"
