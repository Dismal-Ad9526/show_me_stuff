# show_me_stuff

The basic idea of this program is to take a plain text file that has a list, compare it to a CSV file, and show results. 




**Necessary Libraries:**
1. Install [RegEx](https://pypi.org/project/regex/) python library with `pip install regex`

2. Install [Pandas](https://pandas.pydata.org/docs/getting_started/index.html#getting-started) python library with `pip install pandas`


**`This works with Python v3.11.`**



**Hypothetical Scenario**


You need to find out what workstations are either online or offline, see what IP address it has, it's MAC address, what OS it has, etc. The only information you've been given is a list of twenty random workstations (i.e., `sample_text_file.txt`). You can export a report of all workstations you have in your domain (i.e., `sample_csv_master_file.csv` - to download: open the RAW file > then right-click on the page > Save as...), but there's a thousand workstations to go through. You **_could_** filter out the report by each individual workstation or CTRL+F your way through it, but ain't nobody got time for that! 


**How to Use this Program**


Sample files are in the repository that'll help show how this python program works - download and save them locally on your computer. All the data is made up and is only meant to illustrate what the program can do. Keep in mind that different reports from different programs or third party vendors will have different columns, rows, formatting, etc., so adjust accordingly!

1. Copy and save the program locally on your computer and run program in your terminal window

`python3 show_me_stuff.py` or `python show_me_stuff.py`


2. With the `sample_text_file.txt`, drag and drop that into the terminal - this will input the literal path to the file wherever it's located on your computer and saves the filepath as a variable. Press `Enter` to store the path in the variable.

3. Next, with the `sample_csv_master_file.csv`, drag and drop that into the terminal - this will also input the literal path to the file wherever it's located on your computer and assign it to a variable. Press `Enter` to store the path in the variable.

4. Because we need to have the same file types for the program to work, we have to convert the text file to a CSV - it's not too late to back out if you don't want to see awesomeness, but type `y` or `Y` to have the program work its magic, and press `Enter`.

5. Last chance - if you're ready, type `y` or `Y`, and press `Enter`.

6. Results will be printed on-screen in seconds! Time for an hour-long coffee break!



You could also save the results in a CSV - just comment out line 50 and uncomment line 53. It will save the results to wherever you ran the program from. 
