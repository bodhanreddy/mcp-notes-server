MCP Notes management server

A simple and efficient Model Context Protocol (MCP) server for managing note files with basic CRUD operations.

What It Does

This MCP server helps you manage your notes through a clean API. Think of it as your personal note-taking assistant that can:

- Create notes - Write new notes or add to existing ones
- Read notes - Retrieve content from any note file  
- Delete chunks - Remove specific portions of text from your notes
- List all notes - See what notes you have stored

Features

- Multiple formats supported: txt, py, md, html, css, js files
- Flexible writing modes: Append to existing notes or overwrite them
- Precise editing: Delete specific byte ranges from files
- Simple file organization: All notes stored in one configurable directory

Quick Start

Setup

1. Configure your notes directory:
   ```python
   BASE_PATH = "Your/Path/Here"  # Change this to your desired notes folder
   ```

2. Install dependencies:
   ```bash
   pip install fastmcp
   ```

3. Run the server:
   ```bash
   python main.py
   ```

Available Tools

`create_note(filename, content, mode="a", format="txt")`
Creates a new note or adds content to an existing one.

Parameters:
- `filename`: Name of your note (without file extension)
- `content`: The text you want to write
- `mode`: `"a"` to append, `"w"` to overwrite (default: append)
- `format`: File type - txt, py, md, html, css, js (default: txt)

Example: Create a shopping list
```python
create_note("shopping_list", "- Milk\n- Eggs\n- Bread\n")
```

`read_note(filename, format="txt")`
Reads and returns the content of a note file.

Parameters:
- `filename`: Name of the note to read
- `format`: File extension (default: txt)

`delete_chunk(filename, start, end, format)`
Removes a specific portion of text from a note.

Parameters:
- `filename`: Name of the file to edit
- `start`: Starting byte position
- `end`: Ending byte position  
- `format`: File extension

`list_notes()`
Shows all your available notes.

Returns: List of all note files in your directory

Example Usage

```python
# Create a new note
create_note("ideas", "Remember to call mom\n")

# Add more content
create_note("ideas", "Buy birthday gift for Sarah\n", mode="a")

# Read your notes
content = read_note("ideas")

# See all your notes
my_notes = list_notes()
```

File Organization

All notes are stored in the directory specified by `BASE_PATH`. The server automatically:
- Creates the directory if it doesn't exist
- Manages file extensions for you
- Keeps everything organized in one place

Supported File Types

- `.txt` - Plain text notes
- `.py` - Python scripts and code notes
- `.md` - Markdown documents  
- `.html` - HTML files
- `.css` - Stylesheets
- `.js` - JavaScript files

Configuration

Important: Before running, update the `BASE_PATH` variable to point to where you want your notes stored:

```python
BASE_PATH = "/home/username/my_notes"  # Linux/Mac
# or
BASE_PATH = "C:\\Users\\username\\Documents\\Notes"  # Windows
```

Tips

- Use descriptive filenames to keep your notes organized
- The append mode (`mode="a"`) is great for building lists or logs over time
- Use the `list_notes()` function regularly to see what you have
- Different file formats help organize different types of content

This MCP server makes note management simple and programmatic - perfect for integrating with AI assistants or automation workflows!
