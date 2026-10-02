import streamlit as st
from datetime import datetime
from urllib.parse import quote
import requests
from io import BytesIO


# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Quán Trà Sữa Dương dễ thương",
    page_icon="🧋",
    layout="wide"
)


# =========================================================
# THÔNG TIN THANH TOÁN
# =========================================================

BANK_NAME = "VPBank"
BANK_BIN = "970432"
SO_TAI_KHOAN = "0947451914"
TEN_CHU_TAI_KHOAN = "LE TIEN DUONG"


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #fff7fb;
}

h1 {
    color: #e91e63;
    text-align: center;
}

h2 {
    color: #d81b60;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    background-color: #e91e63;
    color: white;
    font-weight: bold;
    border: none;
    padding: 10px;
}

.stButton > button:hover {
    background-color: #c2185b;
    color: white;
}

.bill {
    background-color: #fff;
    border: 2px solid #f48fb1;
    border-radius: 15px;
    padding: 20px;
}

.total {
    color: #e91e63;
    font-size: 26px;
    font-weight: bold;
}

.chat-box {
    background-color: #fff0f6;
    border-radius: 12px;
    padding: 12px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TIÊU ĐỀ + ẢNH
# =========================================================

st.title("🧋 QUÁN TRÀ SỮA")
st.markdown(
    "<h3 style='text-align:center;'>🌸 Thơm ngon - Đậm vị - Giá hợp lý 🌸</h3>",
    unsafe_allow_html=True
)

try:
    st.image("ảnh quán trà sữa.png", use_container_width=True)
except:
    st.info("💡 Hãy đặt file 'ảnh quán trà sữa.png' cùng thư mục với app.py")


# =========================================================
# MENU TRÀ SỮA
# =========================================================

tra_sua = {
    "Trà sữa truyền thống": 25000,
    "Trà sữa trân châu": 28000,
    "Trà sữa matcha": 30000,
    "Trà sữa chocolate": 30000,
    "Trà sữa khoai môn": 30000,
    "Trà sữa dâu": 30000,
    "Trà sữa bạc hà": 30000,
    "Trà sữa caramel": 32000,
    "Trà sữa cookie": 32000,
    "Trà sữa Oreo": 32000,
    "Trà sữa hazelnut": 33000,
    "Trà sữa vanilla": 30000,
    "Trà sữa cà phê": 32000,
    "Trà sữa phô mai": 35000,
    "Trà sữa việt quất": 32000,
    "Trà sữa xoài": 32000,
    "Trà đào": 28000,
    "Trà vải": 28000,
    "Trà dâu": 28000,
    "Trà xoài": 28000,
    "Trà chanh": 22000,
    "Trà tắc": 22000,
    "Trà đào cam sả": 30000,
    "Trà vải hoa hồng": 30000,
    "Trà dâu cam": 30000
}


# =========================================================
# TOPPING
# =========================================================

topping_price = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Trân châu vàng": 5000,
    "Trân châu đường đen": 6000,
    "Thạch trái cây": 5000,
    "Thạch dừa": 5000,
    "Thạch nha đam": 5000,
    "Thạch cà phê": 5000,
    "Thạch phô mai": 6000,
    "Thạch thủy tinh": 6000,
    "Pudding trứng": 7000,
    "Pudding chocolate": 7000,
    "Kem cheese": 8000,
    "Kem tươi": 7000,
    "Oreo": 6000,
    "Cookie": 6000
}


# =========================================================
# SIZE
# =========================================================

size_price = {
    "M": 0,
    "L": 5000,
    "XL": 10000
}


# =========================================================
# MỨC ĐƯỜNG
# =========================================================

muc_duong = {
    "0% - Không đường": 0,
    "10% - Siêu ít ngọt": 10,
    "20% - Rất ít ngọt": 20,
    "30% - Ít ngọt": 30,
    "50% - Ngọt vừa": 50,
    "70% - Ngọt": 70,
    "80% - Khá ngọt": 80,
    "100% - Ngọt nhiều": 100,
    "120% - Siêu ngọt": 120
}


# =========================================================
# MỨC ĐÁ
# =========================================================

muc_da = {
    "0% - Không đá": 0,
    "10% - Rất ít đá": 10,
    "20% - Ít đá": 20,
    "30% - Hơi ít đá": 30,
    "50% - Đá vừa": 50,
    "70% - Nhiều đá": 70,
    "100% - Đầy đá": 100
}


# =========================================================
# MÓN ĂN THÊM
# =========================================================

