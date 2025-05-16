#!/usr/bin/env python3

import os
import re
import glob

def transform_file(file_path):
    """
    Transform a markdown file to match the style in week_01.md
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # First, remove pinyin in parentheses from the title lines
    content = re.sub(r'(\d+\.\s+[\u4e00-\u9fff]+)\s+\([^)]+\)', r'\1', content)
    
    # Then, transform the pattern for bullet points with details/summary structure
    pattern = r'(\d+\.\s+.+?)\n\s+\*\s+\*\*pinyin:\*\*\s+(.+?)\n\s+\*\s+\*\*definition:\*\*\s+(.+?)\n\s+\*\s+\*\*usage:\*\*\s+(.+?)\n\s+\*\s+\*\*example:\*\*\s+(.+?)\n\s+\*\s+\*\*contexts:\*\*\s+(.+?)(?=\n\n|\n\d+\.\s+|$)'
    
    # Replace with details/summary structure like in week_01.md
    replacement = r'\1\n    <details>\n    <summary>Details</summary>\n    <ul>\n    <li><strong>pinyin:</strong> \2</li>\n    <li><strong>definition:</strong> \3</li>\n    <li><strong>usage:</strong> \4</li>\n    <li><strong>example:</strong> \5</li>\n    <li><strong>contexts:</strong> \6</li>\n    </ul>\n    </details>'
    
    transformed_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # If the pattern already has <summary></summary>, replace with <summary>Details</summary>
    transformed_content = re.sub(r'<summary></summary>', r'<summary>Details</summary>', transformed_content)
    
    # Write the transformed content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(transformed_content)
    
    print(f"Transformed: {file_path}")

def main():
    # Directory containing the markdown files
    course_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all week_*.md files for weeks 2-12
    week_files = []
    for week_num in range(2, 13):
        pattern = os.path.join(course_dir, "chinese", f"week_{week_num:02d}.md")
        matches = glob.glob(pattern)
        if not matches:
            pattern = os.path.join(course_dir, "chinese", f"week_{week_num}.md")
            matches = glob.glob(pattern)
        
        week_files.extend(matches)
    
    # Also look for any week_*.md files to catch potential variations in naming
    additional_files = glob.glob(os.path.join(course_dir, "chinese", "week_[0-9]*.md"))
    for file_path in additional_files:
        if file_path not in week_files and "week_01.md" not in file_path:
            week_files.append(file_path)
    
    if not week_files:
        print("No week files found for weeks 2-12")
        return
    
    print(f"Found {len(week_files)} week files to transform:")
    for file_path in week_files:
        print(f"  - {file_path}")
    
    # Transform each file
    for file_path in week_files:
        transform_file(file_path)
    
    print("Transformation complete!")

if __name__ == "__main__":
    main()
