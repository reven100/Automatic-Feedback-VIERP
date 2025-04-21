import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def get_credentials():
    root = tk.Tk()
    root.withdraw()  
    username = simpledialog.askstring("Input", "Enter your VIERP Username:")
    password = simpledialog.askstring("Input", "Enter your Password:", show='*') 
    return username, password
username, password = get_credentials()
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") 
driver = webdriver.Chrome(options=options)
driver.get("https://learner.vierp.in/")
elem = driver.find_element(By.XPATH, "/html/body/div[3]/section/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/input")
elem.clear()
elem.send_keys(username) 
elem = driver.find_element(By.XPATH, "/html/body/div[3]/section/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[3]/input")
elem.clear()
elem.send_keys(password) 
sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'v-btn') and contains(@class, 'bg-primary')]")
sign_in_button.click()

time.sleep(4) 
feedback_link = driver.find_element(By.XPATH, "//a[@href='/Feedback']")
feedback_link.click()

time.sleep(3)  
Course_link = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/main/div/div[2]/div[1]/a")
Course_link.click()

time.sleep(3)
Course_link2 = driver.find_element(By.XPATH, "//button[contains(@class, 'v-btn') and contains(@class, 'bg-primary')]//span[normalize-space()='PROCEED']")
Course_link2.click()

time.sleep(3)
Course_link3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/main/div/div/div[3]/div[4]/center/button/span[3]")
Course_link3.click()

time.sleep(3)
def part1_process(driver):
    """Fill out the feedback form by selecting radio buttons"""
    # Wait for form to be fully loaded
    time.sleep(2)
    
    # Find all radio button groups
    radio_groups = driver.find_elements(By.XPATH, "//div[contains(@class, 'v-card-title') and contains(@class, 'wrap-text')]")
    
    for group in radio_groups:
        try:
            # Get group container
            group_container = group.find_element(By.XPATH, "./parent::div")
            
            # Find all radio buttons in this group
            radio_buttons = group_container.find_elements(By.XPATH, ".//input[@type='radio']")
            
            # Randomly select top choices (Excellent, Strongly agree, Always, etc.)
            # Using random.choice from the first two options for variety
            if radio_buttons:
                choice = random.choice(radio_buttons[:2])
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", choice)
                time.sleep(0.2)  # Small delay for scroll
                choice.click()
                time.sleep(0.1)  # Small delay between clicks
        except Exception as e:
            print(f"Error processing a question group: {e}")
    
    # Optional: Add any comments
    try:
        comment_box = driver.find_element(By.XPATH, "//textarea")
        comment_box.send_keys("Great course and instructor!")
    except:
        print("Comment box not found or not accessible")



while True:  

    part1_process(driver)
    try:
        
        submit_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/main/div/center/button")
        submit_button.click()
        time.sleep(4)  
        start_time = time.time()
    except Exception as e:
        print(f"Error clicking the submit button: {e}")
    if time.time() - start_time > 10:
         break

driver.close()