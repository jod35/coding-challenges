import csv

file_=open ("mydata.csv","r")
new_record="Jona,Se,2018"

file_.write(str(new_record))

file_.close()
