import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import os

# Check if the 'Products_info.csv' file exists
if os.path.exists('Products_info.csv'):
    # If the file exists, delete its contents
    with open('Products_info.csv', 'w', newline='', encoding='utf-8') as file:
        # Open the file in write mode to truncate its contents
        pass

# Create the CSV file if it doesn't exist
with open('Products_info.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Product ID', 'Device Subtitle', 'Device Title', 'Key Feature_1', 
                     'Key Feature_2', 'Key Feature_3', 'Key Feature_4', 'Key Feature_5', 'Key Feature_6', 'Key Feature_7',
                     'Product description', 'Device Type', 'Network Technology', 'LTE catagory support',
                     'Contact_Address', 'Contact_Phone', 'Contact_Email', 'Hardware_Antenna', 
                     'Hardware_Battery', 'Hardware_Display Resolution', 'Hardware_Ethernet Posts', 'Hardware_Sim Type', 
                     'Hardware_USB ports', 'Hardware_Voltage supply', 'Other_Accelerometer', 'Other_Z-Wave', 'Other_Audio',
                     'Other_Battery safety', 'Other_Bluetooth', 'Other_Camera', 'Other_Dual SIM', 'Other_E911', 'Other_eUICC', 
                     'Other_GNSS', 'Other_GPSS', 'Other_GPS', 'Other_Keyboard', 'Other_Magnetic card reader', 'Other_Printer', 'Other_RJ-11', 
                     'Other_Scanning tech', 'Other_Serial', 'Other_Smart card reader', 'Other_Voice transmission capable', 
                     'Other_Wifi', 'Other_Zigbee', 'FoTA For Baseband/Modem Software Update Capability', 'FoTA Client Type', 'Operating System', 
                     'Soft_Developer Kit', 'Soft_Diagnostics', 'Soft_Security Level', 'Soft_EMS', 'Soft_MMS', 'Soft_Remote Management', 
                     'Soft_SMS Capability', 'Soft_WEA', 'Soft_Persistent Prefix IPv6', 'Soft_Mobile Private Network', 
                     'Soft_FWA', 'Soft_Split Data Routing', 'Soft_Multi-APN', 'Soft_Global Capable', 'Soft_Private Wireless Network', 
                     'Chassis_Dimensions', 'Chassis_Weight', 'Chassis_Operating Temperature', 'Chassis_Storage Temperature', 
                     'Chassis_Relative Humidity', 'Chassis_Rain & dust resistance', 'Chassis_Vehicle Mounting', 
                     'Network_NAT', 'Network_Routing Protocols', 'Network_Security Protocol', 'Network_VPN Support', 'Network_Numbershare', 
                     'Network_Fax capable', 'Network_Firewall', 'Network_UMTS', 'Network_LTE', 'Network_LTE Global/Roaming', 
                     'Network_5G', 'Network_5G Global/Roaming', 'Network_GPRS', 'Network_GSM', 'Contact_Website', 'Contact_Address', 'Contact_Phone', 
                     'Contact_Email', 'Industry'])

