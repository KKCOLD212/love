import streamlit as st

# Настройка страницы (вкладка в браузере)
st.set_page_config(page_title="Для самой особенной", page_icon="💖", layout="centered")

# Кастомный CSS для создания милого розового фона и стилизации текста/кнопок
st.markdown("""
    <style>
    /* Розовый фон для всего приложения */
    .stApp {
        background-color: #FFF0F5; /* LavenderBlush (нежно-розовый) */
    }
    
    /* Стилизация контейнера с текстом */
    .text-container {
        text-align: center;
        padding: 50px 20px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    .title-text {
        color: #D87093;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    
    .compliment-text {
        color: #C71585;
        font-size: 32px;
        font-weight: bold;
        min-height: 100px;
        animation: fadeIn 1s;
    }
    
    /* Анимация плавного появления текста */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    
    /* Стилизация кнопки-сердечка */
    div.stButton > button {
        background-color: #FF69B4;
        color: white;
        font-size: 40px;
        border-radius: 50%;
        width: 80px;
        height: 80px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.4);
        transition: all 0.3s ease;
        display: block;
        margin: 0 auto;
    }
    
    div.stButton > button:hover {
        background-color: #FF1493;
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(255, 20, 147, 0.6);
    }
    
    div.stButton > button:active {
        transform: scale(0.95);
    }
    </style>
""", unsafe_allow_html=True)

# Список всех надписей по порядку
phrases = [
    "Привет, а ты знала что...",
    "Ты 10/10 потому что очень красивая",
    "Ты 20/10 потому что очень милая",
    "Ты 30/10 потому что очень добрая",
    "Ты 40/10 потому что ты харизматичная",
    "Ты 50/10 потому что ты честная",
    "Ты 60/10 потому что с тобой комфортно общаться",
    "Ты 70/10 потому что очаровательная",
    "Ты 80/10 потому что ты искреняя",
    "Ты 90/10 потому что ты улыбчивая",
    "Ты 100/10 потому что ты невероятная",
    "Ты 1000000/10"
]

# Инициализация индекса текущей фразы в памяти приложения (session state)
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Функция для переключения на следующую фразу
def next_phrase():
    if st.session_state.current_index < len(phrases) - 1:
        st.session_state.current_index += 1
    else:
        # Начать заново, если дошли до конца (или можно убрать эту строчку, чтобы зафиксировать финал)
        st.session_state.current_index = 0

current_text = phrases[st.session_state.current_index]

# Отображение контента
st.markdown('<div class="text-container">', unsafe_allow_html=True)

# Если это первая фраза, делаем её как заголовок, для остальных — как комплимент
if st.session_state.current_index == 0:
    st.markdown(f'<div class="title-text">{current_text}</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="compliment-text">{current_text}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Кнопка со стрелочкой/сердечком
# Streamlit не всегда идеально отображает эмодзи внутри стилей кнопок на всех ОС,
# поэтому передаем сердечко прямо в аргумент label.
st.button("❤️", on_click=next_phrase)
