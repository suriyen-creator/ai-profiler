import streamlit as st
import pandas as pd
import joblib
import datetime

# ==========================================
# ⚙️ System Configuration
# ==========================================
st.set_page_config(page_title="Homicide Profiling System", page_icon="⚖️", layout="wide")

@st.cache_resource
def load_super_pack():
    try:
        return joblib.load('ai_detective_super_pack.pkl')
    except FileNotFoundError:
        st.error("System Error: 'ai_detective_super_pack.pkl' not found. Please verify the file directory.")
        st.stop()

super_pack = load_super_pack()
model_sex = super_pack['model_sex']
model_page = super_pack['model_page']
model_race = super_pack['model_race']
model_op = super_pack['model_op']
model_rel = super_pack['model_rel']
model_solved = super_pack['model_solved']
options = super_pack['input_options']

# ==========================================
# 🎨 User Interface - Professional Mode
# ==========================================
st.title("ระบบประเมินและวิเคราะห์โปรไฟล์ผู้ก่อเหตุ")
st.markdown("**Homicide Offender Profiling & Solvability Assessment System (HOPSAS)**")
st.markdown("---")

col1, col2 = st.columns([1, 2.5])

# ==========================================
# 📝 Left Panel: Case Input
# ==========================================
with col1:
    st.subheader("1. ข้อมูลเบื้องต้นของคดี (Case Details)")
    
    with st.container(border=True):
        case_id = st.text_input("รหัสคดี (Case ID)", value=f"CASE-{datetime.datetime.now().strftime('%Y%m%d-%H%M')}")
        
        st.markdown("**ข้อมูลผู้เสียชีวิต (Victim Demographics)**")
        victim_age = st.number_input("อายุ (Age)", min_value=0, max_value=100, value=30)
        victim_sex = st.selectbox("เพศ (Sex)", ['Male', 'Female', 'Unknown'])
        victim_race = st.selectbox("เชื้อชาติ (Race)", ['White', 'Black', 'Asian/Pacific Islander', 'Native American/Alaska Native', 'Unknown'])
        
        st.markdown("**ข้อมูลที่เกิดเหตุ (Scene & Modus Operandi)**")
        weapon = st.selectbox("อาวุธ (Weapon)", options['weapons'])
        state = st.selectbox("เขตพื้นที่ (State)", options['states'])
        month = st.selectbox("เดือนที่เกิดเหตุ (Month)", options['months'])
        
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_btn = st.button("ประมวลผลข้อมูล (Execute Analysis)", use_container_width=True, type="primary")

