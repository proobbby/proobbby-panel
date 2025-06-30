# Replace with your panel backend URL and admin API token
PANEL_URL="https://your-panel.com/api/nodes/register"
API_TOKEN="your_admin_jwt_token_here"

curl -X POST "$PANEL_URL" \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "MyNode01",
    "ip": "'"$(hostname -I | awk "{print \$1}")"'",
    "api_key": "generated_wings_api_key"
  }'
