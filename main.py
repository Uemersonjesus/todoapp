from flet import*
from login_page import Loginpage 
from functions import  init_function 

page_first =   Loginpage()

init_function()
def main(page :Page) :


    page.add(page_first.square_main) 
 
app(target=main)   


 
