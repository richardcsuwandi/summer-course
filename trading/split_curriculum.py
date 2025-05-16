import re
import os

INPUT_FILENAME = "/home/ubuntu/complete_curriculum_temp.md"
WEEKLY_OUTPUT_DIR = "/home/ubuntu/weekly_curriculum"
MASTER_FILENAME = "/home/ubuntu/curriculum.md"

WEEK_HEADER_REGEX = r"^\*\*Week (\d{1,2}) \(Days (\d{1,2}-\d{1,2})\): (.*)\*\*$"
PHASE_HEADER_REGEX = r"^## Phase \d+:.*$"
MONTH_HEADER_REGEX = r"^### Month \d+:.*$"

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def split_curriculum():
    ensure_dir(WEEKLY_OUTPUT_DIR)

    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    intro_content = []
    weekly_sections = []
    current_week_content = []
    current_week_info = None
    main_content_started = False

    # First, extract the main introduction part (before any Phase or Week headers)
    # And also capture Phase/Month headers that might appear before the first week's detailed content.
    intro_end_index = 0
    for i, line in enumerate(lines):
        if re.match(WEEK_HEADER_REGEX, line.strip()):
            main_content_started = True
            intro_end_index = i
            break
        intro_content.append(line)
        if re.match(PHASE_HEADER_REGEX, line.strip()) or re.match(MONTH_HEADER_REGEX, line.strip()):
             # These are part of the intro if they appear before the first week's content block
            pass # Already appended to intro_content
    
    # Process from where the first week starts
    for line_num in range(intro_end_index, len(lines)):
        line = lines[line_num]
        stripped_line = line.strip()
        week_match = re.match(WEEK_HEADER_REGEX, stripped_line)

        if week_match:
            if current_week_info and current_week_content:
                weekly_sections.append({
                    "info": current_week_info,
                    "content": "".join(current_week_content)
                })
                current_week_content = []
            
            week_num = week_match.group(1)
            week_days = week_match.group(2)
            week_theme = week_match.group(3).strip()
            current_week_info = {"num": week_num, "days": week_days, "theme": week_theme}
            current_week_content.append(line) # Include the week header in its file
        elif current_week_info: # Only append if we are inside a week's block
            current_week_content.append(line)

    # Add the last processed week
    if current_week_info and current_week_content:
        weekly_sections.append({
            "info": current_week_info,
            "content": "".join(current_week_content)
        })

    # Write weekly files
    for section in weekly_sections:
        week_num = section["info"]["num"]
        week_filename = os.path.join(WEEKLY_OUTPUT_DIR, f"week_{week_num}.md")
        with open(week_filename, "w", encoding="utf-8") as wf:
            wf.write(section["content"])
        print(f"Written: {week_filename}")

    # Create master curriculum.md file
    with open(MASTER_FILENAME, "w", encoding="utf-8") as mf:
        # Write the initial introduction part from the original file
        mf.write("".join(intro_content).strip() + "\n\n")
        
        mf.write("## Calendar Overview\n\n")
        mf.write("| Week | Days    | Theme                                                      | Link                                        |\n")
        mf.write("|------|---------|------------------------------------------------------------|---------------------------------------------|\n")
        for section in sorted(weekly_sections, key=lambda x: int(x["info"]["num"])):
            info = section["info"]
            link = f"[Week {info['num']}](./weekly_curriculum/week_{info['num']}.md)"
            # Ensure theme doesn't break table formatting if it contains pipes
            theme_cleaned = info['theme'].replace('|', '\\|') 
            mf.write(f"| {info['num']}    | {info['days']} | {theme_cleaned} | {link}     |\n")
    print(f"Written: {MASTER_FILENAME}")

if __name__ == "__main__":
    split_curriculum()

