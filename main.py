import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

EXCEL_FILE_PATH = 'farmers_data.xlsx'
WEBSITE_URL = 'http://127.0.0.1:5500/pmfby-demo/index.html'

FIELD_MAPPING = {
    'farmer_name': 'farmerName',
    'aadhaar_number': 'aadhaarNumber',
    'bank_account': 'bankAccountNumber',
    'state': 'stateSelection',
    'district': 'districtSelection',
    'crop_name': 'cropName'
}

def fill_form(driver, data):
    print(f"\n🧑 Filling form for: {data.get('farmer_name', 'N/A')}")
    for column, html_id in FIELD_MAPPING.items():
        try:
            value = str(data[column])
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, html_id))
            )

            if element.tag_name == "select":
                options = element.find_elements(By.TAG_NAME, "option")
                matched = False
                for option in options:
                    if option.text.strip().lower() == value.strip().lower():
                        option.click()
                        matched = True
                        print(f"✅ Selected '{value}' in dropdown '{html_id}'")
                        break
                if not matched:
                    print(f"⚠️ No matching option for '{value}' in dropdown '{html_id}'")
            else:
                element.clear()
                element.send_keys(value)
                print(f"✅ Filled '{html_id}' with '{value}'")

            time.sleep(0.3)
        except Exception as e:
            print(f"⚠️ Error with field '{html_id}': {e}")

    try:
        submit_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submitButton"))
        )
        submit_btn.click()
        time.sleep(1)

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"🔔 Alert: {alert.text}")
        alert.accept()
        print("✅ Alert accepted")

    except Exception as e:
        print(f"❌ Error submitting form: {e}")

def main():
    try:
        df = pd.read_excel(EXCEL_FILE_PATH)
        print(f"📄 Loaded {len(df)} rows from Excel")
    except Exception as e:
        print(f"❌ Could not read Excel: {e}")
        return

    if df.empty:
        print("❌ Excel file is empty")
        return

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    for index, row in df.iterrows():
        try:
            print(f"\n🔁 Processing row {index + 1} of {len(df)}")
            driver.get(WEBSITE_URL)
            time.sleep(1.5)
            fill_form(driver, row.to_dict())

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'farmerName'))
            )
        except Exception as e:
            print(f"❌ Error on row {index + 1}: {e}")
            continue

    driver.quit()
    print("\n✅ All records processed. Browser closed.")

if __name__ == "__main__":
    main()
