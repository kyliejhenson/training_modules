# Generate Visual Output with Skills

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Skills can bundle and run scripts in any language, giving Claude capabilities beyond what's possible in a single prompt. One powerful pattern is generating visual output: interactive HTML files that open in your browser for exploring data, debugging, or creating reports.

This example creates a codebase explorer: an interactive tree view where you can expand and collapse directories, see file sizes at a glance, and identify file types by color.

### Step 1: Create the Skill directory

```bash
mkdir -p ~/.claude/skills/codebase-visualizer/scripts
```

### Step 2: Create the SKILL.md

Create `~/.claude/skills/codebase-visualizer/SKILL.md`. The description tells Claude when to activate this Skill, and the instructions tell Claude to run the bundled script:

````yaml
---
name: codebase-visualizer
description: Generate an interactive collapsible tree visualization of your codebase. Use when exploring a new repo, understanding project structure, or identifying large files.
allowed-tools: Bash(python *)
---

# Codebase Visualizer

Generate an interactive HTML tree view that shows your project's file structure with collapsible directories.

## Usage

Run the visualization script from your project root:

```bash
python ~/.claude/skills/codebase-visualizer/scripts/visualize.py .
```

This creates `codebase-map.html` in the current directory and opens it in your default browser.

## What the visualization shows

- **Collapsible directories**: Click folders to expand/collapse
- **File sizes**: Displayed next to each file
- **Colors**: Different colors for different file types
- **Directory totals**: Shows aggregate size of each folder
````

### Step 3: Create the Python script

Create `~/.claude/skills/codebase-visualizer/scripts/visualize.py`. This script scans a directory tree and generates a self-contained HTML file with:

- A summary sidebar showing file count, directory count, total size, and number of file types
- A bar chart breaking down the codebase by file type (top 8 by size)
- A collapsible tree where you can expand and collapse directories, with color-coded file type indicators

The script requires Python but uses only built-in libraries, so there are no packages to install.

To test, open Claude Code in any project and ask "Visualize this codebase." Claude runs the script, generates `codebase-map.html`, and opens it in your browser.

This pattern works for any visual output: dependency graphs, test coverage reports, API documentation, or database schema visualizations. The bundled script does the heavy lifting while Claude handles orchestration.
