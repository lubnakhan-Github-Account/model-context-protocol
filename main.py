from mcp.server.fastmcp import FastMCP

mcp= FastMCP(name="hello=mcp", stateless_http=True)

@mcp.tool(name="search_online")
def search_online(query: str)->str:
  # TODO: impliment search logic
 return f"Result for {query}..."
  
# Transport -> getstarlette instance 
mcp_app= mcp.streamable_http_app()


