from selenium import webdriver

drive = webdriver.Chrome(
    executable_path="")  # your web browser I am using  chromedriver ("note: we need add the script detect the
# default browser ")
drive.get("*********")  # need to enter o your  site url

inp = drive.find_element(By.CLASS_NAME, "text_field")  # this is temp we need to fond the name of class

print(inp)

drive.close()