# ==========================================
# 📊 Right Panel: Assessment Results
# ==========================================
with col2:
    st.subheader("2. ผลการประเมินทางสถิติ (Statistical Assessment)")
    
    if analyze_btn:
        input_data = pd.DataFrame({
            'Victim Age': [victim_age], 'Victim Sex': [victim_sex], 'Victim Race': [victim_race],
            'Weapon': [weapon], 'State': [state], 'Month': [month]
        })
        
        with st.spinner('กำลังเทียบเคียงรูปแบบกับฐานข้อมูล FBI Homicide Data...'):
            # Predict Categories
            pred_sex = model_sex.predict(input_data)[0]
            pred_age = model_page.predict(input_data)[0]
            pred_race = model_race.predict(input_data)[0]
            pred_op = model_op.predict(input_data)[0]
            pred_rel = model_rel.predict(input_data)[0]
            
            # Extract Confidence Scores (Probabilities)
            conf_sex = max(model_sex.predict_proba(input_data)[0]) * 100
            conf_age = max(model_page.predict_proba(input_data)[0]) * 100
            conf_race = max(model_race.predict_proba(input_data)[0]) * 100
            conf_op = max(model_op.predict_proba(input_data)[0]) * 100
            conf_rel = max(model_rel.predict_proba(input_data)[0]) * 100
            prob_solved = model_solved.predict_proba(input_data)[0][1] * 100
        
        # Display Results in a Professional Grid
        st.markdown(f"**รายงานการวิเคราะห์สำหรับรหัสคดี:** `{case_id}` | **เวลาประมวลผล:** `{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")
        
        with st.container(border=True):
            st.markdown("#### A. โปรไฟล์ทางกายภาพ (Physical Attributes)")
            r1_c1, r1_c2, r1_c3 = st.columns(3)
            r1_c1.metric(label="เพศ (Sex)", value=pred_sex, delta=f"ความมั่นใจ {conf_sex:.1f}%", delta_color="normal")
            r1_c2.metric(label="ช่วงอายุ (Age Group)", value=pred_age.split(' ')[0], delta=f"ความมั่นใจ {conf_age:.1f}%", delta_color="normal")
            r1_c3.metric(label="เชื้อชาติ (Race)", value=pred_race, delta=f"ความมั่นใจ {conf_race:.1f}%", delta_color="normal")
            
        with st.container(border=True):
            st.markdown("#### B. รูปแบบอาชญากรรม (Crime Pattern)")
            r2_c1, r2_c2 = st.columns(2)
            r2_c1.metric(label="การปฏิบัติการ (Operation)", value=pred_op.split(' ')[0], delta=f"ความมั่นใจ {conf_op:.1f}%", delta_color="normal")
            r2_c2.metric(label="ความสัมพันธ์ (Relationship)", value=pred_rel.split(' ')[0], delta=f"ความมั่นใจ {conf_rel:.1f}%", delta_color="normal")
            
        with st.container(border=True):
            st.markdown("#### C. ดัชนีความน่าจะเป็นในการปิดคดี (Solvability Index)")
            st.progress(int(prob_solved))
            if prob_solved > 70:
                st.success(f"ระดับความเป็นไปได้: สูง ({prob_solved:.1f}%) - พบรูปแบบคดีลักษณะนี้ถูกคลี่คลายในสถิติอดีตจำนวนมาก")
            elif prob_solved > 40:
                st.warning(f"ระดับความเป็นไปได้: ปานกลาง ({prob_solved:.1f}%) - จำเป็นต้องอาศัยหลักฐานทางนิติวิทยาศาสตร์เพิ่มเติมอย่างมีนัยสำคัญ")
            else:
                st.error(f"ระดับความเป็นไปได้: ต่ำ ({prob_solved:.1f}%) - มีความเสี่ยงสูงที่จะกลายเป็นคดีที่ปิดไม่ได้ (Cold Case)")

        # AI Recommendations
        st.markdown("---")
        st.subheader("📌 ข้อเสนอแนะทางยุทธวิธี (Tactical Recommendations)")
        recs = []
        if 'Family' in pred_rel or 'Intimate' in pred_rel:
            recs.append("- **มุ่งเป้าการสอบสวน:** บุคคลในครอบครัว, คู่สมรส, หรืออดีตคนรัก ตรวจสอบประวัติการทำประกันชีวิต หรือความขัดแย้งในครัวเรือนในช่วง 6 เดือนที่ผ่านมา")
        elif 'Acquaintance' in pred_rel:
            recs.append("- **มุ่งเป้าการสอบสวน:** เพื่อนร่วมงาน, เพื่อนบ้าน, หรือคนที่มีประวัติการติดต่อกับผู้ตายใน 72 ชั่วโมงก่อนเกิดเหตุ ตรวจสอบการสื่อสารทางโทรศัพท์ (CDR)")
        elif 'Stranger' in pred_rel:
            recs.append("- **มุ่งเป้าการสอบสวน:** คดีนี้มีลักษณะการสุ่มเหยื่อ (Random/Stranger) ตรวจสอบกล้องวงจรปิด (CCTV) ในรัศมี 5 กิโลเมตร และแฟ้มคดีลักษณะใกล้เคียงในพื้นที่ (Serial Pattern)")
            
        if 'Group' in pred_op:
            recs.append("- **เฝ้าระวัง:** มีแนวโน้มสูงที่จะมีผู้ก่อเหตุมากกว่า 1 คน อาจเกี่ยวข้องกับองค์กรอาชญากรรม หรือคดียาเสพติด ควรประสานงานกับหน่วยปราบปรามพิเศษ")
            
        for rec in recs:
            st.markdown(rec)
            
    else:
        st.info("ระบบพร้อมทำงาน: กรุณากรอกข้อมูลพารามิเตอร์ทางซ้ายมือ และกด 'ประมวลผลข้อมูล'")