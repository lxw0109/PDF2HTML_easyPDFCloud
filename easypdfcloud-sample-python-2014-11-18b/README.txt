[IMPORTANT REQUIREMENTS]

Python 3.3 or higher, Pip (if you do not have Python 3.4), Requests external library.
 
If you do not have Python 3.3 or higher:
1) Please update your version of Python. Visit https://www.python.org/ for details.

If you have Python 3.3 but DO NOT have Pip, the standard Python package manager:
1) Update your version or follow the official instructions to install Pip: http://www.pip-installer.org/en/latest/installing.html

Note: Python 3.4 ships with Pip so you won't have to worry about installing it! 


To install the Requests library:

1) Open the command prompt (Windows) or terminal (Mac)

2) Browse to the Scripts folder in your Python install directory using the "cd" command. If Python was installed at "C:\Python34", for 
   example, the path to your scripts folder would simply be "C:\Python34\Scripts" and in the command prompt you would enter 
   "cd C:\Python34\Scripts" to browse to that directory. 

3) You can check to see whether or not you have done this successfully by entering "dir" (Windows) or "ls" (Mac/Unix). If you see .exe
   files named "easy_install" and "pip" (some of them may have version numbers in their names, eg. "pip3.4.exe" or "easy_install-3.4.exe"), 
   you have browsed to the right location. 

4) Run the following command: "pip install requests". This will install the Requests library. 

For more information and other questions regarding installation of Requests, please visit the Requests website at: 
http://docs.python-requests.org/en/latest/

-----------------------------------

[API Usage Instructions]

This sample code shows how to use the developer API to upload a document to the EasyPDFCloud servers, convert it to any format with a 
specified workflow, and save it to your computer. To use this sample API:

1) Create an account at https://www.easypdfcloud.com and obtain developer status. If you do not have developer status, please visit 
   http://www.pdfonline.com/easypdfcloud/restapi/pdf-rest-api.html

2) Create a workflow.

3) Open and configure the provided "Properties.xml" file. Use the given instructions to fill each element with the appropriate information.

4) Run "EasyPDFCloudSample.py". The output file will automatically be given the same name as the input file, but will have a different 
   extension depending on the output format specified in the workflow you chose. 