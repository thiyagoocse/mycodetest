# **README**

## **Introduction**
The repository contains playwright (python) tests that automates the below given test scenarios and the installation steps.

Playwright for Python was created specifically to accommodate the needs of end-to-end testing.
The Playwright library can be used as a general purpose browser automation tool, providing a powerful set of APIs to automate web applications

## **Usage Guide**

**Minimum System requirements**
  > Python 3.8 or higher.
  > Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL).

**Installation Commands**
```
pip install --upgrade pip
pip install playwright
playwright install
pip install python-dotenv
```
**After the installation**
> Please execute the below commands to check the Python, Playwright, dotenv installations
```
python --version
pip list
```
**Note**
  If any issues observed during playwright install command, follow the below steps
  Manually download the file from this url [https://playwright.azureedge.net/builds/chromium/1117/chromium-win64.zip] extract and keep it in the folderpath like this AppData/local/ms-playwright/chromium-1117/

**Secure way of handling Url, username & password** 
```
create .env file and store the following details like url, username, password in secure way
URL="https://testurl.no/"
USER_NAME="testuser@email.com"
PASSWORD="your_password"
```
### **Test Scenario**
**Test 1:-Create an app – attach APPI – verify details after creating app – delete app**
```
  Launch the URL.
  Login with username and password.
  Create the New application by selecting the existing API.
  Verify the details in newly created API.
  Delete the APP.
  Logout & Close the browser.
```
**Test 2:Verify navigation to API explorer from diff parts of application and verify the list of APIs displayed as expected including list under different categories**
```
  Launch the URL.
  Login with username and password.
  Navigate through Browse API -> Verify the list of APIs present in each categories.
  Navigate through API Explorer in the Top menu -> Verify the list of APIs present in each categories.
  Navigate through API Explorer in the bottom menu -> Verify the list of APIs present in each categories.
  Logout & Close the browser.
```
