PANEL_URL="https://your-panel.com/nodes/register"
API_TOKEN="your_admin_jwt_token_here"

curl -X POST "$PANEL_URL" \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "'"$(hostname)"'",
    "ip": "'"$(hostname -I | awk "{print \$1}")"'",
    "api_key": "your_wings_generated_api_key_here"
  }'
