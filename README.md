# Fourier Transform Audio Processing

โปรเจกต์นี้แสดงการใช้ Fourier Transform ในการประมวลผลสัญญาณเสียง โดยสร้างเสียงจากคลื่นไซน์และใช้ Low-pass Filter กรองความถี่สูงออก

## ไฟล์ในโปรเจกต์

### 1. `fourierTransform_1.py` - Audio Generation
โปรแกรมสร้างเสียงจากคลื่นไซน์หลายความถี่

**วิธีใช้:**
```bash
python fourierTransform_1.py
```

**ผลลัพธ์:**
- `original.wav` - เสียงต้นฉบับ
- `output_lowpass.wav` - เสียงหลังผ่าน low-pass filter

### 2. `fourierTransform_2.py` - Image FFT Processing
โปรแกรมประมวลผลภาพด้วย FFT

**คุณสมบัติ:**
- โหลดภาพจาก URL
- แสดง Magnitude Spectrum
- ใช้ Low-pass filter แบบวงกลม

**วิธีใช้:**
```bash
python fourierTransform_2.py
```

**ผลลัพธ์:** แสดงภาพ 3 แบบเปรียบเทียบ
1. ภาพต้นฉบับ
2. Magnitude Spectrum (แสดงความถี่ในภาพ)
3. ภาพหลัง Low-pass Filter (เบลอ)

### 3. `fourierTransform_3.py` - Advanced Audio Processing
โปรแกรมประมวลผลเสียงขั้นสูง

**วิธีใช้:**
```bash
python fourierTransform_3.py
```

### 4. `fourierTransforms_4.py` - Additional Features
โปรแกรมเพิ่มเติมสำหรับการประมวลผล FFT

**วิธีใช้:**
```bash
python fourierTransforms_4.py
```

## หลักการทำงาน

### Fourier Transform
การแปลงสัญญาณจาก Time Domain ไปเป็น Frequency Domain เพื่อวิเคราะห์ว่าสัญญาณประกอบด้วยความถี่อะไรบ้าง

**สำหรับเสียง:**
```python
spec = np.fft.rfft(sig)           # FFT
freqs = np.fft.rfftfreq(sig.size, 1/sr)
spec[freqs > cutoff] = 0          # ตัดความถี่สูง
filt = np.fft.irfft(spec, n=sig.size)  # Inverse FFT
```

**สำหรับภาพ:**
```python
f = np.fft.fft2(img_gray)         # 2D FFT
fshift = np.fft.fftshift(f)       # ย้ายศูนย์กลาง
# ใช้ mask กรอง
f_ishift = np.fft.ifftshift(fshift_masked)
img_filtered = np.fft.ifft2(f_ishift)  # Inverse FFT
```

### Low-pass Filter
กรองความถี่สูงออก เหลือแต่ความถี่ต่ำ

**ผลลัพธ์:**
- เสียง: ฟังดูทุ้มลง ไม่แหลม
- ภาพ: เบลอ สูญเสียรายละเอียด

## ความต้องการของระบบ

```bash
pip install numpy matplotlib pillow requests
```

## ตัวอย่างผลลัพธ์

### เสียง (fourierTransform_1.py)
- **original.wav**: เสียงต้นฉบับที่สร้างจากคลื่นไซน์หลายความถี่
- **output_lowpass.wav**: เสียงหลังผ่าน low-pass filter ที่ตัดความถี่สูงออก ฟังดูทุ้มและนุ่มนวลขึ้น

### ภาพ (fourierTransform_2.py)
- **ภาพต้นฉบับ**: ภาพชัดเจน
- **Magnitude Spectrum**: แสดงการกระจายความถี่ (จุดสว่างตรงกลาง = ความถี่ต่ำ)
- **ภาพหลัง Filter**: ภาพเบลอ เพราะความถี่สูง (ขอบ/รายละเอียด) ถูกตัดออก

## สรุป

โปรเจกต์นี้แสดงให้เห็นว่า Fourier Transform สามารถนำไปใช้กับ:
1. **การวิเคราะห์เสียง** - หาความถี่ที่ประกอบกันเป็นเสียง
2. **การกรองเสียง** - ตัดความถี่ที่ไม่ต้องการออก
3. **การประมวลผลภาพ** - เบลอภาพ, ลดสัญญาณรบกวน

เทคนิคนี้ใช้ในหลายสาขา เช่น วิศวกรรมเสียง, การประมวลผลภาพ, การสื่อสาร, และการบีบอัดข้อมูล (MP3, JPEG)
