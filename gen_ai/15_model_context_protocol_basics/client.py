import asyncio
from fastmcp import Client

async def main():
    async with Client("server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}\n")

        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"Result: {result[0].text}\n")

        static_resources = await client.list_resources()
        print(f"Available static resources: {static_resources}\n")

        static_resource_response = await client.read_resource("config://version")
        print(f"Result: {static_resource_response[0].text}\n")

        dynamic_resources = await client.list_resource_templates()
        print(f"Available dynamic resources: {dynamic_resources}\n")

        dynamic_resource_response = await client.read_resource("users://jainil")
        print(f"Result: {dynamic_resource_response[0].text}\n")

        prompts = await client.list_prompts()
        print(f"Available Prompts: {prompts}\n")

        prompt = await client.get_prompt("custom_prompt", 
                                         arguments={"name": "Jainil"})
        print(f"Result: {prompt}")


if __name__ == "__main__":
    asyncio.run(main())
