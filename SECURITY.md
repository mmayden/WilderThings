# Security Policy

## Content Security

WilderThings contains medical, wilderness, and emergency survival information. **Accuracy is a life-safety matter.**

### Reporting Inaccurate or Dangerous Content

If you find information that is factually wrong, medically unsafe, or could lead to harm:

1. Open a GitHub Issue tagged `content-safety`
2. Include: the guide name, the specific claim, why it is wrong, and a credible source contradicting it
3. Critical safety corrections will be prioritized and addressed before new content

### Content Standards

- Medical information cites established clinical references (military field manuals, UpToDate, peer-reviewed sources)
- Plant and mushroom identification guides include look-alike warnings and regional caveats
- All guides carry disclaimers that content does not replace professional training
- Guides covering regulated activities (hunting, trapping) note legal requirements

---

## Infrastructure Security

### Dependency Management

- Dependencies are pinned to exact versions in `requirements.txt`
- [Dependabot](.github/dependabot.yml) opens weekly PRs for dependency updates
- All dependency upgrades go through CI before merge: `mkdocs build --strict` must pass

### CI/CD Pipeline

The deployment pipeline follows least-privilege principles:

| Job | Permissions |
|-----|-------------|
| build | `contents: read` only |
| deploy | `pages: write`, `id-token: write` (OIDC — no long-lived tokens) |

- No secrets are stored in the repository
- GitHub Actions OIDC is used for deployment (no personal access tokens)
- `mkdocs build --strict` runs on every push and PR; warnings are treated as errors

### Branch Protection (recommended settings)

Configure these in Settings → Branches → main:

- Require pull request reviews before merging
- Require status checks to pass (lint and build-check workflows)
- Require branches to be up to date before merging
- Do not allow force pushes
- Do not allow deletions

### Reporting a Security Vulnerability

This project is a static content site with no server-side code, user accounts, or data collection. The attack surface is limited to:

- Dependency vulnerabilities in the build pipeline
- Supply chain attacks via GitHub Actions
- Inaccurate or harmful content (see Content Security above)

To report an infrastructure vulnerability, open a GitHub Issue tagged `security`. For sensitive issues, contact the maintainer directly via GitHub.

---

## What Is NOT in Scope

- No backend, API, or server infrastructure
- No user data or authentication
- No cookies, tracking, or analytics
- The deployed site is a static HTML/CSS/JS bundle served via GitHub Pages CDN
