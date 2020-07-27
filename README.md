# AUTOHERO

 This project is intended for Automation in Selenium for AUTOHERO Task.
 
 The TECH STACK used are
 
 - Python
 - Behave
 - Gherkin
 - Assertion
 - Browsers compatibility (Safari, Chrome)
    
## Requirements and Setting up 

1. Install Python 3.6 and above
2. Install [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
3. Download Chrome Webdriver for Selenium
4. Add Chrome Webdriver path in the Environmental Variables
5. Run the following commands in the project folder:

    `virtualenv venv`
    
    `source venv/bin/activate` (For mac users)
    
    or `venv/Scripts/activate.bat` (For Windows users)
    
    `pip install -r requirements.txt`

     `behave --tags @search_page` (Basic Scenario)
     
6. After running the above commands, logs can be seen under ./logs.txt which is created dynamically from the project on the run time.
     
## TODO

- Proper structuring of project for easy maintenance.
- Write a good amount of scenario by splitting up the requirement.
- Write the driver related methods in separate file for maintenance and accessibility.
- Plugin tools like Allure for the reporting purpose in JENKINS.
- Use more assertion points.
     

    
    