from mcp.server.fastmcp import FastMCP
import os
from typing import Optional

mcp = FastMCP("Notes")

BASE_PATH = "Your-Base-Path"
ALLOWED_NOTE_EXTENSIONS = (".txt", ".py", ".md", ".html", ".css", ".js") #update extensions according to your choice


#Tool-1
@mcp.tool()
def create_note(filename: str, content: str, mode: Optional[str] = "a", format: str = "txt", dir: str = "Personal-notes-server") -> str:
    """
    Create or append content to a note file.
    """
    try:
        # Create directory path
        dir_path = os.path.join(BASE_PATH, dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        # CRITICAL FIX: Create the actual file path
        file_path = os.path.join(dir_path, f"{filename}.{format}")
        
        # Write content to file
        with open(file_path, mode, encoding="utf-8") as f:
            f.write(content)
        
        if mode == "a":
            return f"Content appended to file {filename}.{format}"
        else:
            return f"File {filename}.{format} created and content written successfully"
    
    except Exception as e:
        return f"Error: {str(e)}"


#Tool-2
@mcp.tool()
def delete_chunk(filename: str, start: int, end: int, format: str = "txt", dir: str = "Personal-notes-server") -> str:
    """
    Delete content from start to end character positions in a file.

    Args:
        filename (str): File name without extension.
        start (int): Start character position.
        end (int): End character position.
        format (str): File extension.

    Returns:
        str: Status message indicating success or failure.
    """
    try:
        # Input validation
        if start < 0 or end < 0:
            return "Error: Start and end positions must be non-negative"
        
        if start >= end:
            return "Error: Start position must be less than end position"
        
        base_path = os.path.join(BASE_PATH, dir)
        file_path = os.path.join(base_path, f"{filename}.{format}")
        
        if not os.path.exists(file_path):
            return f"File {filename}.{format} does not exist"
        
        # Read current content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Validate positions are within content bounds
        if start >= len(content):
            return f"Error: Start position {start} is beyond file content (length: {len(content)})"
        
        if end > len(content):
            return f"Error: End position {end} is beyond file content (length: {len(content)})"
        
        # Create new content with chunk deleted
        new_content = content[:start] + content[end:]
        
        # Write back to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        deleted_chars = end - start
        return f"Deleted {deleted_chars} characters from position {start} to {end} in file {filename}.{format}"
    
    except Exception as e:
        return f"Error: {str(e)}"


#Tool-3
@mcp.tool()
def read_note(filename: str, format: str = "txt", dir: str = "Personal-notes-server") -> str:
    """
    Read and return file content.

    Args:
        filename (str): File name without extension.
        format (str): File extension. Defaults to 'txt'.

    Returns:
        str: File content if successful, error message if failed.
    """
    try:
        file_path = os.path.join(BASE_PATH, dir, f"{filename}.{format}")
        
        if not os.path.exists(file_path):
            return f"File {filename}.{format} does not exist"
        
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    
    except Exception as e:
        return f"Error reading file: {str(e)}"


#Tool-4
@mcp.tool()
def list_notes(dir: str = "Personal-notes-server") -> list[str] | str:
    """
    List all note files in the base directory.

    Returns:
        list[str] | str: List of note filenames or error message.
    """
    try:
        base_path = os.path.join(BASE_PATH, dir)
        
        if not os.path.exists(base_path):
            return "Directory does not exist"
        
        notes = [f for f in os.listdir(base_path) if f.endswith(ALLOWED_NOTE_EXTENSIONS)]
        
        if notes:
            return sorted(notes)  # Return sorted list for consistency
        else:
            return "No notes found in directory"
    
    except Exception as e:
        return f"Error accessing directory: {str(e)}"


if __name__ == "__main__":
    mcp.run()
