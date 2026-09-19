from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate 
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


target_course_name = "Appium (Selenium) - Mobile Automation Testing from Scratch"

# 1. Locate the specific Web Table 
table = driver.find_element(By.NAME, "courses")

# 2. Extract all the rows from this table
rows = table.find_elements(By.TAG_NAME, "tr")

print("Scanning the table for the target course...\n")

# 3. Iterate through rows
for row in rows[1:]:
    # Find all columns in the current row
    columns = row.find_elements(By.TAG_NAME, "td")
    
    # Ensure the row actually contains data cells
    if len(columns) > 0:
        instructor = columns[0].text
        course_name = columns[1].text
        
        
        if course_name == target_course_name:
            
            price = columns[2].text
            
            print("--- Match Found! ---")
            print(f"Instructor: {instructor}")
            print(f"Course: {course_name}")
            print(f"Extracted Price: ${price}")
            
            

# Close browser
time.sleep(2)
driver.quit()