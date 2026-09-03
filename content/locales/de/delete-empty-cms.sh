#!/bin/sh
# Delete leftover empty CMS collections. Does not publish.
# Requires WEBFLOW_SITE_API_TOKEN with cms:write. Do not commit a token.
set -eu

SITE_ID=6a7b43a328ec101a40bb1d20
API=https://api.webflow.com/v2

if [ -z "${WEBFLOW_SITE_API_TOKEN:-}" ]; then
  echo "WEBFLOW_SITE_API_TOKEN is not set. Cannot DELETE collections." >&2
  exit 2
fi

auth() {
  curl -sS -D - -o /tmp/wf-body \
    -H "Authorization: Bearer ${WEBFLOW_SITE_API_TOKEN}" \
    -H "accept: application/json" \
    "$@"
}

echo "Listing collections before delete..."
auth "${API}/sites/${SITE_ID}/collections" | head -n 20

for id in 6a876663b22843d8b60c22c8 6a87666d57cf52c62b38e6cf; do
  echo "DELETE ${API}/collections/${id}"
  auth -X DELETE "${API}/collections/${id}" | head -n 20
  echo
done

echo "Listing collections after delete..."
auth "${API}/sites/${SITE_ID}/collections"
