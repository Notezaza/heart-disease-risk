import streamlit as st
import matplotlib.pyplot as plt

# ฟังก์ชันคำนวณคะแนนความเสี่ยงโรคหลอดเลือดหัวใจ
def calculate_risk_score(age, gender, smoking, hypertension, waist_circumference, weight, height, exercise, family_history, blood_sugar, cholesterol, diet):
    score = 0

    # การคำนวณคะแนนตามพารามิเตอร์ที่กำหนด
    if age < 35:
        score += -3
    elif 35 <= age <= 39:
        score += -2
    elif 40 <= age <= 44:
        score += 0
    elif 45 <= age <= 49:
        score += 2
    elif 50 <= age <= 54:
        score += 4
    elif 55 <= age <= 59:
        score += 6
    elif 60 <= age <= 64:
        score += 8
    elif 65 <= age <= 69:
        score += 10
    elif age >= 70:
        score += 12

    if gender == "ชาย":
        score += 3

    if smoking:
        score += 2

    if hypertension:
        score += 3

    if cholesterol > 240:
        score += 4
    elif cholesterol > 200:
        score += 2

    if blood_sugar > 126:
        score += 4

    if (gender == "ชาย" and waist_circumference >= 90) or (gender == "หญิง" and waist_circumference >= 80):
        score += 4

    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        score += 3
    elif bmi > 30:
        score += 4

    if exercise == "ไม่ออกกำลังกาย":
        score += 3

    if family_history:
        score += 5

    if diet == "ทานอาหารที่มีไขมันสูง":
        score += 3
    elif diet == "ทานผักและผลไม้ไม่เพียงพอ":
        score += 2

    return score

# ฟังก์ชันตีความคะแนนความเสี่ยง
def interpret_risk(score):
    if score < 0:
        return "<1%", "คุณมีความเสี่ยงต่ำมาก ควรรักษาพฤติกรรมสุขภาพที่ดีต่อไป"
    elif 1 <= score <= 5:
        return "1%", "ความเสี่ยงอยู่ในระดับต่ำ ควรดูแลสุขภาพต่อไป"
    elif 6 <= score <= 8:
        return "2%", "คุณมีความเสี่ยงปานกลาง ควรปรึกษาแพทย์เกี่ยวกับสุขภาพ"
    elif 9 <= score <= 11:
        return "4%", "ความเสี่ยงค่อนข้างสูง ควรปรึกษาแพทย์และปรับพฤติกรรมสุขภาพ"
    elif 12 <= score <= 15:
        return "5-10%", "ความเสี่ยงสูง ควรพบแพทย์เพื่อการวินิจฉัยและการรักษา"
    else:
        return ">12%", "คุณมีความเสี่ยงสูงมาก ควรปรึกษาแพทย์ทันที"

# เริ่มสร้างหน้าเว็บด้วย Streamlit
st.title("แบบสอบถามประเมินความเสี่ยงโรคหลอดเลือดหัวใจ")

st.write("กรุณากรอกข้อมูลเพื่อประเมินความเสี่ยงของคุณ:")
age = st.number_input("อายุ (ปี)", min_value=1, max_value=120, step=1)
gender = st.selectbox("เพศ", ["ชาย", "หญิง"])
smoking = st.checkbox("คุณสูบบุหรี่หรือไม่?", value=False)
hypertension = st.checkbox("คุณมีความดันโลหิตสูงหรือไม่?", value=False)
waist_circumference = st.number_input("รอบเอว (ซม.)", min_value=50.0, step=0.1)
weight = st.number_input("น้ำหนัก (กก.)", min_value=30.0, step=0.1)
height = st.number_input("ส่วนสูง (ซม.)", min_value=100.0, step=0.1)
exercise = st.selectbox("คุณออกกำลังกายบ่อยแค่ไหน?", ["ออกกำลังกายปกติ", "ไม่ออกกำลังกาย"])
family_history = st.checkbox("คุณมีประวัติครอบครัวเป็นโรคหลอดเลือดหัวใจหรือไม่?", value=False)
blood_sugar = st.number_input("ระดับน้ำตาลในเลือด (mg/dL)", min_value=0, step=1)
cholesterol = st.number_input("ระดับคอเลสเตอรอล (mg/dL)", min_value=0, step=1)
diet = st.selectbox("คุณทานอาหารอย่างไร?", ["ทานอาหารที่มีไขมันสูง", "ทานผักและผลไม้ไม่เพียงพอ", "ทานอาหารสมดุล"])

if st.button("ประเมินความเสี่ยง"):
    score = calculate_risk_score(age, gender, smoking, hypertension, waist_circumference, weight, height, exercise, family_history, blood_sugar, cholesterol, diet)
    risk_percentage, advice = interpret_risk(score)
    st.write(f"คะแนนความเสี่ยงของคุณคือ: {score}")
    st.write(f"โอกาสเกิดโรคหลอดเลือดหัวใจใน 10 ปีข้างหน้าคือ: {risk_percentage}")
    st.write(f"คำแนะนำ: {advice}")