with open('product_ids.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file) 
    for row in reader:
        product_id = row[0]
        url = f"https://opendevelopment.verizonwireless.com/device-showcase/device/{product_id}"
        product_number = [product_id]

        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully visited URL: {url}")
        else:
            print(f"Failed to visit URL: {url}")

        # initialize the Chrome driver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # head to product page
        driver.get(url)

        time.sleep(2)

        try:
            # Device Subtitle
            device_subtitle_element = driver.find_element(By.CSS_SELECTOR, ".details__content-subtitle a")
            device_subtitle = device_subtitle_element.text
            print(device_subtitle)

            # Device title
            device_title_element = driver.find_elements(By.CSS_SELECTOR, ".details__content-title")
            device_title = device_title_element[1].text
            print(device_title)

            # Key Features
            key_feature_elements = driver.find_elements(By.CLASS_NAME, "details__content-item")
            key_features = [feature.text for feature in key_feature_elements]

            # Pad the key_features list with empty strings if there are fewer than 6 features
            while len(key_features) < 7:
                key_features.append('')
            print(key_features)

            # Product description
            product_description_element = driver.find_element(By.CLASS_NAME, "details__content-copy")
            product_description = [product_description_element.text]
            print(product_description)

            # Overview
            overview_elements = driver.find_elements(By.CLASS_NAME, "definition-list-description")
            ## Device Type
            overview_device_type = [overview_elements[0].text] if len(overview_elements) > 0 else [""]
            print(overview_device_type)
            ## Network Technology
            overview_network_technology = [overview_elements[1].text] if len(overview_elements) > 1 else [""]
            print(overview_network_technology)
            ## LTE Category Support
            overview_category_support = [overview_elements[2].text] if len(overview_elements) > 2 else [""]
            print(overview_category_support)

            # Contact Manufacturer
            ## Sales
            contact_sales_elements = driver.find_elements(By.CSS_SELECTOR, ".details__image-content-copy-container p")
            contact_sales = [sales_element.text for sales_element in contact_sales_elements]
            print(contact_sales)
            ## Email
            contact_sales_email_element = driver.find_element(By.CSS_SELECTOR, ".details__image-content-copy-container a")
            contact_sales_email = [contact_sales_email_element.text]
            print(contact_sales_email)

            #Hardware Field Open
            hardware_main_click = driver.find_elements(By.CLASS_NAME, 'details__content-lower')[0].click()
            ## Hardware Field
            hardware_main_element = driver.find_element(By.CLASS_NAME, 'is-accordion-open')
            hardware_main = hardware_main_element.find_elements(By.CSS_SELECTOR, '.details__content-features--no-border p')
            hardware_main_antenna = [hardware_main[0].text]
            hardware_main_battery = [hardware_main[1].text]
            hardware_main_display = [hardware_main[2].text]
            hardware_main_ethernet = [hardware_main[3].text]
            hardware_main_sim = [hardware_main[4].text]
            hardware_main_usbports = [hardware_main[-2].text]
            hardware_main_voltage = [hardware_main[-1].text]
            print(hardware_main_antenna, hardware_main_battery, hardware_main_display, hardware_main_ethernet, hardware_main_sim, 
                  hardware_main_usbports, hardware_main_voltage)
            # Other features
            other_features = []
            other_elements = hardware_main_element.find_elements(By.CLASS_NAME, 'definition-list-description--right')
            for other_element in other_elements:
                other_features.append(other_element.text)
            print(other_features)

            # Software Field Open
            software_main_click = driver.find_elements(By.CLASS_NAME, 'details__content-lower')[1].click()
            ## Software Field
            software_main_element = driver.find_elements(By.CLASS_NAME, 'is-accordion-open')[1]
            software_main = software_main_element.find_elements(By.CSS_SELECTOR, '.details__content-features--no-border p')
            software_main_baseband = [software_main[0].text]
            software_main_clientType = [software_main[1].text] 
            software_main_system = [software_main[3].text]
            print(software_main_baseband, software_main_clientType, software_main_system)
            ### Software Features
            software_features_elements = software_main_element.find_elements(By.CLASS_NAME, 'definition-list-description--right')
            software_features = [software_features_element.text.replace("\n", ",") for software_features_element in software_features_elements]
            print(software_features)

            # Chassis open 
            chassis_main_click = driver.find_elements(By.CLASS_NAME, 'details__content-lower')[2].click()
            ## Chassis Field
            chassis_main_element = driver.find_elements(By.CLASS_NAME, 'is-accordion-open')[2]
            ### Chassis main features
            chassis_main_features_elements = chassis_main_element.find_elements(By.CLASS_NAME, 'details__content-subhead-copy--short-break')
            chassis_main_features = [chassis_main_features_element.text for chassis_main_features_element in chassis_main_features_elements]
            print(chassis_main_features)
            ### Chassis other features
            chassis_other_features_elements = chassis_main_element.find_elements(By.CLASS_NAME, 'definition-list-description--right')
            chassis_other_features = [chassis_other_features_element.text for chassis_other_features_element in chassis_other_features_elements]
            print(chassis_other_features)

            # Network open
            network_main_click = driver.find_elements(By.CLASS_NAME, 'details__content-lower')[3].click()
            ## Network Field
            network_main_element = driver.find_elements(By.CLASS_NAME, 'is-accordion-open')[3]
            ### Network main features
            network_main_features_elements = network_main_element.find_elements(By.CLASS_NAME, 'details__content-subhead-copy--short-break')
            network_main_features = [network_main_features_element.text for network_main_features_element in network_main_features_elements]
            print(network_main_features)
            ### Network other features
            network_other_features_table_elements = network_main_element.find_elements(By.CLASS_NAME, 'details__content-definition-list')
            network_other_features_elements = network_other_features_table_elements[-1].find_elements(By.CLASS_NAME, 'definition-list-description--right')
            network_other_features = [network_other_features_element.text.replace('\n', ', ') for network_other_features_element in network_other_features_elements]
            # Pad the key_features list with empty strings if there are fewer than 7 features
            while len(network_other_features) < 9:
                network_other_features.append('') 
            print(network_other_features)

            # Contact open
            contact_main_click = driver.find_elements(By.CLASS_NAME, 'details__content-lower')[4].click()
            ## Contact Field
            contact_main_element = driver.find_elements(By.CLASS_NAME, 'is-accordion-open')[4]
            ### Contact website url
            contact_features_elements = contact_main_element.find_elements(By.CLASS_NAME, 'details__content-subhead-copy--short-break')
            contact_features = [contact_features_element.text for contact_features_element in contact_features_elements]
            print(contact_features)

            # Industry open
            industry_main_click = driver.find_elements(By.CLASS_NAME, 'details__accordion-container')[5].click()
            ## Industry Field
            industry_main_element = driver.find_elements(By.CLASS_NAME, 'is-accordion-open')[5]
            ### Industry features
            industry_features_element = industry_main_element.find_element(By.CLASS_NAME, 'details__content-features--no-border')
            industry_features = [industry_features_element.text.replace('\n', ', ')]
            print(industry_features)




            
            # Save the extracted information to a CSV file
            with open('Products_info.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(product_number + [device_subtitle, device_title] + key_features + product_description + 
                                overview_device_type + overview_network_technology + overview_category_support + 
                                contact_sales + contact_sales_email + hardware_main_antenna + hardware_main_battery + 
                                hardware_main_display + hardware_main_ethernet + hardware_main_sim + hardware_main_usbports + 
                                hardware_main_voltage + other_features + software_main_baseband + software_main_clientType + 
                                software_main_system + software_features + chassis_main_features + chassis_other_features + 
                                network_main_features + network_other_features + contact_features + industry_features)
        except NoSuchElementException:
            print(f"Could not find device subtitle or title for {url}")

        # Close the browser window
        driver.quit()
        print("===============")

print("Information scraped and saved to verizon_device_info.csv")