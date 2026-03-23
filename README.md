# ⚖️ Homicide Offender Profiling & Solvability Assessment System (HOPSAS)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

An advanced, 6-dimensional profiling and assessment system designed to simulate the statistical analysis of crime scene data. Utilizing Machine Learning, this system evaluates the probability of case scenarios and potential suspect profiles based on historical homicide reports.

## 🌟 Key Features
The system processes victim demographics and crime scene details to predict 6 distinct dimensions:
* 👤 **Sex:** Estimates the likely sex of the perpetrator.
* 🎂 **Age Group:** Categorizes the likely age group (Juvenile, Adult, Elderly).
* 🌍 **Race:** Predicts the most probable race of the suspect.
* 🐺 **Operation Type:** Analyzes whether the crime was likely committed by a single individual (Lone Wolf) or multiple perpetrators (Group).
* 🔗 **Relationship:** Assesses the probable relationship between the perpetrator and the victim.
* 🎯 **Solvability Index:** Calculates the percentage of probability that a case with these characteristics will be solved.

## 🛠️ Tech Stack
* **Frontend / UI:** Streamlit
* **Machine Learning:** scikit-learn (RandomForestClassifier)
* **Data Processing:** Pandas, NumPy
* **Model Serialization:** Joblib

## 🚀 Local Setup & Installation

1. Clone this repository to your local machine:
```bash
git clone [https://github.com/suriyen-creator/ai-profiler.git](https://github.com/suriyen-creator/ai-profiler.git)
cd ai-profiler
Install the required dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py
⚠️ Disclaimer
This project was created strictly for educational purposes and learning in the fields of Data Science and Machine Learning. The outputs are purely statistical probability estimates (trained on historical FBI Homicide Data) and cannot be used as legal evidence, in real-world criminal investigations, or for actual personal identification.

thai ver.

# ⚖️ Homicide Offender Profiling & Solvability Assessment System (HOPSAS)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

ระบบประเมินและวิเคราะห์โปรไฟล์ผู้ก่อเหตุ (Ultimate AI Profiler 6-in-1) พัฒนาขึ้นเพื่อจำลองการวิเคราะห์ข้อมูลเชิงสถิติจากฐานข้อมูลอาชญากรรม โดยใช้ Machine Learning ในการประเมินความน่าจะเป็นของรูปคดีและผู้ต้องสงสัย

## 🌟 ฟีเจอร์หลัก (Key Features)
ระบบประมวลผลข้อมูลจากลักษณะเหยื่อและสถานที่เกิดเหตุ เพื่อทำนายผลลัพธ์ 6 มิติ:
* 👤 **เพศ (Sex):** ประเมินเพศของผู้ต้องสงสัย
* 🎂 **ช่วงอายุ (Age Group):** ประเมินกลุ่มอายุ (วัยรุ่น, วัยผู้ใหญ่, ผู้สูงอายุ)
* 🌍 **เชื้อชาติ (Race):** ประเมินเชื้อชาติที่มีความเป็นไปได้สูงสุด
* 🐺 **รูปแบบการลงมือ (Operation):** วิเคราะห์ว่าลงมือคนเดียว (Lone Wolf) หรือเป็นกลุ่ม (Group)
* 🔗 **ความสัมพันธ์ (Relationship):** ประเมินความสัมพันธ์ระหว่างคนร้ายและเหยื่อ
* 🎯 **ดัชนีโอกาสปิดคดี (Solvability Index):** คำนวณเปอร์เซ็นต์ความน่าจะเป็นที่คดีลักษณะนี้จะถูกคลี่คลาย

## 🛠️ เทคโนโลยีที่ใช้ (Tech Stack)
* **Frontend / UI:** Streamlit
* **Machine Learning:** scikit-learn (RandomForestClassifier)
* **Data Processing:** Pandas, NumPy
* **Model Serialization:** Joblib

## 🚀 วิธีการติดตั้งและรันโปรแกรม (Local Setup)

1. Clone repository นี้ลงเครื่อง:
```bash
git clone [https://github.com/suriyen-creator/ai-profiler.git](https://github.com/suriyen-creator/ai-profiler.git)
cd ai-profiler

ติดตั้งไลบรารีที่จำเป็น:

Bash
pip install -r requirements.txt
รันแอปพลิเคชัน:

Bash
streamlit run app.py
⚠️ ข้อสงวนสิทธิ์ (Disclaimer)
โปรเจกต์นี้สร้างขึ้นเพื่อการศึกษาและการเรียนรู้ด้าน Data Science และ Machine Learning เท่านั้น ข้อมูลที่ได้เป็นเพียงการประเมินความน่าจะเป็นทางสถิติ (อ้างอิงจาก FBI Homicide Data) ไม่สามารถนำไปใช้เป็นหลักฐานทางกฎหมาย การสืบสวนจริง หรือการระบุตัวตนบุคคลได้
