# RGI User Guide — CI & Hosting

## What this repo is

This repo contains the RGI user guide as a **Jupyter Book v1** project (do not upgrade to v2), with two version folders:

- `v7.0/` — current stable release, published at <https://rgidata.org/user_guide>
- `v7.1/` — work in progress, available on staging only

Both repos (`rgi_user_guide` and `rgi-website`) live in the **GLIMS-RGI** GitHub organisation.

---

## Hosting

| Environment | URL | How it is deployed |
| --- | --- | --- |
| Staging | <https://glims-rgi.github.io/rgi_user_guide/> | Automatically on every push to `main` (CI) |
| Production | <https://rgidata.org/user_guide> | Manually triggered CI → opens PR on `rgi-website` |

`rgi-website` is a Material/MkDocs site at <https://github.com/GLIMS-RGI/rgi-website>.
Its CI runs `mkdocs gh-deploy --force` on every push to `main`.
MkDocs copies non-Markdown files verbatim, so the Jupyter Book HTML placed in
`docs/user_guide/` is served as-is at `rgidata.org/user_guide`.

---

## Staging toggle

The staging build is controlled by the repository variable **`STAGING_ENABLED`**
(GitHub → Settings → Secrets and variables → Actions → Variables tab):

| Value | Behaviour |
| --- | --- |
| `true` | Full Jupyter Book build deployed on every push to `main` |
| absent / anything else | Placeholder HTML page deployed instead (no build) |

This lets staging stay dark between active development cycles without changing any code.

---

## URL structure (Option A — latest at root)

| Path | Content |
| --- | --- |
| `/user_guide/` | Latest published version (currently v7.0) |
| `/user_guide/v7.0/` | Stable archive of v7.0 (permanent URL) |
| `/user_guide/v7.1/` | Added when v7.1 is published |

**Same structure on staging and production.**

v7.0 is deployed to both the root and `/v7.0/` from a single build (HTML uses relative
links throughout, so the same output is path-portable). See `build.sh` → `merge_outputs()`.

### Future migration to v7.1

When v7.1 is ready to become the default:

1. v7.1 takes the root slot; v7.0 stays only at `/v7.0/`
2. Update `merge_outputs()` in `build.sh` accordingly
3. Update the `workflow_dispatch` title/commit message in `deploy-production.yml`
4. The `--merge` step already skips v7.1 if it has not been built, so production
   can continue to be v7.0-only until that switch is made

---

## Files created / modified

| File | What it does |
| --- | --- |
| `build.sh` | Builds one or both versions and merges HTML into `_html_merged/`. `--merge` is safe to run after a v7.0-only build (v7.1 copy is skipped if not built). |
| `v7.0/docs/_static/custom.css` | RGI-branded staging banner CSS (navy→red gradient, gold link pill). Copied to `v7.1/` too. |
| `.github/workflows/staging.yml` | Builds both versions, injects staging banner, deploys to `gh-pages`. |
| `.github/workflows/deploy-production.yml` | Manual trigger: builds v7.0, opens PR on `rgi-website`. |
| `push.sh` | **Retired** — staging is now handled by CI. |

---

## Cross-repo secret

The production workflow opens PRs on `rgi-website` using a fine-grained PAT stored as:

> **Secret name**: `RGI_WEBSITE_TOKEN`
> **Location**: `rgi_user_guide` repo → Settings → Secrets and variables → Actions
> **Scoped to**: `rgi-website` repo only (Contents + Pull requests: read/write)
> **Resource owner**: GLIMS-RGI organisation
> **Expiry**: **2027-05-25** (~366 days from creation on 2026-05-24)

Renew before that date at:
GitHub → profile picture → Settings → Developer settings → Personal access tokens → Fine-grained tokens

---

## Staging banner injection

The CI patches `_config.yml` (both versions) at build time with `html.announcement`
before running Jupyter Book. The patch is a regex insertion under the `html:` key —
the file on disk is never permanently modified (clean checkout each run).
The production workflow does **not** inject the banner.

Banner CSS is in `v7.0/docs/_static/custom.css` (identical copy in `v7.1/`).
Colors: navy `#2D2D8C` → red `#CC2E22` gradient; gold `#F5A623` link pill.

---

## Note for rgi-website

The production deploy workflow (`deploy-production.yml`) opens a PR that replaces
`docs/user_guide/` in `rgi-website` with the freshly built Jupyter Book HTML.
The structure placed there is:

```text
docs/user_guide/          ← v7.0 HTML (served at rgidata.org/user_guide/)
docs/user_guide/v7.0/     ← v7.0 HTML copy (served at rgidata.org/user_guide/v7.0/)
```

No changes to `rgi-website`'s `mkdocs.yml` or CI are needed — MkDocs copies
the HTML files verbatim. The user guide has its own navigation (Jupyter Book sidebar)
and does not appear in the MkDocs nav menu, which is intentional.

When the PR is merged, `rgi-website`'s CI fires automatically and deploys everything.
