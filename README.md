# 🌾 PMFBY Form Automation using Python & Selenium

This project automates the **PM Fasal Bima Yojna (PMFBY)** farmer registration form using Excel data and Selenium. It reads farmer details from an Excel file and automatically fills out the registration form on a simulated website.

---

## 📸 Demo
![demo](docs/demo.gif) 
---

## ✅ Features

- 📄 Reads data from an Excel sheet
- 🤖 Auto-fills a PMFBY-like HTML form
- 🔁 Submits forms in a loop for multiple farmers
- 🧠 Handles `<select>` dropdowns with case-insensitive matching
- ⚠️ Handles alerts and errors gracefully
- 💻 Built-in demo website for safe testing

---

## 📁 Folder Structure

```
pmfby-form-automation/
├── main.py                     # Main automation script
├── farmers_data.xlsx           # Sample Excel file with farmer data
├── pmfby-demo/
│   ├── index.html              # Demo HTML form
│   ├── style.css               # Optional CSS styling
│   └── script.js               # JavaScript with form alert + reload
├── .gitignore
├── README.md
```

---

## 📦 Requirements

Install Python libraries:

```bash
pip install selenium pandas openpyxl webdriver-manager
```

> ✅ Make sure Chrome browser is installed  
> ✅ You must have Python 3.7+

---

## 🧪 Usage

### 1. 📊 Prepare Your Excel File

Create `farmers_data.xlsx` with columns:

| farmer_name   | aadhaar_number   | bank_account   | state           | district | crop_name |
|---------------|------------------|----------------|------------------|----------|-----------|
| Ramesh Yadav  | 123412341234     | 123456789012   | Chhattisgarh     | Raipur   | Rice      |
| Sita Verma    | 987654321098     | 456789012345   | Madhya Pradesh   | Durg     | Wheat     |

---

### 2. 🧪 Run the Demo Website

Use VS Code Live Server or Python HTTP server:

```bash
cd pmfby-demo
# If using Python 3.x
python -m http.server 5500
```

Then open:
```
http://127.0.0.1:5500/index.html
```

---

### 3. 🚀 Run Automation Script

From the project root folder:

```bash
python main.py
```

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 🧪 Selenium WebDriver
- 📊 Pandas
- 📄 Excel (.xlsx)
- 🌐 HTML/CSS/JS (for demo form)
- 🌍 Chrome & WebDriver Manager

---

## 💡 Customization

- Add more fields to the HTML and map them in `FIELD_MAPPING`
- Hook into real PMFBY website (⚠️ not recommended for unauthorized access)
- Use GitHub Actions + Headless Chrome for CI bots

---

## ⚠️ Legal Disclaimer

This project uses a **demo HTML form** that simulates the real PMFBY form. It does not access or automate the official PMFBY portal. Do not use this script on real government websites without permission.

---

## 👨‍💻 Author

**Manoj Kumar Sinha**  
🎓 B.Tech Student, CSVTU  
📫 [GitHub](https://github.com/mksinha01)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
