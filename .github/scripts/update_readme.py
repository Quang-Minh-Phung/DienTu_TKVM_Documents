import os
import re

ROOT = "."

IGNORE = [".git", ".github", "scripts"]

def get_folders():
    return [
        d for d in os.listdir(ROOT)
        if os.path.isdir(d) and d not in IGNORE
    ]

def count_files(folder):
    count = 0
    for _, _, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(".pdf"):
                count += 1
    return count

folders = sorted(get_folders())

table = "| Thư mục | Số file |\n"
table += "|----------|---------|\n"

total = 0

for f in folders:
    c = count_files(f)
    total += c
    table += f"| {f} | {c} |\n"

table += f"| **Tổng** | **{total}** |\n"

# đọc README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start = "<!-- FILE_COUNT_START -->"
end = "<!-- FILE_COUNT_END -->"

new_content = re.sub(
    f"{start}.*?{end}",
    f"{start}\n{table}{end}",
    content,
    flags=re.S
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ Updated README")
