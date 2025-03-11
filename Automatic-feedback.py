import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_credentials():
    root = tk.Tk()
    root.withdraw()  
    username = simpledialog.askstring("Input", "Enter your VIERP Username:")
    password = simpledialog.askstring("Input", "Enter your Password:", show='*') 
    return username, password
username, password = get_credentials()
driver = webdriver.Chrome()
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
def part1_process():
    try:
        for i in range(3, 7):  
            b1 = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/main/div/div[2]/div/div[{i}]/div[3]/input")
            b1.click()
    except Exception as e:
        print(f"Error clicking b1 input in section 2: {e}")
    try:
       for i in range(2,15):
              b7 = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/main/div/div[{i}]/div/div[3]/div[3]/input")
              b7.click()
    except Exception as e:
        print(f"Error clicking b1 input in section 2: {e}")
    try:
        for i in range(3, 10): 
            b2 = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/main/div/div[3]/div/div[{i}]/div[3]/input")
            b2.click()
    except Exception as e:
        print(f"Error clicking b2 input in section 3: {e}")

    try:
        # Click on other input fields outside loops
        b3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/main/div/div[4]/div/div[3]/div[3]/input")
        b3.click()
    except Exception as e:
        print(f"Error clicking b3 input in section 4: {e}")

    try:
        b4 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/main/div/div[5]/div/div[3]/div[3]/input")
        b4.click()
    except Exception as e:
        print(f"Error clicking b4 input in section 5: {e}")

    try:
        
        for i in range(3, 5): 
            b5 = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/main/div/div[6]/div/div[{i}]/div[3]/input")
            b5.click()
    except Exception as e:
        print(f"Error clicking b5 input in section 6: {e}")
        
    try:
        for i in range(3,5): 
              b6 = driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/main/div/div[7]/div/div[{i}]/div[3]/input")
              b6.click()
    except Exception as e:
        print(f"Error clicking b1 input in section 2: {e}")


while True:   
    part1_process()
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