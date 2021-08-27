# apache-flume

# Storing the real time stock data from alpha vantage API using apache flume to HDFS.

Step 1: Get the API key
    https://www.alphavantage.co/support/#api-key

Step 2: Go through the documentation part of stock API

Step 3 : Write the python code to get the live stock data by creating stock.py file and     
              add API key from the env file.
Step 4: After writing the code run it to get the output of stock data

Step 5: Now, we have to create a file named stocks.conf inside the
        /home/naziya/apache-flume-1.9.0-bin/conf directory and add the flume 
        configuration. 
        Use the below-mentioned command for creating the file “stocks.conf”:
        touch stocks.conf or nano stocks.conf to create and edit.
        
Step 6: Now we will start the Flume agent by using a shell script called flume-ng. This 
        shell script is located in the bin directory of the Apache Flume distribution.
        We need to specify agent name, config directory, and config file on the          
        command line:
        In my case,
             bin/flume-ng agent –conf ./conf/ -f conf/stocks.conf -n agent1
            -Dflume.root.logger=DEBUG

Step 7: Now we can check if the output is written into the hdfs ie stocks_data by either using a web
        console (http://localhost:9870) or viewing the files in HDFS by using the command prompt.

     


