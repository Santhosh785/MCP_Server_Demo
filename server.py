from fastmcp import FastMCP, Context
import openai
import os
import platform
import psutil
import subprocess

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Create MCP server
mcp = FastMCP(name="Python Executor GPT")

# System info tool
@mcp.tool()
async def system_info(ctx: Context):
    info = {
        "OS": f"{platform.system()} {platform.release()}",
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2)
    }
    
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        info["GPU"] = ", ".join([gpu.name for gpu in gpus]) if gpus else "No GPU detected"
    except:
        info["GPU"] = "GPUtil not installed"
    
    return "\n".join(f"{k}: {v}" for k, v in info.items())

# Execute Python code tool
@mcp.tool()
async def run_python(ctx: Context, code: str):
    filename = "temp_code.py"
    with open(filename, "w") as f:
        f.write(code)
    
    try:
        result = subprocess.run(["python", filename], capture_output=True, text=True, timeout=5)
        output = result.stdout if result.stdout else result.stderr
    except Exception as e:
        output = f"Error executing code: {e}"
    
    # Remove temporary file
    os.remove(filename)
    return output

# GPT tool
@mcp.tool()
async def ask_gpt(ctx: Context, question: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Python-savvy AI assistant. You can provide system info and run Python code safely."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error contacting OpenAI: {e}"

# Start MCP server
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=3001)
