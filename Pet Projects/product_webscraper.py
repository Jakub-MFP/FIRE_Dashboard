from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

# you can adjust the search filters for each site by adjusting the filters on the target website then pasting the new URL on the source#
source1 = "https://www.target.com/s?searchTerm=video+games"
source2 = "https://www.gamestop.com/search/?q=video+games&lang=default"
source3 = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2540003.m570.l1311&_nkw=video+games&_sacat=0"
source4 = "https://www.bestbuy.com/site/electronics/video-games/abcat0700000.c?id=abcat0700000"
source5 = "https://www.walmart.com/cp/video-games/2636?search_redirect=true&redirect_query=video%20games&redirectQuery=video%20games"
source6 = "https://www.amazon.com/s?k=video+games&ref=nb_sb_noss_1"

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome()

print("**************************************************************** \n")
print("                        Starting Program, Please wait . . . .  \n")
print("Connecting to Target")
wd.get(source1)
wd.implicitly_wait(wait_imp)
t_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]")
pr_name = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[1]/h1/span")
product = pr_name.text
r_price = t_price.text
# print(r_price[1:])
print (" ---> Successfully retrieved the price from Target  \n")
time.sleep(2)

print("Connecting to GameStop")
wd.get(source2)
wd.implicitly_wait(wait_imp)
g_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]")
raw_p = g_price.txt
# print(raw_p[2:])
print (" ---> Successfully retrieved the price from GameStop  \n")
time.sleep(2)

print("Connecting to Ebay")
wd.get(source3)
wd.implicitly_wait(wait_imp)
e_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]")
raw_e = e_price.txt
# print(raw_e[2:])
print (" ---> Successfully retrieved the price from Ebay  \n")
time.sleep(2)

print("Connecting to BestBuy")
wd.get(source4)
wd.implicitly_wait(wait_imp)
b_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]")
raw_b = b_price.txt
# print(raw_b[2:])
print (" ---> Successfully retrieved the price from BestBuy  \n")
time.sleep(2)

print("Connecting to Walmart")
wd.get(source5)
wd.implicitly_wait(wait_imp)
w_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]")
raw_w = w_price.txt
# print(raw_w[2:])
print (" ---> Successfully retrieved the price from BestBuy  \n")
time.sleep(2)

print("Connecting to Amazon")
wd.get(source6)
wd.implicitly_wait(wait_imp)
a_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]")
raw_a = a_price.txt
# print(raw_a[2:])
print (" ---> Successfully retrieved the price from Amazon  \n")
time.sleep(2)

# Final display
print ("#----------------------------------------------------------------------------------------#")
print ("Price for [{}] on all websites, Prices are in USD \n".format(product))
print ("Price available at Target is: "+r_price[1:])
print ("   Price available at GameStop is: "+raw_p[2:])
print ("   Price available at Ebay is: "+raw_e[2:])
print ("   Price available at BestBuy is: "+raw_b[2:])
print ("   Price available at Walmart is: "+raw_w[2:])
print ("   Price available at Amazon is: "+raw_a[2:])