mon_them = {
    "Bánh flan": 10000,
    "Tiramisu": 25000,
    "Bánh su kem": 15000,
    "Bánh chocolate": 20000,
    "Bánh matcha": 20000,
    "Bánh bông lan": 15000,
    "Khoai tây chiên": 20000,
    "Khoai lang chiên": 20000,
    "Xúc xích": 15000,
    "Cá viên": 15000,
    "Bò viên": 15000,
    "Gà viên": 15000,
    "Phô mai que": 20000,
    "Mực viên": 18000,
    "Nem chua rán": 20000,
    "Sandwich": 20000,
    "Bánh mì": 15000,
    "Hot dog": 25000,
    "Hamburger": 30000,
    "Gà rán": 30000,
    "Combo khoai + xúc xích": 30000
}


# =========================================================
# HÀM TẠO QR THANH TOÁN
# =========================================================

def tao_qr_url(so_tien, noi_dung):
    """
    Tạo đường dẫn VietQR.
    """

    noi_dung_ma_hoa = quote(noi_dung)
    ten_ma_hoa = quote(TEN_CHU_TAI_KHOAN)

    qr_url = (
        f"https://img.vietqr.io/image/"
        f"{BANK_BIN}-{SO_TAI_KHOAN}-compact2.png"
        f"?amount={so_tien}"
        f"&addInfo={noi_dung_ma_hoa}"
        f"&accountName={ten_ma_hoa}"
    )

    return qr_url


# =========================================================
# CHATBOT
# =========================================================

def chatbot_tra_loi(cau_hoi):

    cau_hoi = cau_hoi.lower().strip()

    if any(x in cau_hoi for x in ["xin chào", "hello", "hi", "chào"]):
        return (
            "👋 Xin chào! Mình là trợ lý của Quán Trà Sữa. "
            "Bạn có thể hỏi mình về menu, giá tiền, topping, "
            "mức đường, mức đá hoặc món ăn nhé!"
        )

    if "menu" in cau_hoi or "trà sữa" in cau_hoi:
        return (
            "🧋 Quán có rất nhiều loại như trà sữa truyền thống, "
            "matcha, chocolate, khoai môn, Oreo, cookie, caramel, "
            "trà đào, trà vải, trà xoài..."
        )

    if "topping" in cau_hoi:
        return (
            "🍡 Topping gồm trân châu đen, trân châu trắng, "
            "trân châu đường đen, thạch trái cây, thạch dừa, "
            "pudding, kem cheese, Oreo, cookie..."
        )

    if "giá" in cau_hoi:
        return (
            "💰 Giá trà sữa từ khoảng 22.000đ đến 35.000đ. "
            "Size L thêm 5.000đ, size XL thêm 10.000đ."
        )

    if "size" in cau_hoi:
        return (
            "🥤 Quán có 3 size:\n"
            "M: giá gốc\n"
            "L: +5.000đ\n"
            "XL: +10.000đ"
        )

    if "đường" in cau_hoi:
        return (
            "🍬 Bạn có thể chọn đường từ 0%, 10%, 20%, 30%, "
            "50%, 70%, 80%, 100% đến 120%."
        )

    if "đá" in cau_hoi:
        return (
            "🧊 Mức đá gồm 0%, 10%, 20%, 30%, 50%, 70% và 100%."
        )

    if "ít ngọt" in cau_hoi:
        return (
            "🍬 Nếu bạn thích ít ngọt, có thể chọn 20% hoặc 30% đường."
        )

    if "ngọt" in cau_hoi:
        return (
            "🍬 Nếu thích ngọt, bạn có thể chọn 70%, 80%, "
            "100% hoặc 120% đường."
        )

    if "món ăn" in cau_hoi or "đồ ăn" in cau_hoi:
        return (
            "🍟 Quán có khoai tây chiên, khoai lang chiên, "
            "xúc xích, cá viên, bò viên, gà viên, phô mai que, "
            "hamburger, hot dog, gà rán và nhiều món khác."
        )

    if "gợi ý" in cau_hoi or "nên uống" in cau_hoi:
        return (
            "⭐ Bạn có thể thử Trà sữa trân châu + pudding trứng "
            "với 50% đường và 50% đá."
        )

    if "cảm ơn" in cau_hoi or "thanks" in cau_hoi:
        return "🥰 Không có gì! Chúc bạn ngon miệng!"

    return (
        "🤖 Mình có thể giúp bạn về: menu, giá, topping, "
        "size, đường, đá và món ăn thêm."
    )


