import streamlit as st

st.set_page_config(
    page_title="Chúc Mừng 20/10 💖",
    page_icon="💐",
    layout="centered"
)

css_20_10 = """
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f5 0%, #ffe4e1 100%);
}

#bg-effects {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: -1;
    overflow: hidden;
}

.float-item {
    position: absolute;
    bottom: -10%;
    color: rgba(255, 105, 180, 0.5);
    font-size: 26px;
    animation: floatUp 8s linear infinite;
}

.float-item:nth-child(1) { left: 10%; animation-duration: 7s; font-size: 22px; }
.float-item:nth-child(2) { left: 25%; animation-duration: 10s; font-size: 32px; animation-delay: 2s; }
.float-item:nth-child(3) { left: 40%; animation-duration: 6s; font-size: 20px; animation-delay: 1s; }
.float-item:nth-child(4) { left: 55%; animation-duration: 9s; font-size: 28px; animation-delay: 3s; }
.float-item:nth-child(5) { left: 70%; animation-duration: 8s; font-size: 24px; animation-delay: 1.5s; }
.float-item:nth-child(6) { left: 85%; animation-duration: 11s; font-size: 34px; animation-delay: 0.5s; }

@keyframes floatUp {
    0% { transform: translateY(0) rotate(0deg); opacity: 0; }
    20% { opacity: 0.8; }
    100% { transform: translateY(-120vh) rotate(360deg); opacity: 0; }
}
</style>

<div id="bg-effects">
    <div class="float-item">🌸</div>
    <div class="float-item">💖</div>
    <div class="float-item">💓</div>
    <div class="float-item">✨</div>
    <div class="float-item">🌷</div>
    <div class="float-item">💕</div>
</div>
"""

st.markdown(css_20_10, unsafe_allow_html=True)

st.title("💖 Chúc Mừng Ngày Phụ Nữ Việt Nam 20/10 💐")

st.markdown("""
### Gửi tới những người phụ nữ tuyệt vời nhất! ✨

Nhân ngày **20/10**, xin gửi những lời chúc tốt đẹp nhất đến hành tinh chữ S . 
Chúc chị em phụ nữ luôn luôn xinh đẹp, rạng rỡ, tràn ngập niềm vui và luôn được yêu thương trọn vẹn trong cuộc sống! 🌸

---
""")

with st.container():
    st.info("""
    💌 **Lời chúc ý nghĩa:**  
    *"Mong rằng mỗi ngày trôi qua đều mang đến cho chi em phụ nữ thật nhiều nụ cười, may mắn và hạnh phúc. mọi người
xứng đáng nhận được những điều tuyệt vời nhất!"*
    """)

if st.button("🎁 Bấm vào đây để nhận món quà bất ngờ!"):
    st.balloons()
    st.success("🎉 Chúc chị em phụ nữ có một ngày 20/10 ngập tràn hoa, quà và lời hay ý đẹp. Quan trọng nhất là có một bờ vai che trở cho tâm hồn dễ thương !")
    
