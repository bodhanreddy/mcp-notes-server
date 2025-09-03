from mcp.server.fastmcp import FastMCP
import os
from typing import Optional

mcp = FastMCP("Notes")

BASE_PATH = "Your/Path/Here"

if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)


#Tool-1
@mcp.tool()
def create_note(filename: str, content: str, mode: Optional[str] = "a", format: str = "txt") -> str:
    """
        Create or append content to a note file.

        Args:
            filename (str): File name without extension.
            content (str): Text content to write.
            mode (Optional[str]): Write mode, 'a' for append, 'w' for overwrite. Defaults to 'a'.
            format (str): File extension. Defaults to 'txt'.

        Returns:
            str: Status message indicating success or failure.
        """
    file_path = os.path.join(BASE_PATH, f"{filename}.{format}")
    if os.path.exists(file_path):
        with open(file_path, mode) as f:
            f.write(content)
            return f"File {filename} already exists and the content is written into it"
    else:
        with open(file_path, "w") as f:
            f.write(content)
            return f"File {filename} created and content written successfully"


#Tool-2
@mcp.tool()
def delete_chunk(filename: str, start: int, end: int, format: str) -> str:
    """
        Delete content from start to end positions in a file.

        Args:
            filename (str): Full file path.
            start (int): Start byte position.
            end (int): End byte position.
            format (str): File extension. Defaults to 'txt'.

        Returns:
            str: Status message indicating success or failure.
        """
    file_path = os.path.join(BASE_PATH, f"{filename}.{format}")
    if os.path.exists(file_path):
        with open(file_path, "r+b") as f:
            f.seek(end)
            rest = f.read()
            f.seek(start)
            f.write(rest)
            f.truncate()
            return f"Deleted content from {start} to {end} in file {filename}"
    else:
        return f"File {filename} does not exist"


#tool-3
@mcp.tool()
def read_note(filename: str, format: str = "txt") -> str:
    """
        Read and return file content.

        Args:
            filename (str): File name without extension.
            format (str): File extension. Defaults to 'txt'.

        Returns:
            Optional[str]: File content if successful, error message if failed.
        """
    file_path = os.path.join(BASE_PATH, f"{filename}.{format}")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return f.read()
    else:
        return f"File {filename} does not exist"


#tool-4
@mcp.tool()
def list_notes() -> list[str] | str:
    """
        List all note files in the base directory.

        Returns:
            list[str] | str: List of note filenames or error message.
        """
    if os.path.exists(BASE_PATH):
        notes = [f for f in os.listdir(BASE_PATH) if f.endswith((".txt",".py",".md",".html",".css",".js"))]
        if notes:
            return notes
        else:
            return "no notes exist"
    else:
        return "no data"
    

if __name__ == "__main__":
    mcp.run()