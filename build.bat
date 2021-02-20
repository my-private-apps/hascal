@ECHO OFF
cls
python --version
echo =====================
pip -v
echo =====================
Installing pyinstaller
pip install pyinstaller
echo =====================
Building
pyinstaller --noconfirm --onefile --console --name "hascal"  "src/hascal.py"