# =========================================================
# SIDEBAR - CHATBOT
# =========================================================

with st.sidebar:

    st.header("🤖 TRỢ LÝ QUÁN")

    cau_hoi = st.text_input(
        "Bạn muốn hỏi gì?",
        placeholder="Ví dụ: Quán có topping gì?"
    )

    if st.button("💬 Hỏi chatbot"):

        if cau_hoi:
            st.markdown(
                f"""
                <div class="chat-box">
                <b>👤 Bạn:</b><br>
                {cau_hoi}<br><br>
                <b>🤖 Trợ lý:</b><br>
                {chatbot_tra_loi(cau_hoi)}
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# KHU VỰC ĐẶT HÀNG
# =========================================================

st.header("🛒 ĐẶT MÓN")


ten_khach = st.text_input(
    "👤 Tên khách hàng",
    placeholder="Nhập tên khách hàng"
)


col1, col2 = st.columns(2)


with col1:

    st.subheader("🧋 Trà sữa")

    loai_tra_sua = st.selectbox(
        "Chọn loại trà sữa",
        list(tra_sua.keys())
    )

    so_luong = st.number_input(
        "Số lượng ly",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

    size = st.selectbox(
        "Chọn size",
        list(size_price.keys())
    )


with col2:

    st.subheader("🍬 Tùy chọn")

    duong_text = st.select_slider(
        "Mức độ đường",
        options=list(muc_duong.keys()),
        value="50% - Ngọt vừa"
    )

    da_text = st.select_slider(
        "Mức độ đá",
        options=list(muc_da.keys()),
        value="50% - Đá vừa"
    )

    toppings = st.multiselect(
        "🍡 Chọn topping",
        list(topping_price.keys())
    )


# =========================================================
# MÓN ĂN THÊM
# =========================================================

st.subheader("🍟 MÓN ĂN THÊM")

co_mon_them = st.checkbox("Có thêm món ăn")


mon_chon = None
so_luong_mon = 0

if co_mon_them:

    col3, col4 = st.columns(2)

    with col3:

        mon_chon = st.selectbox(
            "Chọn món",
            list(mon_them.keys())
        )

    with col4:

        so_luong_mon = st.number_input(
            "Số lượng món",
            min_value=1,
            max_value=20,
            value=1,
            step=1
        )


# =========================================================
# TÍNH TIỀN
# =========================================================

gia_tra = tra_sua[loai_tra_sua]
gia_size = size_price[size]

gia_topping = sum(
    topping_price[topping]
    for topping in toppings
)

gia_mon_them = 0

if co_mon_them and mon_chon:
    gia_mon_them = mon_them[mon_chon] * so_luong_mon


tong_tien = (
    (gia_tra + gia_size + gia_topping) * so_luong
    + gia_mon_them
)


# =========================================================
# HIỂN THỊ TẠM TÍNH
# =========================================================

st.markdown("---")

st.subheader("💰 TẠM TÍNH")

st.write(f"🧋 {loai_tra_sua}: {gia_tra:,}đ × {so_luong}")
st.write(f"📏 Size {size}: +{gia_size:,}đ/ly")

if toppings:
    st.write(
        "🍡 Topping: "
        + ", ".join(toppings)
        + f" (+{gia_topping:,}đ/ly)"
    )
else:
    st.write("🍡 Topping: Không")

if co_mon_them and mon_chon:
    st.write(
        f"🍟 {mon_chon}: "
        f"{mon_them[mon_chon]:,}đ × {so_luong_mon}"
    )

st.markdown(
    f"<div class='total'>💰 TỔNG: {tong_tien:,} VNĐ</div>",
    unsafe_allow_html=True
)


# =========================================================
# NÚT THANH TOÁN
# =========================================================

if "da_thanh_toan" not in st.session_state:
    st.session_state["da_thanh_toan"] = False


if st.button("💳 THANH TOÁN"):

    if not ten_khach.strip():

        st.warning("⚠️ Vui lòng nhập tên khách hàng!")

    else:

        st.session_state["da_thanh_toan"] = True

        st.session_state["thoi_gian"] = (
            datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )


# =========================================================
# BILL SAU KHI THANH TOÁN
# =========================================================

if st.session_state["da_thanh_toan"]:

    st.markdown("---")

    st.success("🎉 Thanh toán thành công! Hóa đơn của bạn:")

    col_bill, col_qr = st.columns([1.4, 1])

    # =====================================================
    # BILL
    # =====================================================

    with col_bill:

        st.markdown(
            "<div class='bill'>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2 style='text-align:center;'>🧾 HÓA ĐƠN</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center;'>🧋 QUÁN TRÀ SỮA 🧋</p>",
            unsafe_allow_html=True
        )

        st.write("👤 **Khách hàng:**", ten_khach)

        st.write("🧋 **Trà sữa:**", loai_tra_sua)

        st.write("🔢 **Số lượng:**", so_luong)

        st.write("📏 **Size:**", size)

        st.write("🍬 **Đường:**", duong_text)

        st.write("🧊 **Đá:**", da_text)

        if toppings:

            st.write(
                "🍡 **Topping:** "
                + ", ".join(toppings)
            )

        else:

            st.write("🍡 **Topping:** Không")

        if co_mon_them and mon_chon:

            st.write(
                f"🍟 **Món thêm:** {mon_chon} × {so_luong_mon}"
            )

        else:

            st.write("🍟 **Món thêm:** Không")

        st.markdown("---")

        st.markdown(
            f"<div class='total'>"
            f"💰 TỔNG THANH TOÁN: {tong_tien:,} VNĐ"
            f"</div>",
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.write("🏦 **Ngân hàng:** VPBank")

        st.write(
            f"💳 **Số tài khoản:** {SO_TAI_KHOAN}"
        )

        st.write(
            f"👤 **Chủ tài khoản:** {TEN_CHU_TAI_KHOAN}"
        )

        st.write(
            f"🕐 **Thời gian:** "
            f"{st.session_state['thoi_gian']}"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # =====================================================
    # QR THANH TOÁN
    # =====================================================

    with col_qr:

        st.markdown(
            "<h2 style='text-align:center;'>📱 QR THANH TOÁN</h2>",
            unsafe_allow_html=True
        )

        noi_dung_chuyen_khoan = (
            f"THANH TOAN {ten_khach}"
        )

        qr_url = tao_qr_url(
            tong_tien,
            noi_dung_chuyen_khoan
        )

        try:

            response = requests.get(
                qr_url,
                timeout=10
            )

            if response.status_code == 200:

                st.image(
                    BytesIO(response.content),
                    caption="📱 Quét mã để thanh toán",
                    use_container_width=True
                )

            else:

                st.error(
                    "Không thể tải mã QR. "
                    "Bạn có thể chuyển khoản thủ công."
                )

        except:

            st.warning(
                "⚠️ Không tải được QR. "
                "Vui lòng kiểm tra kết nối Internet."
            )

        st.info(
            f"""
💰 **Số tiền:** {tong_tien:,} VNĐ

🏦 **Ngân hàng:** VPBank

💳 **STK:** {SO_TAI_KHOAN}

👤 **Chủ TK:** {TEN_CHU_TAI_KHOAN}

📝 **Nội dung:** {noi_dung_chuyen_khoan}
"""
        )


    # =====================================================
    # NỘI DUNG HÓA ĐƠN
    # =====================================================

    noi_dung_bill = f"""
========================================
           QUÁN TRÀ SỮA
             HÓA ĐƠN
========================================

Khách hàng: {ten_khach}

Trà sữa: {loai_tra_sua}
Số lượng: {so_luong}
Size: {size}

Mức đường: {duong_text}
Mức đá: {da_text}

Topping:
{", ".join(toppings) if toppings else "Không"}

Món thêm:
{mon_chon if co_mon_them and mon_chon else "Không"}

Số lượng món thêm:
{so_luong_mon if co_mon_them and mon_chon else 0}

----------------------------------------

TỔNG THANH TOÁN:
{tong_tien:,} VNĐ

----------------------------------------

THÔNG TIN THANH TOÁN

Ngân hàng: VPBank
Số tài khoản: {SO_TAI_KHOAN}
Chủ tài khoản: {TEN_CHU_TAI_KHOAN}

Nội dung chuyển khoản:
{noi_dung_chuyen_khoan}

----------------------------------------

Thời gian:
{st.session_state["thoi_gian"]}

========================================
       CẢM ƠN QUÝ KHÁCH ❤️
========================================
"""


    # =====================================================
    # TẢI HÓA ĐƠN
    # =====================================================

    st.download_button(
        label="📥 TẢI HÓA ĐƠN",
        data=noi_dung_bill,
        file_name="hoa_don_tra_sua.txt",
        mime="text/plain"
    )


    # =====================================================
    # ĐƠN MỚI
    # =====================================================

    if st.button("🔄 TẠO ĐƠN MỚI"):

        st.session_state["da_thanh_toan"] = False
        st.rerun()
