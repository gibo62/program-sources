from urllib.parse import unquote
import re
filename = "record_2026-03-08_10-23-03.mkv"
# Decodifica dei caratteri URL (es. %3A → :)
decoded = unquote(filename)
# Regex per estrarre data e ora
pattern = r"record_(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2}-\d{2})\.mkv"
match = re.match(pattern, decoded)
if match:
    data = match.group(1)
    ora = match.group(2)
    print("Data:", data)
    print("Ora:", ora)
else:
    print("Formato non riconosciuto")
