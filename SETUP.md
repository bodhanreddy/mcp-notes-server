# SETUP.md

## Connecting Your Notes MCP Server to Claude and Cursor

This guide shows you how to connect your Notes MCP server to both Claude Desktop and Cursor IDE, so you can manage your notes directly through AI conversations.

## Prerequisites

Before starting, make sure you have:

- **Python 3.8+** installed
- **Node.js** and **npm** installed (for remote connections)
- Your Notes MCP server configured with the correct `BASE_PATH`

## Method 1: Local Connection (Recommended for Development)

### For Claude Desktop

**Option A: Using uv (Recommended)**

If you have `uv` installed, create a managed project:

```bash
uv init mcp-server-demo
cd mcp-server-demo
```

Add MCP to your project dependencies:
```bash
uv add "mcp[cli]"
```

Install directly in Claude Desktop:
```bash
uv run mcp install main.py
```

Test with MCP Inspector:
```bash
uv run mcp dev main.py
```

**Option B: Manual Configuration**

1. **Locate Your Config File**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`  
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. **Add Your MCP Server Configuration**

   Add this to your `claude_desktop_config.json`:

   ```json
   {
     "mcpServers": {
       "notes-server": {
         "command": "python",
         "args": ["/full/path/to/your/main.py"],
         "env": {}
       }
     }
   }
   ```

   **Important**: Replace `/full/path/to/your/main.py` with the actual absolute path to your Notes server file.

3. **Restart and Test**
   - Close and restart Claude Desktop completely
   - Start a new conversation
   - Test with: "Create a note called 'test' with the content 'Hello World'"

### For Cursor IDE

**Step 1: Open MCP Settings**

1. Open Cursor
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Search for "Cursor Settings"
4. Look for **MCP** in the sidebar

**Step 2: Add Your Server**

Create a new MCP server configuration:

```json
{
  "mcpServers": {
    "notes-server": {
      "command": "python",
      "args": ["/full/path/to/your/main.py"]
    }
  }
}
```

**Step 3: Restart and Test**

1. Restart Cursor
2. Open the AI chat panel
3. Test with: "List all my notes"

## Method 2: Remote Connection (For Production/Sharing)

If you want to run your Notes server remotely and access it from anywhere, follow these steps:

### Modify Your Server for Remote Access

First, update your `main.py` to support remote connections:

```python
# Add this to the end of your main.py file
if __name__ == "__main__":
    import asyncio
    import os
    
    port = int(os.environ.get("PORT", 8000))
    asyncio.run(
        mcp.run_sse_async(
            host="0.0.0.0",  # Allow external connections
            port=port,
            log_level="debug"
        )
    )
```

### Deploy Your Server

Deploy your server to a cloud platform like:
- **Heroku**: Easy deployment with git
- **Railway**: Simple Python app hosting  
- **DigitalOcean**: VPS with more control
- **AWS/GCP**: Enterprise-grade hosting

### Configure Claude Desktop for Remote Access

```json
{
  "mcpServers": {
    "notes-server": {
      "command": "npx",
      "args": [
        "mcp-remote@latest",
        "https://your-server-url.com"
      ]
    }
  }
}
```

### Configure Cursor for Remote Access

```json
{
  "mcpServers": {
    "notes-server": {
      "command": "npx", 
      "args": [
        "mcp-remote@latest",
        "https://your-server-url.com"
      ]
    }
  }
}
```

## Method 3: Claude Web (Claude.ai) - Remote Only

For Claude's web interface, you can only use remote MCP servers:

**Step 1: Deploy Your Server Remotely**

Your server must be publicly accessible via HTTPS.

**Step 2: Connect in Claude Web**

1. Go to [Claude.ai](https://claude.ai) and log in
2. Click your profile in the bottom-left
3. Select **Settings** → **Integrations** 
4. Click **Add Integration**
5. Enter your server name and URL
6. Accept the security notice and click **Add**

**Step 3: Enable and Test**

1. Start a new conversation
2. Click the search/tools icon
3. Find your Notes server and click **Connect**
4. Enable the actions you want Claude to access
5. Test with: "Show me all my notes"

## Troubleshooting

### Common Issues

**"Server not found" or connection errors:**
- Check that your file paths are absolute, not relative
- Ensure Python is in your system PATH
- Verify your `BASE_PATH` directory exists and is writable

**"Configuration invalid" in Claude Desktop:**
- Validate your JSON syntax (use a JSON validator)
- Ensure all file paths use forward slashes, even on Windows
- Restart Claude Desktop completely after config changes

**MCP server not appearing in Cursor:**
- Check that Node.js and `npx` are installed
- Restart Cursor after configuration changes
- Look in Cursor's developer console for error messages

### Testing Your Connection

Once connected, try these commands to verify everything works:

- **"Create a note called 'shopping' with 'milk, eggs, bread'"**
- **"Read my shopping note"**  
- **"List all my notes"**
- **"Add 'butter' to my shopping note"**

### Security Considerations

- **Local servers**: Your notes stay on your machine
- **Remote servers**: Ensure HTTPS and consider authentication
- **Access control**: MCP servers have full file system access within your `BASE_PATH`

## What You Can Do Now

With your Notes MCP server connected, you can:

- **Create and manage notes** through natural conversation
- **Organize different file types** (txt, md, py, html, css, js)
- **Build upon your notes** by appending content over time
- **Integration with workflows** - let AI help manage your documentation, code snippets, and ideas

Your AI assistant can now seamlessly read, write, and organize your notes while you focus on the important work!
