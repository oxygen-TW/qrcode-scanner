# qrcode-scanner

## Usage:
```
usage: qrcode-scanner.exe [-h] [-c] [-i IMAGE] [-b]

optional arguments:
  -h, --help            show this help message and exit
  -c, --clipboard       Decode QR code image from clipboard
  -i IMAGE, --image IMAGE
                        Decode QR code from image
  -b, --copyback        If you want copy decode text to clipboard.
  ```

## Build:
```
pip install poetry
poetry shell
poetry install
pyinstaller -F -c app.py
```