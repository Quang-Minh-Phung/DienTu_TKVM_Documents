👋 Chào mừng bạn đến với kho tài liệu học thuật do mình tự tổng hợp để hỗ trợ bạn trong việc tự học Điện Tử, đặc biệt là hướng Thiết Kế Vi Mạch 🙂

Kho tài liệu này gồm các cuốn sách, dặc tả kỹ thuật được:
1. Giới thiệu trong quá trình mình học chuyên ngành Điện Tử, bởi các giảng viên của chuyên ngành Điện Tử đã có kinh nghiệm trong lĩnh vực Thiết Kế Vi Mạch.
2. Chia sẻ bởi các kỹ sư Thiết Kế Vi Mạch ở quy trình Front End, Cell-based/Automatic Design Flow và Full-custom Design Flow trên 20 năm kinh nghiệm.
3. Mình phải tự mò trong quá trình giải quyết các vấn đề của các công việc được giao trong dự án 😭.
4. Chia sẻ bởi các bạn thực tập sinh từ BKU, HCMUTE, UIT, TDTU, PTIT mà mình quen trong thời gian mình học tập, làm việc cũng như hướng dẫn kỹ thuật 🥰.
Mình xin thống kê số lượng tài liệu hiện có ở các thư mục chuyên môn để bạn nắm thông tin.
Sau phần thống kê là nơi mình bắt đầu hỗ trợ hướng dẫn bạn cách tự học cùng với nguồn tài liệu tham khảo mà mình đã tổng hợp trong đây nha 😁.

---

## 📂 Dashboard tài liệu
<!-- DASHBOARD_START -->
📊 **Tổng số PDF:** 220

| Subfolder | Số file PDF |
|-----------|-------------|
| Firmware_and_Scripting | 31 |
| RTL_DE__Testbench_DV | 31 |
| Arch_and_uArch | 27 |
| Dien_Tu_Tuong_Tu | 23 |
| High_Speed_Storage | 22 |
| AMBA_protocols | 14 |
| Dien_Tu_So | 13 |
| Dien_Tu_Can_Ban | 11 |
| MCTP_SMBus_I2C_CRC | 9 |
| Supporting_Documents | 7 |
| DSP | 7 |
| Power_analysis | 7 |
| PLL | 6 |
| DFT | 5 |
| MEMS_NEMS | 5 |
| SECDED | 2 |
<!-- DASHBOARD_END -->

---

