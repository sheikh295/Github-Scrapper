import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

username = input("Please enter the target GIT username: ")
keyword = input("Please Enter the Keyword you want to search for: ")

service = Service(executable_path='C:\web_dev_projects\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(f"https://github.com/{username}")
git_username = f"https://github.com/{username}"

repo_name = []
repo_url = []
repo1_files = []
repo1_file_urls = []

repo2_files = []
repo2_file_urls = []

repo3_files = []
repo3_file_urls = []

repo4_files = []
repo4_file_urls = []

repo5_files = []
repo5_file_urls = []

repo6_files = []
repo6_file_urls = []

def opening_raw():
    html1 = driver.page_source
    html1 = f"{html1}"
    if "raw-button" in html1:
        # raw = driver.find_element(By.CLASS_NAME, "js-permalink-replaceable-link")
        raw = driver.find_element(By.XPATH, "//a[@data-testid='raw-button']")
        raw.click()
        time.sleep(3)
        html2 = driver.page_source
        html2 = f"{html2}"
        if keyword in html2:
            url = driver.current_url
            print(f"Found {keyword} here: '{url}'")


def repo1():
    driver.get(repo_url[0])
    time.sleep(2)
    resource2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in resource2:
        repo1_files.append(a.text)
    time.sleep(2)
    # repo1_files.pop(0)
    # repo1_files.pop(0)
    # repo1_files.pop(0)
    # repo1_files.pop(0)
    print(f"Repo 1 files: '{repo1_files}'")
    for b in repo1_files:
        inserted_repo1_file = f"{repo_url[0]}/blob/master/{b}"
        repo1_file_urls.append(inserted_repo1_file)
        driver.get(inserted_repo1_file)
        opening_raw()

def repo2():
    driver.get(repo_url[1])
    time.sleep(2)
    resource3 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in resource3:
        repo2_files.append(a.text)
    time.sleep(2)
    # repo2_files.pop(0)
    # repo2_files.pop(0)
    # repo2_files.pop(0)
    # repo2_files.pop(0)
    print(f"Repo 2 files: {repo2_files}")
    for b in repo2_files:
        inserted_repo2_file = f"{repo_url[1]}/blob/master/{b}"
        repo2_file_urls.append(inserted_repo2_file)
        driver.get(inserted_repo2_file)
        opening_raw()

def repo3():
    driver.get(repo_url[2])
    time.sleep(2)
    resource4 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in resource4:
        repo3_files.append(a.text)
    time.sleep(2)
    # repo3_files.pop(0)
    # repo3_files.pop(0)
    # repo3_files.pop(0)
    # repo3_files.pop(0)
    print(f"Repo 3 files: {repo3_files}")
    for b in repo3_files:
        inserted_repo3_file = f"{repo_url[2]}/blob/master/{b}"
        repo3_file_urls.append(inserted_repo3_file)
        driver.get(inserted_repo3_file)
        opening_raw()

def repo4():
    driver.get(repo_url[3])
    time.sleep(2)
    resource5 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in resource5:
        repo4_files.append(a.text)
    time.sleep(2)
    # repo4_files.pop(0)
    # repo4_files.pop(0)
    # repo4_files.pop(0)
    # repo4_files.pop(0)
    print(f"Repo 4 files: {repo4_files}")
    for b in repo4_files:
        inserted_repo4_file = f"{repo_url[3]}/blob/master/{b}"
        repo4_file_urls.append(inserted_repo4_file)
        driver.get(inserted_repo4_file)
        opening_raw()

def repo5():
    driver.get(repo_url[4])
    time.sleep(2)
    resource6 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in resource6:
        repo5_files.append(a.text)
    time.sleep(2)
    # repo5_files.pop(0)
    # repo5_files.pop(0)
    # repo5_files.pop(0)
    # repo5_files.pop(0)
    print(f"Repo 5 files: {repo5_files}")
    for b in repo5_files:
        inserted_repo5_file = f"{repo_url[4]}/blob/master/{b}"
        repo5_file_urls.append(inserted_repo5_file)
        driver.get(inserted_repo5_file)
        opening_raw()

def repo6():
    driver.get(repo_url[5])
    time.sleep(2)
    resource7 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in resource7:
        repo6_files.append(a.text)
    time.sleep(2)
    # repo6_files.pop(0)
    # repo6_files.pop(0)
    # repo6_files.pop(0)
    # repo6_files.pop(0)
    print(f"Repo 6 files: {repo6_files}")
    for b in repo6_files:
        inserted_repo6_file = f"{repo_url[5]}/blob/master/{b}"
        repo6_file_urls.append(inserted_repo6_file)
        driver.get(inserted_repo6_file)
        opening_raw()

resource1 = driver.find_elements(By.CLASS_NAME, "repo")
for i in resource1:
    repo_name.append(i.text)

print(f"Repositories: '{repo_name}'")

for l in repo_name:
    inserted_repo_name = f"{git_username}/{l}"
    repo_url.append(inserted_repo_name)

print(f"Repo Urls/links: '{repo_url}'")

repo1()
repo2()
repo3()
repo4()
repo5()
repo6()

driver.close()