from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from csv import writer
from time import sleep


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def get_result(reg):
    subs = []

    try:
        driver.get("https://results.bput.ac.in/")

        # Searching the data
        Select(wait.until(EC.presence_of_element_located((By.ID, "select-Session")))).select_by_visible_text("Even-(2025-26)")
        driver.find_element(By.ID, "rollno").send_keys(reg)
        driver.find_element(By.ID, "dob").send_keys("2006-02-02")
        driver.find_element(By.ID, "btnViewStudentReseltsList").click()

        #AJAZ result js
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tb-odr-btns a"))).click()
        wait.until(lambda d: d.find_element(By.ID, "lblSgpa").text.strip() != "")


        #--------------Loaded Result-------------


        #NAME
        wait.until(lambda d: d.find_element(By.ID, "lblStudentName").text.strip() != "")
        name = driver.find_element(By.ID,"lblStudentName").text

        # Appending reg no and name
        subs.append(reg)
        subs.append(name)

        #ROW operation
        wait.until(EC.presence_of_element_located((By.ID, "tbl-results-marks")))
        rows = driver.find_elements(By.XPATH, '//*[@id="tbl-results-marks"]/tbody/tr')

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")

            code = cols[1].text.strip()
            subject = cols[2].text.strip()
            grade = cols[5].text.strip()
            subs.append(grade)

        #SGPA
        sgpa = driver.find_element(By.ID,"lblSgpa").text.split(":")[1].strip()
        subs.append(sgpa)
        print(reg,"Success")

    except Exception as e:
        print("Error", e)
        print(reg,"Not found")

    return subs




def write(lst):
    with open("mefinresult.csv","a+",newline="") as file:
        write = writer(file)
        write.writerow(lst)



start = 2501109291
end = 2501109379



# r = [i+2501109300 for i in [50,45]]

#main loop

# write(["RegNo","Name","Maths","Physics","BEE","PCDS","BCE","UHV","PHY LAB","BEE LAB","C LAB","Egnd Lab","Yoga/NCC","SGPA"])
for reg in range(start,end):
    lst = get_result(reg)
    if lst:
        write(lst)
        # print(lst)
    else:
        print("No data found for",reg)



driver.quit()
