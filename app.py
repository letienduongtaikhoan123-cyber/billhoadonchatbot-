import streamlit as st
from datetime import datetime
st.image("ảnh quán trà sữa.png")
# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Trà Sữa - Tính Hóa Đơn",
    page_icon="🧋",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

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

.chat-title {
    color: #d63384;
    font-size: 24px;
    font-weight: bold;
}

.chat-bot {
    background-color: #fff0f6;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #ffb3d1;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ẢNH QUÁN
# =========================================================

try:
    st.image(
        "ảnh quán trà sữa.png",
        use_container_width=True
    )
except:
    st.warning("⚠️ Không tìm thấy file ảnh quán trà sữa.")


# =========================================================
# MENU TRÀ SỮA
# =========================================================

tra_sua = {

    # Trà sữa
    "Trà sữa truyền thống": 30000,
    "Trà sữa socola": 32000,
    "Trà sữa matcha": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa dâu": 32000,
    "Trà sữa bạc hà": 32000,
    "Trà sữa caramel": 35000,
    "Trà sữa cookies": 38000,
    "Trà sữa oreo": 38000,
    "Trà sữa hạt dẻ": 38000,
    "Trà sữa vani": 32000,
    "Trà sữa cà phê": 35000,
    "Trà sữa phô mai": 38000,
    "Trà sữa việt quất": 35000,
    "Trà sữa xoài": 35000,

    # Trà trái cây
    "Trà đào": 30000,
    "Trà vải": 30000,
    "Trà chanh": 25000,
    "Trà dâu": 30000,
    "Trà xoài": 32000,
    "Trà tắc": 25000,
    "Trà kiwi": 35000,
    "Trà chanh dây": 32000,
    "Trà nhiệt đới": 35000,
    "Trà dưa lưới": 35000
}


# =========================================================
# TOPPING
# =========================================================

topping_price = {

    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Trân châu hoàng kim": 6000,
    "Trân châu phô mai": 7000,
    "Trân châu đường đen": 7000,

    "Thạch trái cây": 5000,
    "Thạch dừa": 5000,
    "Thạch nha đam": 5000,
    "Thạch cà phê": 5000,
    "Thạch phô mai": 7000,
    "Thạch thủy tinh": 6000,

    "Pudding trứng": 7000,
    "Pudding socola": 7000,

    "Kem cheese": 10000,
    "Kem tươi": 8000,

    "Oreo": 7000,
    "Cookie": 7000,
    "Hạt thủy tinh": 6000
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
# MỨC ĐỘ ĐƯỜNG
# =========================================================

muc_duong = [
    "0% - Không đường",
    "10% - Siêu ít ngọt",
    "20% - Rất ít ngọt",
    "30% - Ít ngọt",
    "50% - Ngọt vừa",
    "70% - Ngọt",
    "80% - Khá ngọt",
    "100% - Ngọt nhiều",
    "120% - Siêu ngọt"
]


# =========================================================
# MỨC ĐỘ ĐÁ
# =========================================================

muc_da = [
    "Không đá",
    "10% đá",
    "20% đá",
    "30% đá",
    "50% đá",
    "70% đá",
    "100% đá"
]


# =========================================================
# MÓN ĂN
# =========================================================

mon_them = {

    # Bánh
    "Bánh flan": 10000,
    "Bánh tiramisu": 15000,
    "Bánh cá": 12000,
    "Bánh su kem": 12000,
    "Bánh chocolate": 18000,
    "Bánh matcha": 18000,
    "Bánh bông lan": 15000,

    # Đồ ăn
    "Khoai tây chiên": 20000,
    "Khoai lang chiên": 20000,
    "Xúc xích": 15000,
    "Cá viên chiên": 20000,
    "Bò viên chiên": 20000,
    "Gà viên chiên": 22000,
    "Phô mai que": 22000,
    "Mực viên chiên": 25000,
    "Nem chua rán": 25000,

    # Món khác
    "Sandwich": 20000,
    "Bánh mì": 18000,
    "Hot dog": 25000,
    "Hamburger": 30000,
    "Gà rán": 30000,
    "Combo khoai + xúc xích": 30000
}


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown(
    '<div class="main-title">🧋 QUÁN TRÀ SỮA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Tính hóa đơn nhanh chóng - Chính xác - Tiện lợi'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# CHATBOT
# =========================================================

st.sidebar.markdown(
    '<div class="chat-title">🤖 TRỢ LÝ TRÀ SỮA</div>',
    unsafe_allow_html=True
)

st.sidebar.write(
    "Xin chào! 👋 Mình có thể giúp bạn xem menu, "
    "giá món và gợi ý đồ uống."
)

# Lưu lịch sử chatbot
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


cau_hoi = st.sidebar.text_input(
    "💬 Bạn muốn hỏi gì?",
    placeholder="Ví dụ: Có những topping nào?"
)


def chatbot_tra_loi(cau_hoi):

    q = cau_hoi.lower().strip()

    # -----------------------------
    # CHÀO HỎI
    # -----------------------------

    if any(x in q for x in [
        "xin chào",
        "chào",
        "hello",
        "hi"
    ]):

        return (
            "Xin chào! 👋🧋 "
            "Mình là trợ lý của quán. "
            "Bạn có thể hỏi mình về trà sữa, "
            "topping, món ăn hoặc giá tiền nhé!"
        )


    # -----------------------------
    # MENU TRÀ SỮA
    # -----------------------------

    if (
        "menu" in q
        or "trà sữa" in q
        or "đồ uống" in q
    ):

        danh_sach = "\n".join(
            [
                f"• {mon}: {gia:,}đ"
                for mon, gia in tra_sua.items()
            ]
        )

        return (
            "🧋 **MENU ĐỒ UỐNG:**\n\n"
            + danh_sach
        )


    # -----------------------------
    # TOPPING
    # -----------------------------

    if "topping" in q:

        danh_sach = "\n".join(
            [
                f"• {mon}: +{gia:,}đ"
                for mon, gia in topping_price.items()
            ]
        )

        return (
            "🧋 **TOPPING:**\n\n"
            + danh_sach
        )


    # -----------------------------
    # MÓN ĂN
    # -----------------------------

    if (
        "món ăn" in q
        or "đồ ăn" in q
        or "bánh" in q
        or "ăn gì" in q
    ):

        danh_sach = "\n".join(
            [
                f"• {mon}: {gia:,}đ"
                for mon, gia in mon_them.items()
            ]
        )

        return (
            "🍰 **MÓN ĂN:**\n\n"
            + danh_sach
        )


    # -----------------------------
    # GIÁ
    # -----------------------------

    for mon, gia in tra_sua.items():

        if mon.lower() in q:

            return (
                f"🧋 {mon} có giá "
                f"**{gia:,} VNĐ/ly**."
            )


    for mon, gia in mon_them.items():

        if mon.lower() in q:

            return (
                f"🍰 {mon} có giá "
                f"**{gia:,} VNĐ**."
            )


    # -----------------------------
    # SIZE
    # -----------------------------

    if "size" in q:

        return (
            "🥤 Quán có 3 size:\n\n"
            "• M: Giá gốc\n"
            "• L: +5.000đ\n"
            "• XL: +10.000đ"
        )


    # -----------------------------
    # ĐƯỜNG
    # -----------------------------

    if (
        "đường" in q
        or "ngọt" in q
    ):

        return (
            "🍯 Quán có nhiều mức đường:\n\n"
            "• 0%: Không đường\n"
            "• 10%: Siêu ít ngọt\n"
            "• 20%: Rất ít ngọt\n"
            "• 30%: Ít ngọt\n"
            "• 50%: Ngọt vừa\n"
            "• 70%: Ngọt\n"
            "• 80%: Khá ngọt\n"
            "• 100%: Ngọt nhiều\n"
            "• 120%: Siêu ngọt"
        )


    # -----------------------------
    # ĐÁ
    # -----------------------------

    if "đá" in q:

        return (
            "🧊 Bạn có thể chọn:\n\n"
            "• Không đá\n"
            "• 10%\n"
            "• 20%\n"
            "• 30%\n"
            "• 50%\n"
            "• 70%\n"
            "• 100%"
        )


    # -----------------------------
    # GỢI Ý
    # -----------------------------

    if (
        "gợi ý" in q
        or "nên uống" in q
        or "tư vấn" in q
        or "recommend" in q
    ):

        return (
            "💖 Một số lựa chọn bạn có thể thử:\n\n"
            "🧋 Trà sữa matcha + trân châu trắng\n"
            "🍫 Trà sữa socola + pudding\n"
            "🍓 Trà sữa dâu + thạch trái cây\n"
            "🥭 Trà xoài + trân châu hoàng kim\n"
            "🧀 Trà sữa truyền thống + kem cheese\n\n"
            "Nếu thích ít ngọt, bạn có thể chọn "
            "30% hoặc 50% đường."
        )


    # -----------------------------
    # ÍT NGỌT
    # -----------------------------

    if (
        "ít ngọt" in q
        or "ít đường" in q
    ):

        return (
            "🍯 Nếu bạn thích ít ngọt, "
            "mình gợi ý mức **30% đường**.\n\n"
            "Nếu muốn thanh nhẹ hơn, hãy chọn "
            "**20% hoặc 10% đường**."
        )


    # -----------------------------
    # SIÊU NGỌT
    # -----------------------------

    if (
        "ngọt nhiều" in q
        or "rất ngọt" in q
        or "siêu ngọt" in q
    ):

        return (
            "🍯 Quán có mức **100%** và "
            "**120% đường** dành cho bạn thích vị ngọt đậm."
        )


    # -----------------------------
    # CẢM ƠN
    # -----------------------------

    if (
        "cảm ơn" in q
        or "thanks" in q
    ):

        return (
            "🥰 Không có gì! "
            "Chúc bạn có một ly trà sữa thật ngon! 🧋❤️"
        )


    # -----------------------------
    # TRẢ LỜI MẶC ĐỊNH
    # -----------------------------

    return (
        "🤖 Mình chưa hiểu câu hỏi này.\n\n"
        "Bạn có thể hỏi:\n"
        "• Menu trà sữa\n"
        "• Giá topping\n"
        "• Món ăn\n"
        "• Mức độ đường\n"
        "• Mức độ đá\n"
        "• Size ly\n"
        "• Gợi ý món"
    )


if cau_hoi:

    tra_loi = chatbot_tra_loi(cau_hoi)

    st.sidebar.markdown(
        f"""
        <div class="chat-bot">
        🤖 <b>Trợ lý:</b><br><br>
        {tra_loi.replace(chr(10), '<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.session_state.chat_history.append(
        {
            "cau_hoi": cau_hoi,
            "tra_loi": tra_loi
        }
    )


# =========================================================
# THÔNG TIN KHÁCH HÀNG
# =========================================================

st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)


# =========================================================
# CHỌN TRÀ SỮA
# =========================================================

st.header("🧋 Chọn trà sữa")

col1, col2 = st.columns(2)


with col1:

    loai_tra = st.selectbox(
        "Loại trà sữa / trà trái cây",
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
        "🍯 Mức độ đường",
        options=muc_duong,
        value="50% - Ngọt vừa"
    )

    da = st.select_slider(
        "🧊 Mức độ đá",
        options=muc_da,
        value="50% đá"
    )

    toppings = st.multiselect(
        "🧋 Chọn topping",
        list(topping_price.keys())
    )


# =========================================================
# TÍNH TIỀN TRÀ SỮA
# =========================================================

gia_ly = tra_sua[loai_tra]

gia_size = size_price[size]

gia_topping = sum(
    topping_price[t]
    for t in toppings
)

gia_mot_ly = (
    gia_ly
    + gia_size
    + gia_topping
)

thanh_tien_tra = (
    gia_mot_ly
    * so_luong
)


# =========================================================
# MÓN ĂN
# =========================================================

st.header("🍰 Món ăn / đồ uống thêm")

co_mon_them = st.checkbox(
    "Tôi muốn gọi thêm món"
)

mon_da_chon = []

so_luong_mon_them = 1

thanh_tien_mon_them = 0


if co_mon_them:

    col3, col4 = st.columns(2)

    with col3:

        mon_da_chon = st.multiselect(
            "🍟 Chọn món ăn",
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

    thanh_tien_mon_them = sum(
        mon_them[mon]
        for mon in mon_da_chon
    ) * so_luong_mon_them


# =========================================================
# TỔNG TIỀN
# =========================================================

tong_tien = (
    thanh_tien_tra
    + thanh_tien_mon_them
)


# =========================================================
# THÔNG TIN ĐƠN HÀNG
# =========================================================

st.divider()

st.header("🧾 Thông tin đơn hàng")

col5, col6 = st.columns([2, 1])


with col5:

    st.write(
        f"**Khách hàng:** "
        f"{ten_khach if ten_khach else 'Chưa nhập tên'}"
    )

    st.write(
        f"**Trà:** {loai_tra}"
    )

    st.write(
        f"**Số lượng:** {so_luong} ly"
    )

    st.write(
        f"**Size:** {size}"
    )

    st.write(
        f"**Đường:** {duong}"
    )

    st.write(
        f"**Đá:** {da}"
    )

    if toppings:

        st.write(
            "**Topping:** "
            + ", ".join(toppings)
        )

    else:

        st.write(
            "**Topping:** Không có"
        )

    if co_mon_them and mon_da_chon:

        st.write(
            "**Món thêm:** "
            + ", ".join(mon_da_chon)
            + f" × {so_luong_mon_them}"
        )

    else:

        st.write(
            "**Món thêm:** Không có"
        )


with col6:

    st.markdown(
        f"""
        <div class="total-box">

            <div>
                TỔNG THANH TOÁN
            </div>

            <div class="total-price">
                {tong_tien:,.0f} VNĐ
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# THANH TOÁN
# =========================================================

st.divider()

if st.button(
    "💳 THANH TOÁN",
    use_container_width=True,
    type="primary"
):

    if not ten_khach.strip():

        st.warning(
            "⚠️ Vui lòng nhập tên khách hàng."
        )

    elif co_mon_them and not mon_da_chon:

        st.warning(
            "⚠️ Bạn đã chọn thêm món "
            "nhưng chưa chọn món."
        )

    else:

        st.session_state["da_thanh_toan"] = True

        st.session_state["thoi_gian"] = (
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        st.success(
            "✅ Thanh toán thành công!"
        )


# =========================================================
# HÓA ĐƠN
# =========================================================

if st.session_state.get(
    "da_thanh_toan",
    False
):

    st.divider()

    st.success(
        "✅ Thanh toán thành công!"
    )

    thoi_gian = st.session_state.get(
        "thoi_gian",
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    )


    st.markdown(
        f"""
        <div class="invoice">

            <div class="invoice-title">
                🧋 HÓA ĐƠN THANH TOÁN
            </div>

            <hr>

            <p>
                <b>Khách hàng:</b> {ten_khach}
            </p>

            <p>
                <b>Thời gian:</b> {thoi_gian}
            </p>

            <hr>

            <h4>🧋 ĐỒ UỐNG</h4>

            <p>
                <b>{loai_tra}</b>
            </p>

            <p>
                Số lượng: {so_luong} ly
            </p>

            <p>
                Size: {size}
            </p>

            <p>
                Đường: {duong}
            </p>

            <p>
                Đá: {da}
            </p>

            <p>
                Topping:
                {", ".join(toppings)
                if toppings else "Không có"}
            </p>

            <p>
                Thành tiền:
                <b>{thanh_tien_tra:,.0f} VNĐ</b>
            </p>

            <hr>

            <h4>🍰 MÓN ĂN</h4>

            <p>
                {
                    ", ".join(mon_da_chon)
                    + f" × {so_luong_mon_them}"
                    if mon_da_chon
                    else "Không có"
                }
            </p>

            <p>
                Thành tiền món ăn:
                <b>
                    {thanh_tien_mon_them:,.0f} VNĐ
                </b>
            </p>

            <hr>

            <h2 style="
                text-align:right;
                color:#d63384;
            ">
                Tổng cộng:
                {tong_tien:,.0f} VNĐ
            </h2>

            <p style="
                text-align:center;
                font-size:18px;
            ">
                ❤️ Cảm ơn quý khách!
                Hẹn gặp lại ❤️
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # FILE HÓA ĐƠN
    # =====================================================

    hoa_don_text = f"""
========================================
             QUÁN TRÀ SỮA
              HÓA ĐƠN
========================================

Khách hàng: {ten_khach}
Thời gian: {thoi_gian}

----------------------------------------
ĐỒ UỐNG
----------------------------------------

Tên món: {loai_tra}
Số lượng: {so_luong}
Size: {size}
Đường: {duong}
Đá: {da}

Topping:
{", ".join(toppings) if toppings else "Không có"}

Thành tiền:
{thanh_tien_tra:,.0f} VNĐ

----------------------------------------
MÓN ĂN
----------------------------------------

{
    ", ".join(mon_da_chon)
    + f" x {so_luong_mon_them}"
    if mon_da_chon
    else "Không có"
}

Thành tiền:
{thanh_tien_mon_them:,.0f} VNĐ

----------------------------------------
TỔNG THANH TOÁN
----------------------------------------

{tong_tien:,.0f} VNĐ

========================================

          CẢM ƠN QUÝ KHÁCH!

========================================
"""


    ten_file = (
        ten_khach.strip()
        .replace(" ", "_")
        if ten_khach.strip()
        else "khach_hang"
    )


    st.download_button(
        label="📥 TẢI HÓA ĐƠN",
        data=hoa_don_text,
        file_name=f"hoa_don_{ten_file}.txt",
        mime="text/plain",
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#888;
        padding:15px;
    ">
        🧋 <b>QUÁN TRÀ SỮA</b><br>
        Ngon mỗi ngày • Phục vụ tận tâm ❤️
    </div>
    """,
    unsafe_allow_html=True
)
