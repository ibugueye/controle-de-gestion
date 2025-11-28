@echo off
setlocal

echo ============================================
echo       LANCEMENT APPLICATION PROJET GESTION
echo ============================================

if not exist python-embed (
    echo Téléchargement Python portable...
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.11.6/python-3.11.6-embed-amd64.zip -OutFile python-embed.zip"
    powershell -Command "Expand-Archive python-embed.zip -DestinationPath python-embed"
    del python-embed.zip
)

echo Installation de pip...
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://bootstrap.pypa.io/get-pip.py','get-pip.py')"
python-embed\\python.exe get-pip.py
del get-pip.py

echo Installation dependances...
python-embed\\python.exe -m pip install -r requirements.txt

echo Lancement de l'application Streamlit...
start "" python-embed\\python.exe -m streamlit run projet_gestion.py
pause
