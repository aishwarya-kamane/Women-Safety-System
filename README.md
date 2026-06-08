# 🛡️ Women Safety App

A desktop-based **Women Safety Application** built using **Python 3.x**, **Tkinter**, and **SQLite**.  
This app is designed to provide a **panic mode**, **voice-triggered emergency activation**, and **automatic location & alert notifications** to emergency contacts via **Email** and **SMS**.

---

## 📌 Features

✅ **Panic Button** – One-click emergency activation with visual blinking effect  
✅ **Voice Trigger** – Continuous microphone listening for a custom trigger phrase (e.g., "help me")  
✅ **Live Audio Waveform** – Real-time sound visualization near panic button  
✅ **Emergency Alerts** – Sends Email and SMS notifications to saved contacts  
✅ **Location Tracking** – Gets location from GPS or falls back to IP-based geolocation  
✅ **Contact Management** – Add, update, and delete emergency contacts  
✅ **Logs Management** – View, export (CSV), and clear past emergency events  
✅ **Customizable Settings** – Configure SMTP, SMS, and voice trigger phrase from UI  
✅ **Thread-Safe Design** – Background threads for listening, siren playback, and network requests  
✅ **SQLite Database** – Lightweight persistent storage with schema for contacts, events, and settings  
✅ **Configurable** – Stores settings in `config.json` and `.env` for secrets (Brevo SMTP, SMS API keys)

---

## 📂 Project Structure

```
women-safety/
├── database/
|   ├── schema.sql           # Database schema (contacts, events, settings)
│   └── db.py                # SQLite helpers (CRUD for contacts, logs, settings)
├── modules/
│   ├── emergency.py         # Handles panic mode, siren, and notifications
│   ├── gui_dashboard.py     # Main dashboard with panic button & log preview
│   ├── gui_logs.py          # Logs page (view/export/clear events)
│   ├── gui_settings.py      # Settings page (SMTP, voice, SMS, contacts)
│   ├── gui_theme.py         # Theme and color configuration
│   ├── location.py          # Fetches location (GPS or IP fallback)
│   ├── notifier.py          # Email (Brevo) & SMS (Fast2SMS) sender
│   └── voice_listener.py    # Continuous mic listener + waveform visualization
├── requirements.txt         # Required dependencies
├── config.json              # Configuration (trigger phrase, thresholds)
├── .env                     # API keys & SMTP credentials
└── main.py                  # WomenSafetyApp class (entry point)
```

---

## 🗄️ Database Schema

```sql
-- Contacts table (stores emergency contacts)
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    notes TEXT
);

-- Events table (logs all emergency triggers)
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    latitude TEXT,
    longitude TEXT,
    address TEXT,
    message TEXT,
    methods TEXT
);

-- Settings table (stores configuration like voice trigger word)
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT
);
```

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/bhavesh.gharat.kit/women-safety-app.git
cd women-safety-app
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables
Create a `.env` file in the root folder:
```env
BREVO_API_URL="https://api.brevo.com/v3/smtp/email"
BREVO_API_KEY=brevo-api-key
BREVO_SENDER_EMAIL=brevo-sender-email
FAST2SMS_API_URL=https://www.fast2sms.com/dev/bulkV2
FAST2SMS_API_KEY=fast2sms-api-key
```

### 5️⃣ Initialize Database
```bash
python -m database.db
```

---

## ▶️ Running the App

```bash
python main.py
```

- The main dashboard will launch.
- Click **Panic Button** or say the **trigger phrase** to activate emergency mode.
- The siren will play, alerts will be sent, and the event will be logged automatically.

---


## 📦 Requirements

The following Python libraries are used:

```
SpeechRecognition
pyaudio
requests
geocoder
pygame
sounddevice
soundfile
numpy
```

Install via:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

| Setting           | Location        | Description                               |
|------------------|---------------|-------------------------------------------|
| Trigger Phrase   | config.json   | Word/Phrase that activates panic mode     |
| SMTP & SMS Keys  | .env          | API keys for Brevo & Fast2SMS             |
| Contacts         | App UI        | Managed via GUI (stored in SQLite)        |
| Panic Auto-Stop  | emergency.py  | Default: 20 seconds, configurable         |

---

## 🧪 Testing & Debugging

- **Voice Listener:** Ensure mic permissions are granted and background noise is minimal.
- **Email Alerts:** Test with a valid Brevo account & SMTP credentials.
- **SMS Alerts:** Test with Fast2SMS API key (India-specific).
- **Logs:** Verify that every panic activation creates a new entry in the events table.

---

## 🚀 Future Enhancements

- ✅ Push notifications via WhatsApp API
- ✅ Automatic call to first contact on panic trigger
- ✅ Cloud sync for contacts and logs
- ✅ Multilingual UI

---

## 👨‍💻 Author

**Aishwarya Kamane**  
  

📧 **Email:** aishwaryakamane8@gmail.com  


---

<!-- ## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this project for personal or commercial use. -->
