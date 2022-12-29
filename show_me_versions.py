import re # RegEx
import pandas as pd

print(f"\n**************************************************")
print('**********        CylancePROTECT        **********')
print('**************************************************')

# RegEx for user responses; you have to define the expected response!
response1 = "(y|Y)"
response2 = "(n|N)"

# List of endpoints in a text file. This takes advantage of how the CMD prompt will write the
# full file path and can be located anywhere on your HDD! Just drag and drop...
prompt1 = f"\nText file of endpoints to convert to CSV [Drag & drop file to terminal and press ENTER]\n"
prompt1 += f"\n--- Don't forget to [CLICK] back into the terminal window --- \n"
prompt1 += f"\nFilepath: "
txt_file_loc = input(str(prompt1))

# List of all devices - can be exported from Cylance console. Just drag and drop...
prompt2 = f"\nCSV file of all Devices - Export from Cylance Console\n"
prompt2 += f"\n--- Don't forget to [CLICK] back into the terminal window --- \n"
prompt2 += f"\nFilepath: "
all_devices_loc = input(str(prompt2))

# Converts text file to CSV for 1-to-1 comparison
prompt3 = "\nConvert text file to CSV? [ Y | N ] "
user_response1 = input(str(prompt3))

# Sit back and relax...
prompt3 = "\nLet's do some work! [ Y | N ] "
user_response2 = input(str(prompt3))

# Function for converting the text file to CSV
def convert_txt_to_csv():
    with open(txt_file_loc) as input:
        convert_uppercase = input.read().upper().strip()
    with open(txt_file_loc, 'w') as output:
        output.write(convert_uppercase)
    contents = pd.read_csv(txt_file_loc)
    contents.to_csv('output_file_this_can_be_deleted.csv', encoding='cp1252', header=['Name'], sep=',')

# Function merges similar values between 'df1' & 'df2' and prints output on-screen
def compare_files():
    df1 = pd.read_csv('output_file_this_can_be_deleted.csv', encoding='cp1252')
    df2 = pd.read_csv(all_devices_loc, encoding='cp1252')
    df2_picky1 = df2[['Name', 'State', 'Agent Version', 'IP Addresses', 'MAC Addresses', 'OS Version']]
    df2_picky2 = df2_picky1.reset_index(drop=True)
    merge = pd.merge(df1, df2_picky2, on='Name')
    print(merge)
 
# User response will tell Python what to do
if(re.search(response1, user_response1)):
      convert_txt_to_csv()
if(re.search(response1, user_response2)):
    compare_files()
else:
    print("Goodbye!")
   
# If you want to export results as an actual CSV...
# merge.to_csv("results.csv")
