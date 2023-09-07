sudo apt install python3 python3-pip -y
python3 -m venv v
. v/bin/activate
pip install -r requirements.txt
sudo apt-get install -y tesseract-ocr-rus
python run.py
