import streamlit as st
from datetime import datetime

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Trà Sữa - Tính Hóa Đơn",
    page_icon="🧋",
    layout="wide"
)

# =========================
# CSS GIAO DIỆN
# =========================
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #d63384;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #777;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .total-box {
        background-color: #fff0f6;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #ffb3d1;
    }

    .total-price {
        color: #d63384;
        font-size: 32px;
        font-weight: bold;
    }

    .invoice {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border: 2px dashed #d63384;
    }

    .invoice-title {
        text-align: center;
        color: #d63384;
        font-size: 28px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# =========================
# DỮ LIỆU MENU
# =========================

tra_sua = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa socola": 32000,
    "Trà sữa matcha": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa dâu": 32000,
    "Trà sữa bạc hà": 32000,
    "Trà đào": 30000,
    "Trà vải": 30000,
    "Trà chanh": 25000
}

topping_price = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Thạch phô mai": 7000,
    "Kem cheese": 10000
}

size_price = {
    "M": 0,
    "L": 5000,
    "XL": 10000
}

mon_them = {
    "Bánh flan": 10000,
    "Bánh tiramisu": 15000,
    "Khoai tây chiên": 20000,
    "Xúc xích": 15000,
    "Bánh cá": 12000
}


# =========================
# TIÊU ĐỀ
# =========================

st.markdown(
    '<div class="main-title">🧋 QUÁN TRÀ SỮA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Tính hóa đơn nhanh chóng - Chính xác - Tiện lợi</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================

st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)


# =========================
# CHỌN MÓN
# =========================

st.header("🧋 Chọn trà sữa")

col1, col2 = st.columns(2)

