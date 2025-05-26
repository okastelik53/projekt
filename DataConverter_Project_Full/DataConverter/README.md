# Data Converter

Program do konwersji danych pomiędzy formatami: `.json`, `.xml`, `.yaml`.

## 📦 Sposób użycia

```bash
project.exe inputFile outputFile
```

Gdzie:
- `inputFile` to ścieżka do pliku źródłowego (.json, .xml, .yml, .yaml),
- `outputFile` to ścieżka do pliku wynikowego (.json, .xml, .yml, .yaml).

## 💻 Wersja z GUI

Plik `ui_app.py` uruchamia prosty interfejs graficzny (GUI) do wyboru pliku wejściowego.

### Uruchomienie GUI:
```bash
python ui_app.py
```

### Utworzenie .exe z GUI (bez konsoli):
```bash
pyinstaller --onefile --noconsole ui_app.py
```

---

## ✅ Zadania projektowe (TaskX)

| Task  | Opis |
|-------|------|
| Task0 | Skrypt `installResources.ps1` instalujący zależności |
| Task1 | Parsowanie argumentów wejściowych |
| Task2 | Wczytywanie i walidacja pliku .json |
| Task3 | Zapis danych do pliku .json |
| Task4 | Wczytywanie i walidacja pliku .yml |
| Task5 | Zapis danych do pliku .yml |
| Task6 | Wczytywanie i walidacja pliku .xml |
| Task7 | Zapis danych do pliku .xml |
| Task8 | Utworzenie wersji z GUI (PyQt5) |
| Task9 | Asynchroniczne operacje w GUI (multithreading) |

---

## ⚙️ GitHub Actions

Plik `.github/workflows/build.yml` zawiera:
- nazwę workflow: `Build EXE`,
- harmonogram (automatyczne uruchomienie raz w tygodniu),
- trigger po pushu na `master`,
- uruchamianie ręczne (`workflow_dispatch`),
- domyślny serwer `windows-latest`,
- instalacja zależności ze skryptu `installResources.ps1`,
- komenda budująca `.exe`,
- upload wygenerowanego `.exe` jako artifact (`actions/upload-artifact@v3`).

---

## 📦 Instalacja zależności

Plik `installResources.ps1` zawiera:
```powershell
pip install pyinstaller
pip install pyyaml
pip install PyQt5
```

---

## 🔗 Dokumentacja GitHub Actions

[https://docs.github.com/en/actions](https://docs.github.com/en/actions)
