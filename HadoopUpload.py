import csv
import hdfs


client = hdfs.InsecureClient('http://localhost:9870/')

with open('C:/Users/Jonat/Documents/deds/week8/Hadoopie/Reviews_Data/H&M_reviews.csv', 'rb') as f:
    data = f.read()
    client.write("/data/HM_Reviews.csv", data)

with open('C:/Users/Jonat/Documents/deds/week8/Hadoopie/Reviews_Data/Zalando2_reviews.csv', 'rb') as f:
    data = f.read()
    client.write("/data/Zalando_Reviews.csv", data)

with open('C:/Users/Jonat/Documents/deds/week8/Hadoopie/Reviews_Data/Wehkamp_reviews.csv', 'rb') as f:
    data = f.read()
    client.write("/data/Wehkamp_Reviews.csv", data)