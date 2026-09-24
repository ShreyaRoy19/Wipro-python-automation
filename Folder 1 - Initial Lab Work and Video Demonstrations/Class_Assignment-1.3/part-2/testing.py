 #Identify multiple elements of the same type on a webpage and use Selenium to find and work with the list of elements. 
 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8000")
driver.maximize_window()

print("\n===== MULTIPLE ELEMENT IDENTIFICATION =====\n")

projects = driver.find_elements(By.CLASS_NAME, "project-card")

print("Total Project Cards:", len(projects))
for i, project in enumerate(projects, start=1):
    print(f"\nProject {i}:")
    print(project.text)

print("\n-----------------------------------")

skills = driver.find_elements(By.CLASS_NAME, "skill-card")

print("Total Skill Cards:", len(skills))
for i, skill in enumerate(skills, start=1):
    print(f"\nSkill {i}:")
    print(skill.text)

print("\n-----------------------------------")

buttons = driver.find_elements(By.TAG_NAME, "button")

print("Total Buttons:", len(buttons))
for i, button in enumerate(buttons, start=1):
    print(f"Button {i}: {button.text}")

print("\n-----------------------------------")

inputs = driver.find_elements(By.TAG_NAME, "input")

print("Total Input Fields:", len(inputs))
for i, input_field in enumerate(inputs, start=1):
    print(f"Input {i}")
    print("Type:", input_field.get_attribute("type"))
    print("Name:", input_field.get_attribute("name"))
    print("ID:", input_field.get_attribute("id"))

print("\n-----------------------------------")

links = driver.find_elements(By.TAG_NAME, "a")

print("Total Links:", len(links))
for i, link in enumerate(links, start=1):
    print(f"Link {i}: {link.text}")
    print("URL:", link.get_attribute("href"))

print("\n-----------------------------------")

project_titles = driver.find_elements(
    By.CSS_SELECTOR,
    ".project-card h3"
)

print("Total Project Titles:", len(project_titles))
for i, title in enumerate(project_titles, start=1):
    print(f"Project Title {i}: {title.text}")

print("\n===== END OF TEST =====")

time.sleep(5)

driver.quit()
