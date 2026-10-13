import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dữ liệu & Xử lý
data = {
    'Họ tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [9.0, 8.0, 7.0, 10.0, 8.0, 6.0, 9.0, 7.0, 8.0, 9.0],
    'Giữa kỳ': [8.0, 7.0, 6.0, 9.0, 7.0, 5.0, 8.0, 6.0, 7.0, 8.0],
    'Cuối kỳ': [8.5, 9.0, 6.5, 8.0, 6.0, 7.0, 8.5, 7.0, 7.5, 8.5]
}
df = pd.DataFrame(data)
df['Tong_ket'] = df['Chuyên cần'] * 0.2 + df['Giữa kỳ'] * 0.3 + df['Cuối kỳ'] * 0.5

def xep_loai(score):
    if score >= 8.5: return 'Giỏi'
    elif score >= 7.0: return 'Khá'
    elif score >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 2. Tiêu đề Web App
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 3. Hiển thị bảng điểm
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df)

# 4. Hiển thị thống kê
st.subheader("Thống kê chung")
dtb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

st.write(f"- **Điểm trung bình của lớp:** {dtb_lop:.2f}")
st.write(f"- **Sinh viên có điểm tổng kết cao nhất:** {sv_max['Họ tên']} ({sv_max['Tong_ket']:.2f})")
st.write(f"- **Sinh viên có điểm tổng kết thấp nhất:** {sv_min['Họ tên']} ({sv_min['Tong_ket']:.2f})")
st.write(f"- **Số sinh viên đạt (điểm tổng kết ≥ 5):** {so_sv_dat}")

# 5. Danh sách chọn sinh viên (Selectbox)
st.subheader("Thông tin chi tiết sinh viên")
selected_student = st.selectbox("Chọn một sinh viên:", df['Họ tên'])
sv_info = df[df['Họ tên'] == selected_student].iloc[0]

st.write(f"**Chuyên cần:** {sv_info['Chuyên cần']} | **Giữa kỳ:** {sv_info['Giữa kỳ']} | **Cuối kỳ:** {sv_info['Cuối kỳ']} | **Tổng kết:** {sv_info['Tong_ket']:.2f} | **Xếp loại:** {sv_info['Xep_loai']}")

# 6. Biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Họ tên'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Tên sinh viên')
ax.set_title('Điểm tổng kết của 10 sinh viên')
ax.set_xlim(0, 10)
ax.invert_yaxis()
st.pyplot(fig)

# 7. Thông tin người tạo 
st.markdown("---")
st.caption("Họ và tên: [Trần Hoàng Duy] - MSSV: [068208005300]") 
