
# What is this program for?

This program is to scrape the contents of news article of one of a Vietnamese webmedia "[VNExpress](https://vnexpress.net/)"  
I personally use this program to make materials to learn Vietnamese language.

# What you should do before using this program
Type or paste a Location in a txt-file named "*save_space.txt*" **without any linebreak** in which you want to save scraped txt files.  
    
For Example: C:/Users/User_name/Desktop/  
  
Simply save and close the file after that.

# How to use this program
Execute it from command-line by typing as below and hit enter:   
python vs.py "an URL of VNExpress article"   
  
For Example:   
python vs.py "https://vnexpress.net/pho-thu-tuong-goi-phuc-hoi-kinh-te-lam-than-trong-de-tranh-so-suat-4471202.html"   
  
Notice that 1 VNExpress URL is required as a command-line argument.  
The contents will be scraped and immediately opened as a txt file.   


# Important Notice

This program has been made 6/1st/2022, so if the specification of VNExpress is editted or changed, this program might get out of order. Please keep it in your mind.  
You need to have "bs4" and "requests" libraries.
