# Saucedemo Automation Test (BDD)

## 1. Yêu cầu:
- Python 3.x
- ChromeDriver cài đặt đúng phiên bản phù hợp với Chrome
- Thư viện: Selenium, Behave

## 2. Hướng dẫn cài đặt:
- Cài Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Cài pip:
bash
python -m ensurepip --upgrade

- Cài các thư viện:
bash
pip install -r requirements.txt
Trong file `requirements.txt` cần có:
selenium
behave


## 3. Cách chạy:
- Mở Terminal hoặc Command Prompt
- Truy cập đến thư mục gốc của dự án (chứa folder `features`)
- Chạy lệnh:
bash
behave features/test_saucedemo.feature


## 4. Ghi chú:
- Đảm bảo `chromedriver.exe` đã được thêm vào PATH hoặc để chung thư mục chạy.
- Có thể tải ChromeDriver tại: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- Khi hoàn thành, hãy push project lên private GitHub repo và mời reviewer theo yêu cầu.
- Ảnh chụp màn hình sẽ được lưu dưới tên `checkout_complete.png` khi hoàn tất đơn hàng.
#   s a u c e d e m o _ a u t o m a t i o n _ t e s t 
 
 
