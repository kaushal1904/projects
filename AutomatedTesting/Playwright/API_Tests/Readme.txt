#Playwright Automation API_Tests ~  Automated API testing of a web app v1.1

# Author: Kaushal Shastry
# Email: kaushal.shastry@outlook.com // kaushal19.shastry@gmail.com
# LinkedIn: www.linkedin.com/in/kaushal-shastry/
# PayPal: kaushal.shastry@outlook.com
#-----------------------------------------------------------------------------------------------------------------------

API testing an application is a software testing phase to check the new build's stability and ensure core APIs work. 

This suite has API test cases for Get, Post, Put and Delete requests. Used Visual Studio Code to build, test and run the application on MacOS 15.7.3. 

Tests are written in TypeScript. Playwright supports TypeScript, JavaScript, Python, .NET (C#) and Java. 

This suite can be used to test REST APIs and perform Smoke testing on any server. Make sure to set the 
"$base_url" in API calls to url you want to test accordingly. 
1. const response = await request.get('$base_url') 
2. const response = await request.post('$base_url') 
3. const response = await request.put('$base_url') 
4. const response = await request.delete('$base_url') 

Change the "$base_url" to the URL you want to test and verify the responses. Requests and the parameters should be set accordingly.

Tweaking specfic to the URL used in these tests: some resources(pets) might have been deleted or updated as this is an open url. Make sure to use the resource id(pet id) accordingly. 

Reach out for customization and for specific testing.

Playwright Documentation: https://playwright.dev/docs/intro

# Reach out via GitHub or Email for any communication
# Mentions and donations will be appreciated
