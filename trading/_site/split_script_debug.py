import re
import os

def split_curriculum_debug():
    input_file = "/home/ubuntu/90_Day_Stock_Trading_Curriculum.md"
    output_dir = "/home/ubuntu/weekly_curriculum"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        for f_name in os.listdir(output_dir):
            if os.path.isfile(os.path.join(output_dir, f_name)):
                 os.remove(os.path.join(output_dir, f_name))

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"Total lines read from curriculum: {len(lines)}")

    intro_content = []
    content_to_split_from = []
    conclusion_content = []
    
    # Adjusted regex: Handles optional spaces better and non-greedy theme capture.
    # It expects the line to start with "**Week", then number, then "(Days ...):", then theme, optionally ending with "**"
    week_header_pattern = re.compile(r"^\*\*Week\s+(\d+)\s*\(Days.*?\):\s*(.+?)(?:\s*\*\*|$)")

    # Extract Introduction
    intro_end_index = 0
    first_major_header_found = False
    # Find the end of the intro section (before the first "## Phase" or actual "**Week")
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        # Check if the line indicates the start of the main curriculum body
        if stripped_line.startswith("## Phase") or week_header_pattern.match(stripped_line):
            intro_end_index = i
            first_major_header_found = True
            print(f"Intro section ends at line {i}: Content starts with \t'{stripped_line[:50]}...'" )
            break
    else:
        # Fallback if no clear delimiter is found after initial lines
        if lines and lines[0].strip().startswith("# 90-Day US Stock Trading Curriculum"):
             intro_end_index = min(len(lines), 15) # Default to a small intro (e.g. first 15 lines)
             print(f"No clear phase/week header for intro end, defaulting intro to line {intro_end_index}")
        else:
            intro_end_index = 0 # No intro found or file doesn't start with main title
            print(f"No intro section identified by typical markers.")

    if intro_end_index > 0 : # If intro_end_index is 0, it means no intro was sliced off.
        intro_content = lines[:intro_end_index]
        content_to_split_from = lines[intro_end_index:]
    else: # No intro found or file doesn't start with main title, treat all as content_to_split_from
        intro_content = []
        content_to_split_from = lines
        print("No intro content sliced, attempting to split all lines.")

    print(f"Length of content_to_split_from: {len(content_to_split_from)}")
    if content_to_split_from:
        print("First 5 lines of content_to_split_from (potential curriculum body):")
        for k in range(min(5, len(content_to_split_from))):
            print(f"  Line index {k} (original line {k+intro_end_index}): {content_to_split_from[k].strip()[:100]}...")
    
    # Extract Conclusion
    potential_conclusion_start_in_cts = -1
    if content_to_split_from:
        for i in range(len(content_to_split_from) - 1, max(-1, len(content_to_split_from) - 20), -1):
            line_text = content_to_split_from[i]
            if "This concludes the 90-day curriculum." in line_text:
                potential_conclusion_start_in_cts = i
                print(f"Conclusion marker 'This concludes...' found at relative line {i} in content_to_split_from.")
                break
            if line_text.strip().endswith("Good luck!") and potential_conclusion_start_in_cts == -1:
                 potential_conclusion_start_in_cts = i
                 print(f"Conclusion marker 'Good luck!' found at relative line {i} in content_to_split_from.")

    if potential_conclusion_start_in_cts != -1:
        conclusion_content = content_to_split_from[potential_conclusion_start_in_cts:]
        content_to_split_from = content_to_split_from[:potential_conclusion_start_in_cts]
        print(f"Conclusion extracted. New length of content_to_split_from: {len(content_to_split_from)}")
    else:
        print("No conclusion section found by markers.")
    
    # Save intermediate files for debugging
    with open(os.path.join(output_dir, "debug_intro_for_master.md"), "w", encoding="utf-8") as f:
        f.writelines(intro_content)
    with open(os.path.join(output_dir, "debug_conclusion_for_master.md"), "w", encoding="utf-8") as f:
        f.writelines(conclusion_content)

    week_starts_indices = []
    print("\nScanning for week headers in the processed content_to_split_from:")
    for i, line in enumerate(content_to_split_from):
        stripped_line = line.strip()
        match = week_header_pattern.match(stripped_line)
        if match:
            week_num = int(match.group(1))
            theme = match.group(2).strip()
            # Clean up theme if it was captured with trailing markdown bold characters
            if theme.endswith("**"):
                theme = theme[:-2].strip()
            week_starts_indices.append((week_num, theme, i)) # Store index relative to content_to_split_from
            print(f"  MATCHED Week Header: Line index {i} (original line {i + intro_end_index}), Week {week_num}, Theme: '{theme}'")
        elif stripped_line.lower().startswith("**week"):
            print(f"  POTENTIAL MISS (does not match regex): Line index {i} (original line {i + intro_end_index}): 	'{stripped_line[:100]}...")

    if not week_starts_indices:
        print("Error: No week headers found in the main curriculum content for splitting after intro/conclusion processing.")
        if content_to_split_from:
            with open(os.path.join(output_dir, "debug_remaining_content_no_weeks_found.md"), "w", encoding="utf-8") as f:
                f.writelines(content_to_split_from)
            print("Saved current content_to_split_from to debug_remaining_content_no_weeks_found.md")
        return

    headers_before_first_week = []
    if week_starts_indices: # Ensure week_starts_indices is not empty
        first_week_original_content_start_index = week_starts_indices[0][2]
        headers_before_first_week = content_to_split_from[:first_week_original_content_start_index]
        if headers_before_first_week:
            print(f"Identified {len(headers_before_first_week)} header lines before Week {week_starts_indices[0][0]}:")
            # for h_line in headers_before_first_week: print(f"    {h_line.strip()[:100]}...")

    themes_for_master_file = []
    for i in range(len(week_starts_indices)):
        week_num, week_theme, current_week_start_idx_in_cts = week_starts_indices[i]
        themes_for_master_file.append((week_num, week_theme))

        next_week_start_idx_in_cts = len(content_to_split_from)
        if i + 1 < len(week_starts_indices):
            next_week_start_idx_in_cts = week_starts_indices[i+1][2]
            
        # Content for this week is from its header up to the header of the next week
        week_content_block = content_to_split_from[current_week_start_idx_in_cts : next_week_start_idx_in_cts]
        
        final_content_for_this_week_file = []
        # Prepend Phase/Month headers (that were before the very first week) only to the first actual week file generated
        if i == 0 and headers_before_first_week:
            final_content_for_this_week_file.extend(headers_before_first_week)
        
        final_content_for_this_week_file.extend(week_content_block)
            
        output_filename = os.path.join(output_dir, f"week_{week_num:02d}.md")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.writelines(final_content_for_this_week_file)
        print(f"Written: {output_filename}")

    with open(os.path.join(output_dir, "debug_themes_for_master.txt"), "w", encoding="utf-8") as f:
        for week_num, theme in themes_for_master_file:
            f.write(f"{week_num}:{theme}\n")

    print("Splitting complete (debug version).")

if __name__ == "__main__":
    split_curriculum_debug()

