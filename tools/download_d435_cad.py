"""Download only the official D435 SolidWorks model; local file is gitignored."""
from pathlib import Path
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

URL = "https://dev.realsenseai.com/download/41950"
output = Path(__file__).resolve().parents[1] / "models/local/D435_Solid.SLDPRT"
with urlopen(URL, timeout=60) as response:
    archive = response.read()
with ZipFile(BytesIO(archive)) as bundle:
    data = bundle.read("D435_Solid.SLDPRT")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_bytes(data)
print(output)
