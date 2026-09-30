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
st.title("💰 TÍNH LÃI TIỀN GỬI TIẾT KIỆM")
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
