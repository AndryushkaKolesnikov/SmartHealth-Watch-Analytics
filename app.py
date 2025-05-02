import pandas as pd
import streamlit as st
import seaborn as sns
from catboost import CatBoostRegressor

# Настройка страницы
st.set_page_config(
    page_title="SmartHealth-Watch-Analytics",
    page_icon="📊",
    layout="wide"
)

# Заголовок
st.title("📊 SmartHealth-Watch-Analytics")
st.markdown("### Прогнозирование частоты сердечных сокращений на основе данных смарт-часов")

# Пути к данным и модели
PATH_DATA = "data/clean_smartwatch_health_data.csv"
PATH_MODEL = "data/my_model.cbm"

@st.cache_data
def load_data(path):
    """Загрузка данных из файла"""
    data = pd.read_csv(path)
    # Для демонстрации берем случайную выборку
    data = data.sample(5000, random_state=42)
    return data

@st.cache_data
def load_model(path):
    """Загрузка модели из файла"""
    model = CatBoostRegressor()
    model.load_model(path)
    return model

# Загрузка данных
df = load_data(PATH_DATA)

# Разделение на две колонки
col1, col2 = st.columns([2, 1])

# Отображение графиков в первой колонке
with col1:
    st.subheader("Визуализация данных")
    st.write("Парные графики для анализа взаимосвязей между параметрами:")
    
    # Создание парного графика
    plot = sns.pairplot(df)
    st.pyplot(plot.fig)

# Ввод данных и результаты во второй колонке
with col2:
    st.subheader("Настройки прогноза")
    st.write("Выберите параметры для прогнозирования частоты сердечных сокращений:")

    # Боковая панель для ввода данных
    activity_level = st.selectbox(
        "Уровень активности", 
        options=df['Activity Level'].unique(),
        help="Выберите уровень физической активности."
    )
    stress_level = st.selectbox(
        "Уровень стресса", 
        options=df['Stress Level'].unique(),
        help="Выберите уровень стресса."
    )
    step_count = st.slider(
        "Количество шагов", 
        min_value=int(min(df['Step Count'])), 
        max_value=int(max(df['Step Count'])),
        value=int(df['Step Count'].mean()),
        help="Укажите количество шагов за день."
    )
    blood_oxygen_level = st.slider(
        "Уровень кислорода в крови (%)", 
        min_value=int(min(df['Blood Oxygen Level (%)'])), 
        max_value=int(max(df['Blood Oxygen Level (%)'])),
        value=int(df['Blood Oxygen Level (%)'].mean()),
        help="Укажите уровень кислорода в крови."
    )
    sleep_duration_hours = st.slider(
        "Продолжительность сна (часы)", 
        min_value=float(min(df['Sleep Duration (hours)'])), 
        max_value=float(max(df['Sleep Duration (hours)'])),
        value=float(df['Sleep Duration (hours)'].mean()),
        step=0.1,
        help="Укажите продолжительность сна в часах."
    )

    # Формирование данных для прогноза
    dict_data = {
        "Blood Oxygen Level (%)": blood_oxygen_level,
        "Step Count": step_count,
        "Sleep Duration (hours)": sleep_duration_hours,
        "Activity Level": activity_level,
        "Stress Level": stress_level
    }
    data_predict = pd.DataFrame([dict_data])

    # Кнопка для прогноза
    button = st.button("🚀 Сделать прогноз", use_container_width=True)

    if button:
        # Загрузка модели
        model = load_model(PATH_MODEL)
        
        # Прогноз
        output = model.predict(data_predict)
        st.success(f"Прогнозируемая частота сердечных сокращений: **{round(output[0], 7)} BPM** 🫀")

    # Дополнительная информация
    st.markdown("---")
    st.markdown("""
    #### Описание приложения:
    - Это веб-приложение использует данные смарт-часов для прогнозирования частоты сердечных сокращений.
    - Модель обучена на исторических данных и учитывает такие параметры, как уровень активности, уровень стресса, количество шагов, уровень кислорода в крови и продолжительность сна.
    - Вы можете настроить параметры в правой части экрана и нажать кнопку "Сделать прогноз", чтобы получить результат.
    """)

# Стиль для кнопки
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    height: 3em;
}
div.stButton > button:hover {
    background-color: #45A049;
}
</style>
""", unsafe_allow_html=True)