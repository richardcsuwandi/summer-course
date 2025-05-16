import re
import os

def split_curriculum():
    input_file = "/home/ubuntu/90_Day_Stock_Trading_Curriculum.md"
    output_dir = "/home/ubuntu/weekly_curriculum"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        # Clean up old files if any, to prevent appending or errors
        for f_name in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, f_name))

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    intro_content = []
    content_to_split_from = []
    conclusion_content = []
    
    week_header_pattern = re.compile(r"^\*\*Week (\d+)\s*\(Days .*\):(.*)")

    # Extract Introduction (everything before the first Phase or Week header)
    intro_end_index = 0
    first_major_header_found = False
    for i, line in enumerate(lines):
        # Stop intro if a Phase or Week header is found
        if line.strip().startswith("## Phase ") or week_header_pattern.match(line.strip()):
            intro_end_index = i
            first_major_header_found = True
            break
    else: # If no phase or week header found after intro section
        if lines[0].strip().startswith("# 90-Day US Stock Trading Curriculum"):
             # This case means the file might be only intro, or structure is very different
             # For safety, assume intro is only the first few lines if no clear delimiter
             intro_end_index = min(len(lines), 5) # Default to a small intro if no clear delimiter
        else:
            intro_end_index = 0 # No intro found

    if first_major_header_found:
        intro_content = lines[:intro_end_index]
        content_to_split_from = lines[intro_end_index:]
    else: # No major headers found, assume all content is for splitting or it's just intro
        # If the file starts with the main title, assume it's mostly intro if no structure follows
        if lines and lines[0].strip().startswith("# 90-Day US Stock Trading Curriculum") and not any(week_header_pattern.match(l.strip()) for l in lines):
            intro_content = lines
            content_to_split_from = []
        else: # Assume all content is for splitting if no clear intro section
            intro_content = []
            content_to_split_from = lines

    # Extract Conclusion (last few meaningful lines)
    # Search for "This concludes the 90-day curriculum." or "Good luck!"
    potential_conclusion_start = -1
    if content_to_split_from: # Search in the part that's supposed to be curriculum body
        for i in range(len(content_to_split_from) - 1, max(-1, len(content_to_split_from) - 10), -1):
            if "This concludes the 90-day curriculum." in content_to_split_from[i]:
                potential_conclusion_start = i
                break
            if content_to_split_from[i].strip().endswith("Good luck!") and potential_conclusion_start == -1:
                 # Prefer the longer conclusion marker if found, otherwise take Good luck
                 potential_conclusion_start = i

    if potential_conclusion_start != -1:
        conclusion_content = content_to_split_from[potential_conclusion_start:]
        content_to_split_from = content_to_split_from[:potential_conclusion_start]
    
    # Save intro and conclusion for master file
    with open(os.path.join(output_dir, "intro_for_master.md"), "w", encoding="utf-8") as f:
        f.writelines(intro_content)
    with open(os.path.join(output_dir, "conclusion_for_master.md"), "w", encoding="utf-8") as f:
        f.writelines(conclusion_content)

    # Splitting the main content into weekly files
    week_starts_indices = [] # List of (week_num, theme, line_index_in_content_to_split_from)
    for i, line in enumerate(content_to_split_from):
        match = week_header_pattern.match(line.strip())
        if match:
            week_starts_indices.append((int(match.group(1)), match.group(2).strip(), i))

    if not week_starts_indices:
        print("Error: No week headers found in the main curriculum content for splitting.")
        # If there's content_to_split_from but no week headers, save it to a misc file
        if content_to_split_from:
            with open(os.path.join(output_dir, "remaining_content.md"), "w", encoding="utf-8") as f:
                f.writelines(content_to_split_from)
            print("Saved remaining content to remaining_content.md")
        return

    # Any content before the first week header in content_to_split_from (e.g. Phase/Month headers)
    # should be prepended to the first week's file.
    first_week_content_start_index = week_starts_indices[0][2]
    headers_before_first_week = content_to_split_from[:first_week_content_start_index]

    themes_for_master_file = []

    for i in range(len(week_starts_indices)):
        week_num, week_theme, start_idx_in_content = week_starts_indices[i]
        themes_for_master_file.append((week_num, week_theme))

        end_idx_in_content = len(content_to_split_from)
        if i + 1 < len(week_starts_indices):
            end_idx_in_content = week_starts_indices[i+1][2]
            
        # The content for this week starts from its header line
        week_content_block = content_to_split_from[start_idx_in_content : end_idx_in_content]
        
        final_content_for_this_week_file = []
        # Prepend Phase/Month headers only to the very first weekly file if they exist
        if i == 0 and headers_before_first_week:
            final_content_for_this_week_file.extend(headers_before_first_week)
        
        final_content_for_this_week_file.extend(week_content_block)
            
        output_filename = os.path.join(output_dir, f"week_{week_num:02d}.md")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.writelines(final_content_for_this_week_file)
        print(f"Written: {output_filename}")

    # Save themes for master calendar creation later
    with open(os.path.join(output_dir, "themes_for_master.txt"), "w", encoding="utf-8") as f:
        for week_num, theme in themes_for_master_file:
            f.write(f"{week_num}:{theme}\n")

    print("Splitting complete.")

if __name__ == "__main__":
    split_curriculum()

