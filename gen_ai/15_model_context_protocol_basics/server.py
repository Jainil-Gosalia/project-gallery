# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("config://version")
def static_greeting(): 
    return "Hello"

@mcp.resource("users://{name}")
def dynamic_greeting(name: str):
    return f"Hello {name}"

@mcp.prompt()
def custom_prompt(name: str) -> str:
    """Generate a prompt asking for a summary."""
    return f"Hello from prompt, {name}"

if __name__ == "__main__":
    mcp.run()