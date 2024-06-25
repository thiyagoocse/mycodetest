from playwright.sync_api import sync_playwright, Playwright
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
import os
import time

load_dotenv()
url=os.getenv("URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Function for Application Login
def login_developer_portal(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    # open developer portal
    page.goto(url)
    # ignore cookies popup
    page.locator("//a[text()=\"OK\"]").click()
    # click login button
    page.locator('//a[@href="/login"]').click()
    page.locator('//*[text()="Email address"]/parent::span//input').type(username)
    page.locator('//*[text()="Password"]/ancestor::label/parent::div//input').type(password)
    page.locator('//*[text()="Log in"]/parent::button').click()
    page.wait_for_selector('//*[text()="Log out"]/parent::button',state="visible")
    return browser, page

# Function to Create Application & Select the Existing API
def create_app(page: Page ):
    page.locator('//a[@href="/application/new"]').click()
    page.locator('//*[text()="Application name"]/parent::span//input').type("test-app")
    page.locator('//*[text()="Application description"]/parent::span//textarea').type('Test app for developer portal')
    page.locator('//*[text()="Next"]/parent::button').click()
    # select currencies api
    page.locator('//*[text()="Currencies"]/parent::span//input').click()
    page.locator('//*[text()="Next"]/parent::button').click()
    # select scope
    page.locator('//*[text()="Next"]/parent::button').click()
    # create application
    page.locator('//*[text()="Create application"]/parent::button').click()
    page.locator('//*[text()="Go to application"]/parent::a').click()
    return page

# Function to Verify the details in the newly created APP & Delete APP
def verify_and_delete_app(app_page: Page):
    appid = app_page.locator('//*[text()="App-Id"]/following-sibling::p').text_content()
    print(f"Appid Id is : {appid}")
    expect(app_page.locator('//*[text()="Owner"]/following-sibling::p')).to_have_text("test user")
    app_page.locator('//*[text()="Delete app"]/parent::button').click()
    app_page.locator('//div[@role="alertdialog"]//*[text()="Delete app"]/parent::button').click()
    app_page.locator('//*[text()="Log out"]/parent::button').click()
    print("Test 1 - CreateApp,VerifyAPP,DeleteAPP - Successful")
   
# Function to Verify the API Explorer through BrowseAPI Option  
def browse_app(api_explorer: Page):
    api_explorer.locator('//*[text()="Browse APIs"]/parent::a').click()
    api_explorer.wait_for_selector('//*[text()="Discover APIs that enable you to create great user experiences"]/parent::div/p',state="visible")
    
    # Verify the list of APIs in 'ALL' Category Selection
    api_explorer.locator('//*[text()="All"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Information Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Account Pre-validation"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Currencies"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Payment Initiation Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="PSD2 Fallback"]/parent::p',state="visible")
    # Verify the list of APIs in 'Corporate APIs' Category Selection
    api_explorer.locator('//*[text()="Corporate APIs"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Pre-validation"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Currencies"]/parent::p',state="visible")
    # Verify the list of APIs in 'Regulatory APIs' Category Selection
    api_explorer.locator('//*[text()="Regulatory APIs"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Information Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Payment Initiation Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="PSD2 Fallback"]/parent::p',state="visible")
    print("Test 2.1 - Navigation through Browse API - Successful")

# Function to Verify the API Explorer through TopMenu Option  
def topmenu_navigation(api_explorer: Page):

    api_explorer.locator('//*[text()="Menu"]/parent::button').click()
    api_explorer.locator('//*[text()="API explorer"]//parent::a').click()

    api_explorer.wait_for_selector('//*[text()="Discover APIs that enable you to create great user experiences"]/parent::div/p',state="visible")
    
    # Verify the list of APIs in 'ALL' Category Selection
    api_explorer.locator('//*[text()="All"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Information Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Account Pre-validation"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Currencies"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Payment Initiation Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="PSD2 Fallback"]/parent::p',state="visible")
    # Verify the list of APIs in 'Corporate APIs' Category Selection
    api_explorer.locator('//*[text()="Corporate APIs"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Pre-validation"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Currencies"]/parent::p',state="visible")
    # Verify the list of APIs in 'Regulatory APIs' Category Selection
    api_explorer.locator('//*[text()="Regulatory APIs"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Information Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Payment Initiation Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="PSD2 Fallback"]/parent::p',state="visible")
    print("Test 2.2 - Navigation through Top Menu Option - Successful")

# Function to Verify the API Explorer through BottomMenu Option      
def bottommenu_navigation(api_explorer: Page):

    api_explorer.locator('//*[text()="API Explorer"]//parent::a').click()
    api_explorer.wait_for_selector('//*[text()="Discover APIs that enable you to create great user experiences"]/parent::div/p',state="visible")
    
    # Verify the list of APIs in 'ALL' Category Selection
    api_explorer.locator('//*[text()="All"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Information Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Account Pre-validation"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Currencies"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Payment Initiation Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="PSD2 Fallback"]/parent::p',state="visible")
    # Verify the list of APIs in 'Corporate APIs' Category Selection
    api_explorer.locator('//*[text()="Corporate APIs"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Pre-validation"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Currencies"]/parent::p',state="visible")
    # Verify the list of APIs in 'Regulatory APIs' Category Selection
    api_explorer.locator('//*[text()="Regulatory APIs"]/parent::button').click()
    api_explorer.wait_for_selector('//*[text()="Account Information Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="Payment Initiation Service"]/parent::p',state="visible")
    api_explorer.wait_for_selector('//*[text()="PSD2 Fallback"]/parent::p',state="visible")
    api_explorer.locator('//*[text()="Log out"]/parent::button').click()
    print("Test 2.3 - Navigation through Bottom Menu Option - Successful")

# Test Cases
# Test1: Create APP, Verify APP, Delete APP    
with sync_playwright() as playwright:
    browser, login_page = login_developer_portal(playwright)
    app_page = create_app(login_page)
    verify_and_delete_app(app_page)
    browser.close()

# Test2: API Explorer Different Navigations
with sync_playwright() as playwright:
    browser, login_page = login_developer_portal(playwright)
    api_explorer = browse_app(login_page)
    api_explorer = topmenu_navigation(login_page)
    api_explorer = bottommenu_navigation(login_page)
    browser.close()
