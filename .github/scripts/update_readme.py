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
# CORE REPLACE (FIXED)
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
# UPDATE ROOT
# ======================
def update_root():
    folders = [
        d for d in os.listdir(ROOT)
        if os.path.isdir(d) and d not in IGNORE
    ]

    table = "| Thư mục | Số file PDF |\n"
    table += "|----------|-------------|\n"

    total_all = 0

    for f in sorted(folders):
        c = count_pdf(f)
        total_all += c
        table += f"| {f} | {c} |\n"

    table += f"| **Tổng** | **{total_all}** |\n"

    replace_block("README.md", "FILE_COUNT", table)


# ======================
# UPDATE DASHBOARD (ONE FOLDER)
# ======================
def update_dashboard(folder):
    readme = os.path.join(folder, "README.md")

    if not os.path.exists(readme):
        return

    subs = [
        d for d in os.listdir(folder)
        if os.path.isdir(os.path.join(folder, d))
    ]

    data = []

    # ✅ FIX: đếm toàn bộ PDF trong folder (bao gồm cả file trực tiếp)
    total = count_pdf(folder)

    for s in subs:
        sub_path = os.path.join(folder, s)

        # chỉ tính PDF riêng của subfolder đó
        c = count_pdf(sub_path)
        data.append((s, c))

    data.sort(key=lambda x: x[1], reverse=True)

    text = f"📊 **Tổng số PDF:** {total}\n\n"

    if data:
        text += "| Subfolder | Số file PDF |\n"
        text += "|-----------|-------------|\n"

        for s, c in data:
            text += f"| {s} | {c} |\n"
    else:
        text += "> Không có subfolder\n"

    replace_block(readme, "DASHBOARD", text)


# ======================
# AUTO SCAN ALL README
# ======================
def update_all_dashboards():
    for current_path, dirs, files in os.walk(ROOT):

        # skip internal folder
        if any(x in current_path for x in IGNORE):
            continue

        if "README.md" in files:

            if current_path == ".":
                continue

            print(f"🔍 Processing: {current_path}")
            update_dashboard(current_path)


# ======================
# MAIN
# ======================
if __name__ == "__main__":
    update_root()
    update_all_dashboards()