with col1:
    loai_tra = st.selectbox(
        "Loại trà sữa",
        list(tra_sua.keys())
    )

    so_luong = st.number_input(
        "Số lượng",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

    size = st.selectbox(
        "Size ly",
        list(size_price.keys())
    )

with col2:
    duong = st.select_slider(
        "Mức độ đường",
        options=["0%", "30%", "50%", "70%", "100%"],
        value="50%"
    )

    da = st.select_slider(
        "Mức độ đá",
        options=["Không đá", "30%", "50%", "70%", "100%"],
        value="50%"
    )

    toppings = st.multiselect(
        "Chọn topping",
        list(topping_price.keys())
    )


# =========================
# TÍNH TIỀN TRÀ SỮA
# =========================

gia_ly = tra_sua[loai_tra]
gia_size = size_price[size]
gia_topping = sum(topping_price[t] for t in toppings)

gia_mot_ly = gia_ly + gia_size + gia_topping
thanh_tien_tra = gia_mot_ly * so_luong


# =========================
# MÓN THÊM
# =========================

st.header("🍰 Món ăn / đồ uống thêm")

co_mon_them = st.checkbox("Tôi muốn gọi thêm món")

mon_da_chon = []
so_luong_mon_them = 1
thanh_tien_mon_them = 0

if co_mon_them:
    col3, col4 = st.columns(2)

    with col3:
        mon_them_chon = st.multiselect(
            "Chọn món thêm",
            list(mon_them.keys())
        )

    with col4:
        so_luong_mon_them = st.number_input(
            "Số lượng món thêm",
            min_value=1,
            max_value=20,
            value=1,
            step=1
        )

    mon_da_chon = mon_them_chon

    thanh_tien_mon_them = sum(
        mon_them[mon] for mon in mon_da_chon
    ) * so_luong_mon_them


# =========================
# TỔNG TIỀN
# =========================

tong_tien = thanh_tien_tra + thanh_tien_mon_them


st.divider()

st.header("🧾 Thông tin đơn hàng")

col5, col6 = st.columns([2, 1])

with col5:
    st.write(f"**Khách hàng:** {ten_khach if ten_khach else 'Chưa nhập tên'}")
    st.write(f"**Trà sữa:** {loai_tra}")
    st.write(f"**Số lượng:** {so_luong} ly")
    st.write(f"**Size:** {size}")
    st.write(f"**Đường:** {duong}")
    st.write(f"**Đá:** {da}")

    if toppings:
        st.write("**Topping:** " + ", ".join(toppings))
    else:
        st.write("**Topping:** Không có")

    if co_mon_them and mon_da_chon:
        st.write(
            "**Món thêm:** "
            + ", ".join(mon_da_chon)
            + f" × {so_luong_mon_them}"
        )
    else:
        st.write("**Món thêm:** Không có")

with col6:
    st.markdown(
        f"""
        <div class="total-box">
            <div>TỔNG THANH TOÁN</div>
            <div class="total-price">
                {tong_tien:,.0f} VNĐ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# NÚT THANH TOÁN
# =========================

st.divider()

if st.button(
    "💳 THANH TOÁN",
    use_container_width=True,
    type="primary"
):

    if not ten_khach.strip():
        st.warning("⚠️ Vui lòng nhập tên khách hàng trước khi thanh toán.")

    elif co_mon_them and not mon_da_chon:
        st.warning("⚠️ Bạn đã chọn thêm món nhưng chưa chọn món.")

    else:
        st.session_state["da_thanh_toan"] = True


# =========================
# HIỂN THỊ HÓA ĐƠN
# =========================

if st.session_state.get("da_thanh_toan", False):

    st.divider()

    st.success("✅ Thanh toán thành công!")

    thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    st.markdown(
        f"""
        <div class="invoice">

        <div class="invoice-title">
            🧋 HÓA ĐƠN THANH TOÁN
        </div>

        <hr>

        <p><b>Khách hàng:</b> {ten_khach}</p>
        <p><b>Thời gian:</b> {thoi_gian}</p>

        <hr>

        <h4>🧋 Trà sữa</h4>

        <p>
        {loai_tra} - Size {size} -
        {so_luong} ly
        </p>

        <p>
        Đường: {duong} | Đá: {da}
        </p>

        <p>
        Topping:
        {", ".join(toppings) if toppings else "Không có"}
        </p>

        <p>
        Thành tiền trà sữa:
        <b>{thanh_tien_tra:,.0f} VNĐ</b>
        </p>

        <hr>

        <h4>🍰 Món thêm</h4>

        <p>
        {
            ", ".join(mon_da_chon) + f" × {so_luong_mon_them}"
            if mon_da_chon
            else "Không có"
        }
        </p>

        <p>
        Thành tiền món thêm:
        <b>{thanh_tien_mon_them:,.0f} VNĐ</b>
        </p>

        <hr>

        <h2 style="text-align:right; color:#d63384;">
            Tổng cộng: {tong_tien:,.0f} VNĐ
        </h2>

        <p style="text-align:center;">
            ❤️ Cảm ơn quý khách! Hẹn gặp lại ❤️
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # TẢI HÓA ĐƠN
    # =========================

    hoa_don_text = f"""
========================================
          QUÁN TRÀ SỮA
           HÓA ĐƠN
========================================

Khách hàng: {ten_khach}
Thời gian: {thoi_gian}

----------------------------------------
TRÀ SỮA
----------------------------------------
Tên món: {loai_tra}
Số lượng: {so_luong}
Size: {size}
Đường: {duong}
Đá: {da}

Topping:
{", ".join(toppings) if toppings else "Không có"}

Thành tiền: {thanh_tien_tra:,.0f} VNĐ

----------------------------------------
MÓN THÊM
----------------------------------------
{
    ", ".join(mon_da_chon) + f" x {so_luong_mon_them}"
    if mon_da_chon
    else "Không có"
}

Thành tiền món thêm:
{thanh_tien_mon_them:,.0f} VNĐ

----------------------------------------
TỔNG THANH TOÁN:
{tong_tien:,.0f} VNĐ
----------------------------------------

       CẢM ƠN QUÝ KHÁCH!
========================================
"""

    st.download_button(
        label="📥 Tải hóa đơn",
        data=hoa_don_text,
        file_name=f"hoa_don_{ten_khach}.txt",
        mime="text/plain",
        use_container_width=True
    )
