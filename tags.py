librairies = [
    "sqlite3",
    "Jupyter",
    "Pandas",
    "Numpy",
    "Matplotlib",
    "Flask",
    "math",
    "json",
    "scikit-learn",
    "h5py",
    "tqdm",
    "opencv-python",
    "mail-parser",
    "beautifulsoup4",
    "pyotp",
    "mailbox",
    "pdfkit",
    "python-dotenv",
    "python-dateutil",
    "pytz",
    "moviepy",
    "speechrecognition",
    "pydub",
    "ffmpeg",
    "chardet",
    "codecs",
    "PIL",
    "qrcode",
    "pyzbar",
    "pypdf2",
    "pymupdf",
    "tabulate",
    "python-nmap",
    "netifaces",
    "psutil",
    "socket",
    "ipaddress",
    "openalpr",
    "argparse",
    "cv2",
    "shutil",
    "collections",
    "itertools",
    "pyautogui",
    "click"
]

librairies_embarque = [
    "pyserial",
    "smbus",
    "machine",
    "pico_i2c_lcd",
    "lcd_api",
    "framebuf",
    "adafruit_hid",
    "board",
    "digitalio",
    "usb_hid",
    "sense-hat"
]



string = '<div style="text-align: center; margin-top: 20px;">'
for librairie in librairies:
    string += f"""<span style="background-color: #007BFF; color: #fff; padding: 4px 8px; margin: 2px; border-radius: 4px;">{librairie}</span>&nbsp;"""
string += '</div>'
print(string)

string2 = '<div style="text-align: center; margin-top: 20px;">'
for librairie in librairies_embarque:
    string2 += f"""<span style="background-color: #007BFF; color: #fff; padding: 4px 8px; margin: 2px; border-radius: 4px;">{librairie}</span>&nbsp;"""
string2 += '</div>'
print(string2)