## 📚 Hướng đẫn tự học 😁
- Thành thật mà nói thì việc bạn theo hướng chuyên ngành Điện Tử, rồi tập trung chuyên sâu vào Thiết Kế Vi Mạch cần bạn ở giai đoạn đầu học phải vững nền tảng, có điều kiến thức sẽ hơi nhàm chán với đa số 😢. Nhưng mình mong là bạn vẫn sẽ giữ vững lộ trình mà mình đề ra sau đây để bạn có thể đi xa hơn với định hướng đã chọn.
- Việc học chuyên ngành Điện Tử của bạn có thể chia ra làm 3 giai đoạn sau:
### ***Giai đoạn 1: Nền tảng Điện Tử bắt buộc***
Trước khi bạn chọn hướng Thiết Kế Vi Mạch cụ thể, bạn cần phải nắm vững lý thuyết mạch và các linh kiện nền tảng.
Bạn hãy bắt đầu bằng việc click vô [Điện Tử Căn Bản](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Dien_Tu_Can_Ban) để di chuyển đến thư mục chứa các tài liệu tập trung hoàn toàn vào điện tử căn bản cho dân học Điện Tử thuần 😁
### ***Giai đoạn 2: Lựa chọn định hướng chuyên môn***
Quy trình Thiết Kế Vi Mạch thường gồm 2 quy trình chính và luôn kết hợp với nhau để tạo ra sản phẩm cuối cùng đó là Cell-based Design Flow và Full-custom Design Flow.
1. #### **Cell-based Design Flow**:
Ở quy trình thiết kế này thì bạn đã chọn học sâu vào các thiết kế Digital nhưng vẫn cần nắm căn bản Analog:
- [Điện Tử Số](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Dien_Tu_So)
- [Điện Tử Tương Tự -> Op-amp/Mixed-signal](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Dien_Tu_Tuong_Tu/CMOS_OPAMP)
- [Design For Testability](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/DFT)
- [Xử lý tín hiệu số](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/DSP)
- Cân nhắc đọc qua [Điện Tử Công Suất](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Dien_Tu_Tuong_Tu/Power_Electronics) để nắm nền tảng về Power Analysis.
- Các kiến thức bổ trợ cho công việc: [Linux command, Makefile, Git](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Supporting_Documents)
##### Nếu bạn học tới đây và cảm thấy vất vả quá 😅, cũng như định hướng của bạn là tập trung vào các công việc như Synthesis/STA, Physical Design, Physical Implementation, Hardware Validation thì bạn có thể trực tiếp nhảy sang học Scripting Languages như Tcl, Python, Perl, Sed và Awk ở [Scripting Language](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Firmware_and_Scripting)
##### Nếu bạn vẫn cảm thấy ổn, có định hướng công việc là RTL DE, DV thì bạn sẽ phải tiếp tục học các phần sau 😁 (khá kinh khủng nha 🐧)
- [Lập trình firmware](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Firmware_and_Scripting/C)
- [Cấu trúc dữ liệu và giải thuật](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Firmware_and_Scripting/DSA): Bạn nên đọc các tài liệu và giải thuật phần mềm trước khi đọc tài liệu về [giải thuật phần cứng](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/blob/main/Tai_Lieu_Tham_Khao/Firmware_and_Scripting/DSA/_DSA_for_VLSI.pdf)
- [Scripting Languages: Python, Perl, Tcl, Sed và Awk](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Firmware_and_Scripting)
- [Ngôn ngữ mô tả/thiết kế và kiểm định phần cứng](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/RTL_DE__Testbench_DV): Bạn nên bắt đầu ở [RTL](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/RTL_DE__Testbench_DV/RTL_for_synthesis) rồi hãy qua [DV cho người mới bắt đầu](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/RTL_DE__Testbench_DV/DV/Starter) sau khi đã nắm vững mô tả/thiết kế mạch.
- Các giao thức AMBA thường sử dụng trong kiến trúc SoC: Bạn nên bắt đầu theo thứ tự sau: [APB](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/blob/main/Tai_Lieu_Tham_Khao/AMBA_protocols/_apb_architecture_spec.pdf) -> [ASB](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/blob/main/Tai_Lieu_Tham_Khao/AMBA_protocols/_AMBA_Specification_rev2.pdf) -> [AHB](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/blob/main/Tai_Lieu_Tham_Khao/AMBA_protocols/_ahb_protocol_spec.pdf) -> [AXI](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/blob/main/Tai_Lieu_Tham_Khao/AMBA_protocols/_axi_protocol_spec.pdf).
2. #### **Full-custom Design Flow**:
Ở quy trình thiết kế này thì bạn đã chọn học sâu vào các thiết kế Analog, nhưng vẫn cần nắm căn bản Digital:
- [Điện Tử Tương Tự](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Dien_Tu_Tuong_Tu): trong đây bạn có thể bỏ qua RF nha do bạn chỉ tập trung học thêm RF nếu bạn làm về các thiết kế siêu cao tần.
- [Điện Tử Số -> CMOS VLSI Custom-based Design](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Dien_Tu_So/CMOS_custom_based)
- [PLL chuyên sâu](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/PLL)
### ***Giai đoạn 3: Bổ sung các kiến thức chuyên sâu***
Ở giai đoạn này có nghĩa là bạn đang ở vị trí thực tập sinh hoặc bắt đầu trở thành một nhân viên kỹ thuật hoặc kỹ sư Thiết Kế Vi Mạch chính thức 😁
Từ giai đoạn này thì con đường học tập của mình và bạn sẽ là kế hoạch dài hạn và không có thời gian kết thúc 😅
Bạn chỉ nên theo hướng dẫn bên dưới nếu bạn đang làm DE hoặc DV mà tập trung vào các thiết kế xử lý và lưu trữ dữ liệu nha 😅 (thực tế thì việc học không hề giới hạn nên bạn có thể tham khảo nếu có đam mê nha 😁)
1. [Kiến Trúc và Vi Kiến Trúc Máy Tính](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Arch_and_uArch)
2. [DV nâng cao](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/RTL_DE__Testbench_DV/DV): bỏ qua phần Starter nha do bạn đã xong ở giai đoạn 2.
3. [Các giao thức, thiết kế lưu trữ tốc độ cao](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/High_Speed_Storage)
4. [Phát hiện và khôi phục lỗi trong lưu trữ](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/SECDED)
5. [Các giao thức ngoại vi nâng cao](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/MCTP_SMBus_I2C_CRC)
6. [Phân tích công suất](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/Power_analysis)
7. [Các giao thức AMBA nâng cao](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/AMBA_protocols): tập trung vào các giao thức ngoài 4 giao thức cơ bản ở giai đoạn 2.
8. [MEMS-NEMS](https://github.com/Quang-Minh-Phung/DienTu_TKVM_Documents/tree/main/Tai_Lieu_Tham_Khao/MEMS_NEMS): Đây là phần theo chương trình đào tạo cũ của chuyên ngành Điện Tử bên HCMUS 😅, bản thân mình thấy rất có ích trong tư duy công việc nên mình xin đính kèm nha 😁

---

Vậy là mình đã trình bày xong phần hướng dẫn tổng quát, mình chúc bạn học tôt nha 😁
