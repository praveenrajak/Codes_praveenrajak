import csv
import os
import sys

source_file_path=sys.argv[1]
source_file_name=sys.argv[2]
target_file_path=sys.argv[3]
filter_name=sys.argv[4]
source_filename=''.join([source_file_path,source_file_name])
target_filename1=''.join([target_file_path,filter_name])
target_filename=''.join([target_filename1,'.csv'])

print(target_filename)
if len(sys.argv) < 6:
    print ("wrong no of inputs arguments")
    sys.exit()


source_filename=''.join([source_file_path,source_file_name])


cnt=0
with open (source_filename,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    with open (target_filename,mode='w') as state_files:
        for row in csvreader:
        #print(row[4])

            if row [4] == filter_name:

                arizona_writer=csv.writer(state_files,delimiter=',')
                arizona_writer.writerow(row)
            #print (row)
                cnt +=1


print("the count is:",cnt)

#python3 source_file_path source_file_name target_file_path target_file_name filter_name
#python splitfiles.py /users/praveenrajak/Desktop/dataset breweries_us.csv /users/praveenrajak/Desktop/dataset breweries_us_arizona.csv arizona
