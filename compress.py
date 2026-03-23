import joblib
print("กำลังบีบอัดไฟล์ AI...")
data = joblib.load('ai_detective_super_pack.pkl')
joblib.dump(data, 'ai_detective_super_pack.pkl', compress=3)
print("บีบอัดเสร็จเรียบร้อย! พร้อมส่งขึ้นฟ้าครับ")