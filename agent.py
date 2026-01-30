"""Data Analyst Agent for BigQuery MCP Server"""
""" Rekha Suryae - 29th Jan 2026 """

from google.adk.agents import LlmAgent
import google.auth
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams
import google.auth.transport.requests

# Define the official BigQuery MCP URL
BIGQUERY_MCP_URL = "https://bigquery.googleapis.com/mcp"

# Automatically retrieve credentials and project ID using ADC
credentials, project_id = google.auth.default(scopes=["https://www.googleapis.com/auth/bigquery"])
credentials.refresh(google.auth.transport.requests.Request())
oauth_token = credentials.token

PROJECT_ID = project_id

# Define the headers for the MCP connection
bigquery_mcp_headers = {
    "Authorization": f"Bearer {oauth_token}",
    "x-goog-user-project": project_id, # This is used for billing
}

# Initialize the MCP Toolset with the connection parameters
bigquery_toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=BIGQUERY_MCP_URL,
        headers=bigquery_mcp_headers,
    )
)


root_agent = LlmAgent(
    name="data_analyst_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to help users analyze data using BigQuery."
    ),
    instruction="Help the user answer questions by accessing data in the BigQuery tables.",
    tools=[bigquery_toolset]
)