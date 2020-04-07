#Desktop Clean up program
import re,os,shutil,sys,datetime
text_pattern = re.compile(r'(.+\.txt)')
exl_pattern = re.compile(r'(.+\.xl.+)')
doc_pattern = re.compile(r'(.+\.do.+)')
ppt_pattern = re.compile(r'(.+\.pp.+)')
all_pattern = re.compile(r'(.+\.[t|x|d|p].+)')
txt_output = '../Desktop_bakcup/Text_file'
today = datetime.datetime.now()
today = today.strftime('%Y')
outpath = os.path.join(today)
if not os.path.isdir(outpath):
    os.mkdir(outpath)

i = choice = 0
print("Enter your Choice for file movement".center(50))
print()
print('''1 for EXL , 2 for TXT, 3 for DOC 4 for PPT 5 for All Files and 6 for Exit''')
# Loop to input the choice 
while i<3:
    try:
        choice = int(input())
        if choice >0:
            break
    except:
        print("Enter value from 1 to 5")
        i+=1
# loop to identify files
i = 1
for files in os.listdir('../'):
    
    if choice == 1 and exl_pattern.match(files):
        excel_result = exl_pattern.match(files).group()
        excel_result1 = os.path.join('../',exl_pattern.match(files).group())
        if excel_result not in os.listdir(outpath):
            shutil.move(excel_result1,outpath)
            print("{} file moved from desktop to {}".format(excel_result,outpath))
 
    if choice == 2 and text_pattern.match(files):
        text_result = text_pattern.match(files).group()
        text_result1 = os.path.join('../',text_pattern.match(files).group())
        if text_result not in os.listdir(outpath):
            shutil.move(text_result1,outpath)
            print("{} file moved from desktop to {}".format(text_result,outpath))
            
    if choice == 3 and doc_pattern.match(files):
        doc_result = doc_pattern.match(files).group()
        doc_result1 = os.path.join('../',doc_pattern.match(files).group())
        if doc_result not in os.listdir(outpath):
            shutil.move(doc_result1,outpath)
            print("{} file moved from desktop to {}".format(doc_result,outpath))

    if choice == 4 and ppt_pattern.match(files):
        ppt_result = ppt_pattern.match(files).group()
        ppt_result1 = os.path.join('../',ppt_pattern.match(files).group())
        if ppt_result not in os.listdir(outpath):
            shutil.move(ppt_result1,outpath)
            print("{} file moved from desktop to {}".format(ppt_result,outpath))

    if choice == 5 and all_pattern.match(files):
        all_result = all_pattern.match(files).group()
        all_result1 = os.path.join('../',all_pattern.match(files).group())
        if all_result not in os.listdir(outpath):
            shutil.move(all_result1,outpath)
            print("{} file moved from desktop to {}".format(all_result,outpath))

    if choice >= 6 or choice <1:
        print("Invalid Input, please try again ")
        sys.exit()

