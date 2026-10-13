import streamlit as st
st.image("logo.jpg")
# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰APP TÍNH TIỀN GỬI TIẾT KIỆM TẠI NGÂN HÀNG_TRẦN THỊ HUỲNH NGHI")
st.write("Tính toán tiền lãi theo phương pháp **lãi đơn** hoặc **lãi kép**.")

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================
st.subheader("📋 Thông tin tiền gửi")

# Số tiền gửi
tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=100_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

# Kỳ hạn
ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Loại lãi
loai_lai = st.selectbox(
    "Hình thức tính lãi",
    ["Lãi đơn", "Lãi kép"]
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    [
        "Lãnh lãi hàng tháng",
        "Lãnh lãi hàng quý",
        "Lãnh lãi cuối kỳ"
    ]
)

# Lãi suất
lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# =========================
# NÚT TÍNH
# =========================
if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Chuyển lãi suất từ % sang số thập phân
    r = lai_suat / 100

    # Thời gian theo năm
    so_nam = ky_han / 12

    # Số kỳ nhận lãi
    if hinh_thuc == "Lãnh lãi hàng tháng":
        so_ky = ky_han
        lai_suat_ky = r / 12

    elif hinh_thuc == "Lãnh lãi hàng quý":
        so_ky = ky_han / 3
        lai_suat_ky = r / 4

    else:
        so_ky = 1
        lai_suat_ky = r

    # =========================
    # TÍNH LÃI ĐƠN
    # =========================
    if loai_lai == "Lãi đơn":

        # Công thức:
        # Tiền lãi = Gốc × lãi suất năm × số năm
        tong_lai = tien_gui * r * so_nam

        # Tiền lãi mỗi kỳ
        if hinh_thuc == "Lãnh lãi hàng tháng":
            lai_dinh_ky = tien_gui * r / 12

        elif hinh_thuc == "Lãnh lãi hàng quý":
            lai_dinh_ky = tien_gui * r / 4

        else:
            lai_dinh_ky = tong_lai

        tong_tien = tien_gui + tong_lai

    # =========================
    # TÍNH LÃI KÉP
    # =========================
    else:

        # Lãi kép được nhập gốc vào cuối mỗi kỳ
        # Số kỳ tương ứng với hình thức nhận lãi

        if hinh_thuc == "Lãnh lãi hàng tháng":
            so_ky = ky_han
            lai_suat_ky = r / 12

        elif hinh_thuc == "Lãnh lãi hàng quý":
            so_ky = ky_han / 3
            lai_suat_ky = r / 4

        else:
            # Lãnh cuối kỳ: ghép lãi theo năm
            # Nếu kỳ hạn dưới 1 năm thì tính theo phần kỳ hạn
            so_ky = so_nam
            lai_suat_ky = r

        # Nếu số kỳ là số nguyên thì tính bình thường
        if so_ky == int(so_ky):
            so_ky = int(so_ky)

        tong_tien = tien_gui * (1 + lai_suat_ky) ** so_ky
        tong_lai = tong_tien - tien_gui

        # Lãi phát sinh trong kỳ đầu tiên
        lai_dinh_ky = tien_gui * lai_suat_ky

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================
    st.divider()
    st.subheader("📊 Kết quả tính toán")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💵 Tiền lãi định kỳ",
            f"{lai_dinh_ky:,.0f} VNĐ"
        )

        st.metric(
            "💰 Tổng tiền lãi",
            f"{tong_lai:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "🏦 Tiền gốc",
            f"{tien_gui:,.0f} VNĐ"
        )

        st.metric(
            "💎 Tổng gốc + lãi",
            f"{tong_tien:,.0f} VNĐ"
        )
       ```python
    # ==========================================
    # 🤖 TRỢ LÝ GIẢI THÍCH KẾT QUẢ TÍNH LÃI
    # ==========================================

    st.divider()
    st.subheader("🤖 Trợ lý giải thích kết quả")

    st.write(
        "Trợ lý sẽ giúp bạn hiểu rõ khoản tiền gửi, "
        "tiền lãi và tổng số tiền dự kiến nhận được."
    )

    # Tính tỷ lệ tiền lãi so với tiền gốc
    if tien_gui > 0:
        ty_le_lai = tong_lai / tien_gui * 100
    else:
        ty_le_lai = 0

    # Tạo phần giải thích theo số liệu đã tính
    st.markdown("### 📊 1. Tổng quan khoản tiết kiệm")

    if tien_gui == 0:
        st.info(
            "Bạn chưa nhập số tiền gửi. "
            "Hãy nhập số tiền lớn hơn 0 để xem phân tích chi tiết."
        )

    else:
        st.success(
            f"Với số tiền gửi **{tien_gui:,.0f} VNĐ**, "
            f"trong kỳ hạn **{ky_han} tháng**, "
            f"với lãi suất **{lai_suat:.2f}%/năm**, "
            f"tiền lãi dự kiến là **{tong_lai:,.0f} VNĐ**. "
            f"Tổng tiền gốc và lãi là **{tong_tien:,.0f} VNĐ**."
        )

        st.write(
            f"Tiền lãi tương đương **{ty_le_lai:.2f}%** "
            "so với số tiền gốc ban đầu."
        )

    # Giải thích phương pháp tính lãi
    st.markdown("### 📐 2. Giải thích phương pháp tính lãi")

    if loai_lai == "Lãi đơn":
        st.write(
            "**Bạn đang sử dụng phương pháp lãi đơn.** "
            "Tiền lãi được tính dựa trên số tiền gốc ban đầu. "
            "Phần lãi không được cộng vào gốc để tiếp tục sinh lãi "
            "trong mô hình tính toán này."
        )

        st.latex(r"I = P \\times r \\times t")

        st.write(
            f"Với khoản tiền gửi của bạn, tiền lãi được tính "
            f"dựa trên số tiền gốc {tien_gui:,.0f} VNĐ, "
            f"lãi suất {lai_suat:.2f}%/năm và thời gian "
            f"{so_nam:.2f} năm."
        )

    else:
        st.write(
            "**Bạn đang sử dụng phương pháp lãi kép.** "
            "Trong mô hình này, tiền lãi được cộng vào gốc "
            "theo chu kỳ ghép lãi. Những kỳ tiếp theo có thể "
            "tạo ra lãi trên cả tiền gốc và phần lãi đã tích lũy."
        )

        st.latex(r"A = P(1+r)^n")

        st.write(
            "Số tiền cuối kỳ được xác định dựa trên số tiền gốc, "
            "lãi suất mỗi kỳ và số kỳ ghép lãi đã chọn."
        )

    # Giải thích hình thức nhận lãi
    st.markdown("### 💵 3. Giải thích hình thức nhận lãi")

    if hinh_thuc == "Lãnh lãi hàng tháng":
        st.write(
            "Bạn đã chọn nhận lãi hằng tháng. "
            f"Theo phép tính hiện tại, số tiền lãi mỗi tháng "
            f"được ước tính là **{lai_dinh_ky:,.0f} VNĐ** "
            "đối với khoản tiền gửi này."
        )

    elif hinh_thuc == "Lãnh lãi hàng quý":
        st.write(
            "Bạn đã chọn nhận lãi hằng quý. "
            f"Theo phép tính hiện tại, số tiền lãi mỗi quý "
            f"được ước tính là **{lai_dinh_ky:,.0f} VNĐ**."
        )

    else:
        st.write(
            "Bạn đã chọn nhận lãi cuối kỳ. "
            f"Tổng tiền lãi dự kiến khi kết thúc kỳ hạn là "
            f"**{tong_lai:,.0f} VNĐ**."
        )

    # Đưa ra nhận xét theo kết quả
    st.markdown("### 💡 4. Nhận xét về khoản tiền gửi")

    if lai_suat == 0:
        st.info(
            "Lãi suất đang bằng 0%, vì vậy khoản tiền gửi "
            "không phát sinh tiền lãi theo mô hình tính toán."
        )

    elif ty_le_lai > 0:
        st.write(
            f"Với mức lãi suất bạn nhập, khoản tiền gửi tạo ra "
            f"{tong_lai:,.0f} VNĐ tiền lãi theo các giả định "
            "của phép tính hiện tại."
        )

        if loai_lai == "Lãi kép":
            st.write(
                "Lãi kép có thể giúp tăng số tiền tích lũy "
                "khi lãi được giữ lại và tiếp tục ghép vào gốc. "
                "Kết quả phụ thuộc vào chu kỳ ghép lãi và thời gian gửi."
            )
        else:
            st.write(
                "Với lãi đơn, tiền lãi được tính dựa trên "
                "số tiền gốc ban đầu nên cách tính dễ theo dõi."
            )

    # Lưu ý quan trọng
    st.markdown("### ⚠️ 5. Lưu ý trước khi gửi tiết kiệm")

    st.caption(
        "Kết quả trên là số tiền ước tính theo thông tin bạn nhập "
        "và công thức của ứng dụng. Tiền lãi thực tế có thể khác "
        "do phương pháp tính lãi của ngân hàng, số ngày thực gửi, "
        "điều kiện nhận lãi, tái tục hoặc rút trước hạn. "
        "Bạn nên kiểm tra điều khoản của sản phẩm tiền gửi "
        "trước khi đưa ra quyết định."
    )
```


    # =========================
    # THÔNG TIN TÓM TẮT
    # =========================
    st.divider()
    st.subheader("📝 Thông tin khoản tiền gửi")

    st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Phương pháp:** {loai_lai}")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    # =========================
    # CÔNG THỨC
    # =========================
    st.divider()
    st.subheader("📐 Công thức sử dụng")

    if loai_lai == "Lãi đơn":
        st.latex(
            r"I = P \times r \times t"
        )
        st.caption(
            "Trong đó: I là tiền lãi, P là tiền gốc, "
            "r là lãi suất năm, t là số năm."
        )

    else:
        st.latex(
            r"A = P(1+r)^n"
        )
        st.caption(
            "Trong đó: A là tổng tiền nhận được, P là tiền gốc, "
            "r là lãi suất mỗi kỳ, n là số kỳ ghép lãi."
        )
