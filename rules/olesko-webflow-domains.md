# oleskostudio.com — Webflow custom domain setup

Read this before publishing, changing DNS, or touching production domains. The site is already connected. Do not re-add domains. Do not use Quick Connect.

Site: **OLESKO Website — Development** (`6a7b43a328ec101a40bb1d20`)  
Workspace: Agency Workspace (`sebastians-workspace-bddf1a`)  
DNS: Cloudflare (nameservers stay on Cloudflare)  
Mail: Google (MX + SPF, do not touch)

## End state

| Item | Value |
|------|--------|
| Default domain | `https://oleskostudio.com` |
| www | `https://www.oleskostudio.com` (redirects to apex) |
| Staging | `https://olesko-website----development.webflow.io` |
| DNS host | Cloudflare |
| Proxy | Off on Webflow A / CNAME / TXT |
| Mail | Google MX + SPF unchanged |
| Site ID | `6a7b43a328ec101a40bb1d20` |
| Short name | `olesko-website----development` |

Domain IDs for `publish_site`:

- `oleskostudio.com` → `6a874109e067f5d3b357ad46`
- `www.oleskostudio.com` → `6a874109e067f5d3b357ad4d`

## DNS (current, post Cloudflare migration)

Proxy **off** (grey cloud). Nameservers stay on Cloudflare (`trevor.ns.cloudflare.com` / `alla.ns.cloudflare.com`).

| Type | Name | Value |
|------|------|--------|
| A | `@` | `198.202.211.1` |
| CNAME | `www` | `cdn.webflow.com` |
| TXT | `_webflow` | `one-time-verification=1f42e90e-1d0f-4ffb-8b10-e92dc5088fb4` |
| TXT | `@` | Google SPF (`v=spf1 include:_spf.google.com ~all`) — do not overwrite |

Never use legacy Webflow records: `75.2.*` / `99.83.*` or `proxy-ssl.webflow.com`.

## How domains were added (do not repeat unless they disappear)

Webflow Data API can list/publish the site but **cannot add custom domains**. Dashboard only:

`https://webflow.com/dashboard/sites/olesko-website----development/publishing`

1. Site plan must be **Basic or higher**. Starter only gets `.webflow.io`. If Publishing dumps to Site Plans, upgrade first.
2. Add a custom domain → **Manually add domain** (never Quick Connect; that tries to take over DNS).
3. Enter `oleskostudio.com`. Webflow auto-adds `www.oleskostudio.com`.
4. Webflow then issues `_webflow` TXT. Same value for apex and www. Add it on Cloudflare (DNS only, proxy off). Then **Verify domain**.
5. Webflow defaults to **www**. Click **Make default** on the `oleskostudio.com` row. Confirm apex shows **Default** and www shows **Make default**. A first-click race can leave www as default — check the rows.
6. First production publish puts the site on the custom domain and clears SSL “Update needed”. Default-domain change also needs a publish.

Cursor’s in-app browser is often not logged into Webflow and can drop the session. Dashboard login is required for the add-domain step.

## Publish

Do not publish unless Sebastian asks. Draft pages (Styleguide, Example Components, Standard Page) stay unpublished.

`publish_site` needs custom domain **IDs**, not hostnames:

```json
{
  "site_id": "6a7b43a328ec101a40bb1d20",
  "customDomains": [
    "6a874109e067f5d3b357ad46",
    "6a874109e067f5d3b357ad4d"
  ],
  "publishToWebflowSubdomain": true
}
```

First production publish: **2026-08-20T18:04:34.741Z**. Live check: https://oleskostudio.com served the homepage.

## Do not

- Do not add custom domains through the Webflow MCP. `data_sites_tool` = `list_sites` / `get_site` / `publish_site` only.
- Do not use Quick Connect when Cloudflare is DNS.
- Do not move nameservers off Cloudflare.
- Do not overwrite MX or Google SPF.
- Do not proxy (orange cloud) the Webflow A / CNAME / `_webflow` TXT records.
- Do not use legacy Webflow IPs or `proxy-ssl.webflow.com`.

This file is also stored as a Cursor always-on rule (`.cursor/rules/olesko-webflow-domains.mdc`).
