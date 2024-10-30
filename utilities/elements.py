from TestData import data



url = "https://uat.baps.dev/mis"
user_name = "hiteshpatel1487"
password = "Ims@0503"

# browser #

browser = "chrome"


# Login_Page
sso_button_name = "submit"
username_id = "userName"
password_id = "password"
sign_in_xpath ="//button[@class='btn btn-primary btn-submit']"


#position
select_pisition_xpath ="//button[text()='North America System Admin']"


#managePerson

manage_person_xpath ="//span[text()='Manage Person']"
search_person_xpath = "//span[text()='Search Person']"
serach_button_xpath="//button[text()=' Search ']"
page_count_xpath = "//span[text()='10']"

#global_search
global_search_xpath = "(//span[text()='Global Search'])[1]"
first_name_xpath = "//input[@placeholder='First Name']"
last_name_xpath = "//input[@placeholder='Last Name']"
baps_id_xpath = "//input[@placeholder='BAPS ID / MIS ID / BAPS PID']"
global_search_button_xpath = "//button[text()='Search']"
mis_id_verification_xpath = f"//span[text()=' {data.misId} ']"


#Advance_serach

advance_search_xpath= "(//span[text()='Advanced Search'])[1]"
advance_search_button_xpath = "//button[text()=' Search ']"







