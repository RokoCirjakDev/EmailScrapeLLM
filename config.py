config = {
    "LOCAL": True,  # varijabla koja određuje hoće li se koristiti lokalni model ili Gemini API
    "UKLJUCI_CSV": True,  # koristi CSV datoteku za ODER podatke
    "UKLJUCI_EMAIL": True,  # koristi email folder za parsanje emailova
    "UKLJUCI_DOC": True,  # koristi doc folder za parsanje dokumenata
    "PITAJ_APLIKACIJU_DOC": True, # pita na koju aplikaciju se odnosi dokument (Ako je True, APLIKACIJA će biti None)
    "PITAJ_APLIKACIJU_EMAIL": True,  # pita na koju aplikaciju se odnosi email (Ako je True, APLIKACIJA će biti None)
    "FAST_MODE": True  # Gasi thinking na qwen3
}