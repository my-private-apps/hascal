@ECHO OFF
cd src
cls
python --version
echo =====================
pip --version
echo =====================
echo Installing pyinstaller
pip install pyinstaller
echo =====================
echo Building
pyinstaller --noconfirm --onefile --console --name "hascal"  "hascal.py"
