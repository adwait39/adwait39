# Fix `drift-detection-adwait` — remove committed `.env` and `.venv`

Why this matters to a recruiter:

- `.env` is committed → anyone can read whatever keys it contains (Gmail app password, Gemini key, GCP creds…). A hiring manager who spots this will assume you'd do it at work too.
- `.venv` is committed → 51 MB of third-party Python, C, Fortran and Cython shows up in the language bar, so the repo looks like a vendored library dump instead of *your* code. It also skews the "Top languages" card on your profile.

## 1. Rotate every secret in `.env` first

Even after the file is deleted, the old commits stay in GitHub's history until step 3 is done and GitHub's caches expire. Treat every value in it as leaked: regenerate the Gmail app password, Gemini API key, any GCP service-account key, DB password, etc.

## 2. Remove the files from the *current* commit

```powershell
git clone https://github.com/adwait39/drift-detection-adwait.git
cd drift-detection-adwait

git rm -r --cached .env .venv __pycache__
Add-Content .gitignore "`n.env`n.venv/`n__pycache__/`n*.pyc"
Copy-Item .env .env.example        # then open .env.example and blank out every value
git add .gitignore .env.example
git commit -m "Remove committed secrets and virtualenv; add .env.example"
git push
```

## 3. Purge them from history (so the language bar and secret scanning clear up)

```powershell
pip install git-filter-repo
git filter-repo --invert-paths --path .env --path .venv --path __pycache__ --force
git remote add origin https://github.com/adwait39/drift-detection-adwait.git
git push --force --all
git push --force --tags
```

`git filter-repo` removes the `origin` remote on purpose; that's why it's re-added. After the force-push, GitHub recomputes the language stats within a few minutes.

## 4. Verify

- https://github.com/adwait39/drift-detection-adwait → language bar should show mostly Python + Jupyter, well under 1 MB.
- Repo → Settings → Code security → make sure **Secret scanning** and **Push protection** are on so this can't happen again.
