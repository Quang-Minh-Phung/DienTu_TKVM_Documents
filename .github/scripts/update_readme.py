import os
import re

ROOT = "."

IGNORE = [".git", ".github"]

# ==============================
# COUNT PDF (recursive)
# ==============================
def count_pdf(folder):
    total = 0
    for _, _, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(".pdf"):
                total += 1
    return total

# ==============================
# ROOT TABLE (README.md)
# ==============================
def update_root_readme():
    folders = [
        d for d in os.listdir(ROOT)
        if os.path.isdir(d) and d not in IGNORE
    ]

    table = "| Thư mục | Số file PDF |\n"
    table += "|----------|-------------|\n"

    total_all = 0

    for f in sorted(folders):
        count = count_pdf(f)
        total_all += count
        table += f"| {f} | {count} |\n"

    table += f"| **Tổng** | **{total_all}** |\n"

    # đọc README root
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"<!-- FILE_COUNT_START -->.*?<!-- FILE_COUNT_END -->",
        re.DOTALL
    )

    new_section = f"<!-- FILE_COUNT_START -->\n{table}<!-- FILE_COUNT_END -->"

    updated = pattern.sub(new_section, content)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)

    print("✅ Updated root README")


# ==============================
# DASHBOARD SUBFOLDER
# ==============================
def update_dashboard(folder):
    readme_path = os.path.join(folder, "README.md")

    if not os.path.exists(readme_path):
        print(f"❌ No README in {folder}")
        return

    subfolders = [
        d for d in os.listdir(folder)
        if os.path.isdir(os.path.join(folder, d))
    ]

    data = []
    total = 0

    for sub in subfolders:
        path = os.path.join(folder, sub)
        count = count_pdf(path)
        total += count
        data.append((sub, count))

    # sort theo số file
    data.sort(key=lambda x: x[1], reverse=True)

    # tạo bảng
    dashboard = f"📊 **Tổng số PDF:** {total}\n\n"
    dashboard += "| Subfolder | Số file PDF |\n"
    dashboard += "|-----------|-------------|\n"

    for sub, count in data:
        dashboard += f"| {sub} | {count} |\n"

    # đọc README
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"<!-- DASHBOARD_START -->.*?<!-- DASHBOARD_END -->",
        re.DOTALL
    )

    new_section = f"<!-- DASHBOARD_START -->\n{dashboard}<!-- DASHBOARD_END -->"

    updated = pattern.sub(new_section, content)

    # nếu KHÔNG match → báo lỗi luôn
    if content == updated:
        print(f"⚠️ Pattern NOT found in {readme_path}")
    else:
        print(f"✅ Updated dashboard: {folder}")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    update_root_readme()

    # UPDATE DASHBOARD CHO FOLDER CỤ THỂ
    update_dashboard("Tai_Lieu_Tham_Khao")
