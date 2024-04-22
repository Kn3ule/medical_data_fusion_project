# medical_data_fusion_project
 
## Verwendung

Um dieses Projekt auf Ihrem lokalen System zu verwenden, befolgen Sie bitte die folgenden Schritte:

### 1. Repository klonen

Klonen Sie dieses Repository auf Ihren lokalen Computer:

```bash
git clone ...
cd projectname
```

### 2. Datenordner hinzufügen

Ordner mit den Daten (ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3) im Projekt ablegen

### 3. Virtual Environment (Venv) erstellen

Erstellen Sie eine virtuelle Umgebung (Venv), um die Pakete isoliert von anderen Projekten zu installieren:

```bash
python -m venv venv
#venv aktivieren
#windows
venv\Scripts\activate
#mac
source venv/bin/activate
```

### 5. Erforderliche Pakete installieren

Installieren Sie die erforderlichen Python-Pakete aus der `requirements.txt`-Datei:

```bash
pip install -r requirements.txt
```

### 6. Postgres Datenbank erstellen und mit Daten füllen

Um die Metadaten und die SCP_Statements in eine relationale Datenbank zu speichern, müssen folgende Schritte erledigt werden:

- PostgreSQL installieren und Datenbank initiieren
- .env File im Projekt anlegen und folgende env-variable erstellen:
```python
 POSTGRES_URL="postgresql://username:password@host:port/dbname"
```
- database.py ausführen um Tables zu erstellen
- copy csv-files to tables (Header True, Seperater ,) (ptbxl_database.csv -> metadata, scp_satements.csv -> scpstatements)





