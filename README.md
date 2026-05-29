# RGI user guide

Stable version: https://rgidata.org/user_guide

Development version: https://glims-rgi.github.io/rgi_user_guide

## Staging toggle

The development site can be switched on/off via the repository variable `STAGING_ENABLED`
(GitHub → Settings → Secrets and variables → Actions → Variables tab):

- `STAGING_ENABLED = true` — full Jupyter Book build is deployed on every push to `main`
- variable absent or any other value — a placeholder page is deployed instead

## License

[![Creative Commons License](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg)](https://creativecommons.org/licenses/by/4.0)

This document is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
