import os

ROOT = "."

IGNORE = [".git", ".github"]

# ======================
# COUNT PDF
# ======================
def count_pdf(folder):
    total = 0
    for _, _, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(".pdf"):
                total += 1
    return total


# ======================
# UPDATE ROOT README
# ======================
def update_root():
    folders = [
        d for d in os.listdir(ROOT)
        if os.path.isdir(d) and d not in IGNORE
    ]

    rows = []
    total_all = 0

    for f in sorted(folders):
        c = count_pdf(f)
        total_all += c
        rows.append((f, c))

    table = "| Thư mục | Số file PDF |\n"
    table += "|----------|-------------|\n"

    for name, c in rows:
        table += f"| {name} | {c} |\n"

    table += f"| **Tổng** | **{total_all}** |\n"

    replace_block("README.md", "FILE_COUNT", table)


# ======================
# UPDATE DASHBOARD
# ======================
def update_dashboard(folder):
    readme = os.path.join(folder, "README.md")

    if not os.path.exists(readme):
        print("❌ Missing:", readme)
        return

    subs = [
        d for d in os.listdir(folder)
        if os.path.isdir(os.path.join(folder, d))
    ]

    data = []
    total = 0

    for s in subs:
        c = count_pdf(os.path.join(folder, s))
        total += c
        data.append((s, c))

    data.sort(key=lambda x: x[1], reverse=True)

    text = f"📊 **Tổng số PDF:** {total}\n\n"
    text += "| Subfolder | Số file PDF |\n"
    text += "|-----------|-------------|\n"

    for s, c in data:
        text += f"| {s} | {c} |\n"

    replace_block(readme, "DASHBOARD", text)


# ======================
# CORE (NO REGEX)
# ======================
def replace_block(filepath, tag, new_content):
    start = f"<!-- {tag}_START -->"
    end = f"<!-- {tag}_END -->"

    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()

    if start not in data or end not in data:
        print(f"⚠️ TAG NOT FOUND in {filepath}")
        return

    before = data.split(start)[0]
    after = data.split(end)[1]

    new_data = before + start + "\n" + new_content + end + after

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_data)

    print(f"✅ Updated: {filepath}")


# ======================
# MAIN
# ======================
if __name__ == "__main__":
    update_root()
    update_dashboard("Tai_Lieu_Tham_Khao")
