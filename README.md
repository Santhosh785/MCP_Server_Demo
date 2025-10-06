🧠 MCP Server Demo

This repository contains a Minimal MCP (Model Context Protocol) Server example — a next-generation protocol designed for secure communication between LLMs (like GPT) and local or remote tools.
With this demo, you can start your own MCP server locally and explore how upcoming AI models will connect with external systems directly and safely.

🚀 Features

✅ Lightweight MCP server built with Python + FastAPI

🖥️ Returns your system specifications (CPU, RAM, OS info)

🔌 Uses Server-Sent Events (SSE) for live communication

🧩 Easy to extend with your own custom MCP tools

📦 Installation

# 1️⃣ Clone the repo
git clone https://github.com/Santhosh785/MCP_Server_Demo.git
cd MCP_Server_Demo

# 2️⃣ Create a virtual environment
python -m venv .venv
.venv\Scripts\activate  # (Windows)

# 3️⃣ Install dependencies
pip install fastapi uvicorn psutil

# 4️⃣ Run the server
python server.py

⚙️ How It Works

Once you run the server, it will:

Start an MCP-compatible endpoint on your localhost.

Gather system stats using psutil.

Return details such as:

CPU cores

RAM usage

Operating system

Python version

🌐 Example Output
{
  "system": "Windows 11",
  "cpu_cores": 8,
  "ram_gb": 16,
  "python_version": "3.11.5"
}
Developer Message

“This is my first MCP Server — built to help developers understand how LLMs will soon connect to real-world systems.
The MCP protocol will revolutionize how AI tools interact with your local or cloud environments.”

— Santhosh, Developer
