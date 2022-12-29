import re # RegEx
import pandas as pd

print(f"\n**************************************************")
print('**********      "Super Duper Tool!"     **********')
print('**************************************************')
print(f"\nThe basic idea of this program is to take a plain text file that has a list, compare it to a CSV file, and show results.")

# RegEx for user responses
response1 = "(y|Y)"
response2 = "(n|N)"

# Provide list of workstations in a plain text file. This takes advantage of how the terminal/shell 
# will input the literal path and the file can be located anywhere on your HDD! Just drag and drop...
prompt1 = f"\nSample text file of hostnames to convert to CSV [Drag & drop file to terminal and press ENTER]\n"
prompt1 += f"\n--- Don't forget to [CLICK] back into the terminal window --- \n"
prompt1 += f"\nFilepath: "
txt_file_loc = input(str(prompt1))

# Master CSV file of all workstations to compare against. Just drag and drop!
prompt2 = f"\nMaster CSV file - drop file directly into terminal!\n"
prompt2 += f"\n--- Don't forget to [CLICK] back into the terminal window --- \n"
prompt2 += f"\nFilepath: "
all_devices_loc = input(str(prompt2))

# Converts plain text file to CSV for 1-to-1 comparison
prompt3 = "\nConvert text file to CSV? [ Y | N ] "
user_response1 = input(str(prompt3))

# Sit back and relax...
prompt3 = "\nAre we ready? [ Y | N ] "
user_response2 = input(str(prompt3))

# Function converts the text file to CSV and adds uppercase
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
    df2_stuff1 = df2[['Name', 'Status', 'OS Version', 'IP Address', 'MAC Address']]
    df2_stuff2 = df2_stuff1.reset_index(drop=True)
    merge = pd.merge(df1, df2_stuff2, on='Name')
    print(merge)
    # If you want to output the results as a CSV file instead of outputting to your
    # screen, comment out line 50 above and remove the comment from line 53.
    #merge.to_csv("results.csv")
 
# User response will tell Python what to do
if(re.search(response1, user_response1)):
      convert_txt_to_csv()
if(re.search(response1, user_response2)):
    compare_files()
else:
    print("Goodbye!")
