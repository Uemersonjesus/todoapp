
#here are the functions of the project 

from flet_core import icon
from variables import *
from flet import* 




def dropdown_register_key (e) :

    register_drop_down[0]  = e.control.value 



def show_chart_garph() : 
    
    

    groups_of_graph = []

    graph_of_all_money.bar_groups  = groups_of_graph


    time_for_compare =["01","02","03","04","05","06","07","08","09","10","11","12"]

    dic = acess_json("finance") 


    #capturando valores para formar os groupas de cada mês 
    for i in range(12)  :
        
        gain_in_moth  = 0 
        loss_in_moth = 0 
        save_in_moth = 0 

       
        for day in dic :

            
            if (time_for_compare[i] == day[2:4]) :


                register_save = dic[day]['investido']
                register_gain = dic[day]['ganho']
                register_loss = dic[day]['gasto']

                for register in register_save :

                    save_in_moth += register_save[register]

                
                for register in register_gain:

                    gain_in_moth += register_gain[register]
                
                
                for register in register_loss :

                    loss_in_moth += register_loss[register]
                

        groups_of_graph.append(

                    BarChartGroup(
                        x= i , 
                        bar_rods= [

                            BarChartRod(

                                from_y= 0 , 
                                to_y= save_in_moth , 
                                color= colors.AMBER_200 , 
                                border_radius= 4 , 

                            ) ,
                           
                            BarChartRod(
                                
                                from_y= 0 , 
                                to_y= gain_in_moth , 
                                color= colors.GREEN_300 , 
                                border_radius= 4 , 

                            ),
                            
                            
                            BarChartRod(
                                
                                from_y= 0 , 
                                to_y= loss_in_moth , 
                                color= colors.RED_300, 
                                
                                border_radius= 4 , 

                            )


                        ]
                    )
                )
        
        loss_in_moth = 0 
        gain_in_moth = 0
        save_in_moth = 0


def save_finance_json(dic)  :


    import json 

    from pathlib import Path 



    path = Path()/'finance.json'


    with open(path,'w')  as file :

        json.dump(
            dic,file,indent=2 
     ) 


def Remove_alert_dialog(e) :


    alert_dialog_drop_down.visible = False 


    square_page.update() 


def show_alert_dialog(typee):

     
    if typee == '1':
        
        
        alert_dialog_drop_down.content =Row(
                    controls=[

                        Text(value= " Please, choice one option !" ,font_family='poppins',weight= FontWeight.BOLD , size = 14 ) , IconButton(icon= icons.REMOVE,on_click= Remove_alert_dialog)
                    ]
                )
            

        alert_dialog_drop_down.visible = True 

        square_page.update()

    if typee == '2':
        
        
        
        alert_dialog_drop_down.content =Row(
                    controls=[

                        Text(value= " Please, fill out the data !" ,font_family='poppins',weight= FontWeight.BOLD , size = 20) , IconButton(icon= icons.REMOVE,on_click= Remove_alert_dialog)
                    ]
                )
            

        alert_dialog_drop_down.visible = True 

        square_page.update()





def  delete_finance_register(e,day,register,option) :

    dic = acess_json('finance') 
    
    
    if register == 'gasto' :
       
       del dic[day]['gasto'][option] 

    if register == 'ganho' :
       
       del dic[day]['ganho'][option] 

    if register == 'investido' :
       
       
       del dic[day]['investido'][option] 




    save_finance_json(dic )


    show_finance_page()


def counter_of_money()  :

    dic = acess_json('finance') 


    all_money_save = 0 
    all_money_loss = 0 
    all_money_get = 0 
    
    for day in dic :



        dic_current_gasto = dic[day]['gasto']
        dic_current_gain = dic[day]['ganho']
        dic_current_save = dic[day]['investido']



        for   information in dic_current_gasto :
      
            all_money_loss +=  dic_current_gasto[information] 

                
            
        for  information in dic_current_gain :

            all_money_get +=  dic_current_gain[information]  
        
        for information in dic_current_save:

            all_money_save +=  dic_current_save[information]



        all_money_variable.content = Column (

           
             controls=[ 

            Row(
                controls=[

                    Text(value='Money save',weight= FontWeight.BOLD , font_family= 'heveltica',size= 15 ) , 

                    Container(
                        width= 100 
                    )  , 

                    Text(value='Money gain',weight= FontWeight.BOLD , font_family= 'heveltica',size= 15 ) , 

                    Container(
                        width= 100 
                    ) ,

                    Text(value='Money loss',weight= FontWeight.BOLD , font_family= 'heveltica',size= 15 ) , 


                ]
            ),
            
            Row(
        controls=[



            Container(

                width=  200 , 
                height= 80, 

                bgcolor= colors.BLACK , 

                alignment = alignment.center ,

                content= Row(
                    controls=[

                        Text(
                            value = ' R$ ', font_family= 'heveltica' , weight = FontWeight.BOLD ,size =  15  


                        ) , 

                        
                        Text(
                    value = f' {all_money_save}', font_family= 'heveltica' , weight = FontWeight.BOLD ,size =  15 ,color= colors.YELLOW
                )
                    ]
                )


            ) , 





            
            Container(

                width=  200 , 
                height= 80 , 

                bgcolor= colors.BLACK , 

                alignment = alignment.center ,

                content= Row(
                    controls=[

                        Text(
                            value = ' R$ ', font_family= 'heveltica' , weight = FontWeight.BOLD ,size =  15  


                        ) , 

                        
                        Text(
                    value = f' {all_money_get}', font_family= 'heveltica' , weight = FontWeight.BOLD ,size =  15 ,color= colors.GREEN
                )
                    ]
                )


            ) ,


            
            Container(

                width=  200 , 
                height= 80 , 

                bgcolor= colors.BLACK , 

                alignment = alignment.center ,

                content= Row(
                    controls=[

                        Text(
                            value = ' R$ ', font_family= 'heveltica' , weight = FontWeight.BOLD ,size =  15  


                        ) , 

                        
                        Text(
                    value = f' {all_money_loss}', font_family= 'heveltica' , weight = FontWeight.BOLD ,size =  15 ,color= colors.RED
                )
                    ]
                )


            ) , 




        ] 
        
        
        ) 
        
        ] 
        
        )
     
    total =  all_money_get + all_money_loss + all_money_save
    percent_of_gain =  ( (total * all_money_get) / 100 ) / total
    percent_of_loss =  ( (total * all_money_loss) / 100 ) / total
    percent_of_save =  ( (total * all_money_save) / 100 ) / total


    graph_circle_of_all_money.sections = [

        PieChartSection(
            value = percent_of_gain , 
            color= colors.GREEN_700 ,
            border_side= BorderSide(0, colors.with_opacity(0, colors.WHITE))

        )  , 

         PieChartSection(
            value = percent_of_save , 
            color= colors.AMBER_500 ,
            border_side= BorderSide(0, colors.with_opacity(0, colors.WHITE))


        ) , 

         PieChartSection(
            value = percent_of_loss , 
            color= colors.RED_600 ,
            border_side= BorderSide(0, colors.with_opacity(0, colors.WHITE))



        )  ,




    ]

    square_page.update()


def show_date_of_finance_month()  :
   

   
   dic = acess_json("finance")   


   list_of_registers = [ ]
   for day in dic:  
       
       todo = dic[day]
       
       
       register_day= Container(
           width= 500 , 

           height= 80 , 
           border_radius= 4 , 
           bgcolor= colors.WHITE10 ,
           alignment= alignment.center, 
           content= Text(
               value= f' day {day[0:2]} of day {day[2:4]}', 
               font_family= 'poppins', 
               weight= FontWeight.BOLD , 
               size = 12  

           )
       ) 

       list_of_registers.append(
           
           register_day
       )


       for register in  todo :
        
        

        if register == 'ganho' :

            dic_register =  todo[register]

            
            for   anotations in dic_register :

                conteudo =  dic_register[anotations]
                
                if conteudo : 
                    register_todo =   Container(
                        width=  300 , 
                        height=  80 , 
                        bgcolor= colors.TRANSPARENT , 
                        alignment= alignment.center , 
                        content=  Container(
                            width= 280 , 
                            height= 70 , 
                            bgcolor= colors.BLACK12 , 
                            alignment= alignment.center ,  
                            content= Row(

                                

                            controls=[

                                Text(value=f'{anotations}',font_family= 'poppins',weight= FontWeight.BOLD ,size= 15,color= colors.WHITE) ,

                                Text(value=f'{conteudo}',font_family= 'poppins',weight= FontWeight.BOLD ,size= 15,color= colors.GREEN_200) ,
                                ElevatedButton(
                                
                                text='Delete',
                                on_click= lambda e , day = day , register = 'ganho' , option = anotations: delete_finance_register(e,day,register,option) )
                            ]
                    
                        ))
                    )

                    list_of_registers.append(

                        register_todo
                    )

        if register == 'gasto' :
           
            dic_register =  todo[register]

            
            for   anotations in dic_register :

                conteudo =  dic_register[anotations]
                
                if conteudo :
                    register_todo =   Container(
                        width=  300 , 
                        height=  80 , 
                        bgcolor= colors.TRANSPARENT , 
                        alignment= alignment.center , 
                        content=  Container(
                            width= 280 , 
                            height= 70 , 
                            bgcolor= colors.BLACK12 , 
                            alignment= alignment.center ,  
                            content= Row(

                                

                            controls=[

                                Text(value=f'{anotations}',font_family= 'poppins',weight= FontWeight.BOLD ,size= 15,color= colors.WHITE) ,

                                Text(value=f'{conteudo}',font_family= 'poppins',weight= FontWeight.BOLD ,size= 15,color= colors.RED_200) ,
                                ElevatedButton(
                                
                                text='Delete',
                                on_click= lambda e , day = day , register = 'gasto' , option = anotations : delete_finance_register(e,day,register,option) )
                            ]
                    
                        ))
                    )

                    list_of_registers.append(

                        register_todo
                    )

        if register == 'investido' :

            dic_register =  todo[register]

            
            for   anotations in dic_register :

                conteudo =  dic_register[anotations]
                
                if conteudo :
                    register_todo =   Container(
                        width=  300 , 
                        height=  80 , 
                        bgcolor= colors.TRANSPARENT , 
                        alignment= alignment.center , 
                        content=  Container(
                            width= 280 , 
                            height= 70 , 
                            bgcolor= colors.BLACK12 , 
                            alignment= alignment.center ,  
                            content= Row(

                                

                            controls=[

                                Text(value=f'{anotations}',font_family= 'poppins',weight= FontWeight.BOLD ,size= 15,color= colors.WHITE) ,

                                Text(value=f'{conteudo}',font_family= 'poppins',weight= FontWeight.BOLD ,size= 15,color= colors.YELLOW_200) ,
                                ElevatedButton(
                                
                                text='Delete',
                                on_click= lambda e , day = day , register = 'investido' , option = anotations : delete_finance_register(e,day,register,option) )
                            ]
                    
                        ))
                    )

                    list_of_registers.append(

                        register_todo
                    )













  
   list_of_registers_invert = []
   for anotation in list_of_registers:
       
       list_of_registers_invert.append(
           
        list_of_registers.pop()

       )
       

   
   registers_in_finance_show.content = Column(
       
       scroll= ScrollMode.ALWAYS ,
       controls=list_of_registers_invert
       
    ) 
   
   save_in_finance_date()

   
           




def save_in_finance_date() :

    total_of_finance.content =  Row(
        
        controls=[

            Row( controls=[ graph_circle_of_all_money,all_money_variable] ) ,

        ]
    )
    date_of_finance.content = Column(

        scroll= ScrollMode.ALWAYS,
        controls=[
            registers_in_finance_show
        ]


    )




def save_finance_date(e)  :


    import json
    from datetime import date 
    from pathlib import Path 

    dic = acess_json('finance') 

    today =  date.today()

    
    key = str(today.strftime('%d') )   + str(today.strftime('%m') ) + str(today.strftime('%y') ) 

    
    information_for  =  register_drop_down[0]
    
    

    if information_for == '' :
        
        
        
        show_alert_dialog('2')

    
    else :
       
        if  register_drop_down[0]  == 'save':

            dic[key]['investido'][text_field_money_key[0]]  = float( text_field_money_value[0] )
        
        
        if  register_drop_down[0]  == 'loss':

        
            dic[key]['gasto'][text_field_money_key[0]]  =  float(text_field_money_value[0])
        

        
        if  register_drop_down[0]  == 'gain':

        
            dic[key]['ganho'][text_field_money_key[0]]  =  float(text_field_money_value[0])

        

        
        save_finance_json(dic)

        show_finance_page() 







    


def save_text_field_money_key(e) :


    text_field_money_key[0] = e.control.value 


def save_text_field_money_value(e) :

    text_field_money_value[0] =e.control.value 

def show_save_finance()  :

    kind_for_register_in_dic =  Dropdown(
    width= 100 , 
    height = 100 , 
    bgcolor= colors.WHITE10 ,
    border_radius= 4,
    on_change= dropdown_register_key , 
    hint_text= 'option', 
    options= [
  
        dropdown.Option(
            'loss'
        ) ,

        
        dropdown.Option(
            'save'
        ),

        
        dropdown.Option(
            'gain'
        )
    ]
)


    save_finance.content =Column( controls=[

        Text(value='O primeiro passo para melhorá é ter noção daquilo que deve ser  alterado.',font_family='heveltica',weight= FontWeight.BOLD ,size=12) , 
        
        Row(
        controls=[

            Container(
                width= 200 
            ) , 

            kind_for_register_in_dic,

           TextField(hint_text= ' Com ? ', width= 300 , height= 100 , bgcolor= colors.WHITE10,on_change= save_text_field_money_key) , 
           
           TextField(hint_text= ' valor ',suffix_text= 'R$', width= 100 , height= 100 , bgcolor= colors.WHITE10 ,on_change= save_text_field_money_value )  ,

           ElevatedButton(
               text='Save' ,
               on_click= save_finance_date 
           )



        ]
    ) ]  ) 



def show_finance_page(e=0)  : 
    
    show_chart_garph()
    show_save_finance()
    counter_of_money()
    #this orderd is important because , for  show the things . 
    show_date_of_finance_month()
    
    from datetime import time,date,timedelta
    import json 
    from pathlib import Path 

    today = date.today() 

    key = str(today.strftime('%d') )   + str(today.strftime('%m') ) + str(today.strftime('%y') ) 
        
    path = Path()/'finance.json' 


    with open(path,'r')  as file :

          dic = json.load(file)
    
    #se este dia não existe o crie
    

    if dic.get(key,0) == 0 : 

        dic[key] = {

            "gastos":{},
            "ganhos":{},
            "investimentos":{}

        }


    
     
    change_for_another_page = Container(

    width= 200 , 
    height= 80 , 
    
    border_radius=   8 , 

    bgcolor= colors.WHITE10 , 

    alignment= alignment.center ,

    content= ElevatedButton(
        text='change page' , on_click= show_main_page

    ) , )

    

   
    square_page.content = Column(

        scroll= ScrollMode.ALWAYS , 
        
        controls= [


            Row(
                controls=[
                    Text(value= ' Make money ',font_family= 'heveltica',weight= FontWeight.BOLD,size = 20 ),
                
                    Container(
                        width=800 
                    )  ,
                    change_for_another_page , 
                ]
            ) , 

            save_finance ,
            total_of_finance ,
            Container(height= 100) ,

            Container(
                padding= padding.only(left= 300)  , 

                content= alert_dialog_drop_down 
            ),

            date_of_finance , 
            Container(height= 100) , 
            graph_of_all_money ,        
            Container(height= 100) , 


        ]
    )



    

    

    square_page.update()




def every_todo_analysis(e) :
    



    dic = acess_json('todo') 

    dic2 = acess_json("openorend")

    todo_list = []
    

    total = 0 
    total_end = 0 
    total_open= 0 
    
 
    for  day in dic :

        anotations = dic[day]  
        
        todo_list.insert(
            0 ,
                
            Container(

                    width= 200 , 
                    height= 80 , 
                    bgcolor= colors.WHITE10 , 

                    border_radius=  4 , 

                    alignment= alignment.center , 
                    content= Text(value=f' {day[0:2]} / {day[2:4]}') 
                )
            )

        

        for todo in anotations :

            conteudo = anotations[todo]
            container = Container(

                width= 200 , 
                height=  80 , 
                border_radius= 4  , 
                bgcolor= colors.WHITE10   , 

                alignment= alignment.center  , 
                content=  Row(controls=[
                    Text(value= f'{todo}',font_family='heveltica',weight= FontWeight.BOLD,bgcolor=colors.BLUE_300),

                    Text(value= f'{conteudo}',font_family='heveltica',weight= FontWeight.BOLD) ]), 

            )

            todo_list.insert(
                1,
                container
            )


            value = dic2[day][todo]

            total +=  1 

            if value == 'End'  :

                total_end+=  1
            
            
            if value =='open' :

                total_open += 1 

            


            


    todo_list.insert(
        0,
        Container(
            width= 400 , 
            height= 80 , 
            border_radius= 4 , 
            content=  Row(
                controls=[

                    Text(value=f'  total',weight= FontWeight.BOLD,font_family= 'heveltica',size= 12  ) ,Text(value=f'  {total}',weight= FontWeight.BOLD,font_family= 'heveltica',size= 12,color= colors.AMBER_300 ) ,Container(width= 100), Text(value='Open',weight= FontWeight.BOLD,font_family= 'heveltica',size= 12 , ) , Text(value=f'  {total_open}',weight= FontWeight.BOLD,font_family= 'heveltica',size= 12 , ),Container(width= 100),
                    Text(value=f' End ',weight= FontWeight.BOLD,font_family= 'heveltica',size= 12 , ),Text(value=f' {total_end}',weight= FontWeight.BOLD,font_family= 'heveltica',size= 12 ,color= colors.RED_300 ) ,Container(width= 100), ElevatedButton(text='Go back',on_click= counter_of_todo)
                ]
            )
    
        )
    )
    counter_for_todo.content = Column( 

        controls= todo_list  

    )


    square_page.update() 

def counter_of_todo(e=0) :
    
    from datetime import datetime ,date 

    today = date.today() 
    month =  today.strftime('%m')
    dic = acess_json('openorend')

    total = 0 
    openn = 0 
    end = 0 
    for day in dic :

        if  day[2:4] == str(month)   :

            
            todos =  dic[day] 

            for  todo in todos :


                

                total += 1 
                
                
                if  todos[todo] ==  'open'  :

                    openn += 1 

                
                if  todos[todo] ==  'End'  :

                    end += 1 

        
    
    row = Column(
        controls=[

            Row(controls=[Text(value='Todo in month',size=12,font_family='heveltica',weight= FontWeight.BOLD),
                          Container(width= 500 , )
                          
                           ]),
                           IconButton(icon= icons.ADD,on_click= every_todo_analysis),

             Row(
        controls=[

            Container(
                width= 200, 
                height= 100 ,
                border_radius= 4 , 
                bgcolor= colors.TRANSPARENT , 
                content= Text(value= f'total , {total}',font_family= 'heveltica',size= 12 , weight= FontWeight.BOLD) 

            ) ,   
            Container(
                width= 200, 
                height= 100 , 
                 border_radius= 4 , 
                bgcolor= colors.TRANSPARENT , 
                 content= Text(value= f'open , {openn}',font_family= 'heveltica',size= 12 , weight= FontWeight.BOLD)  

            ) ,    
            Container(
                width= 200, 
                height= 100 , 
                border_radius= 4 , 
                bgcolor= colors.TRANSPARENT , 

                content= Text(value= f' end , {end}',font_family= 'heveltica',size= 12 , weight= FontWeight.BOLD) 

            ) , 
        ]
    )
        ]
    )

    counter_for_todo.content = row 




    square_page.update() 
                








def show_new_todo_of_other_day(e,day)  :

    
    default_key[0]  =     str(day.strftime('%d') )   + str(day.strftime('%m') ) + str(day.strftime('%y') ) 
   
    show_calendar()
    show_todo()
    
def save_text_field_value(e) :

    import json
    from pathlib import Path 
    path = Path()/'todo.json'
    path2 = Path()/'openorend.json'

    dic = acess_json('todo')
     
     
    dic[default_key[0]][key_value[0]]  = todo_value[0]
    dic2 = acess_json('openorend')

    dic2[default_key[0]][key_value[0]]  = 'empty' 

    with open(path,'w')  as file :

        json.dump(dic,file,indent=2)
    

    with open(path2,'w')  as file :

        json.dump(dic2,file,indent=2)

    
    show_todo()



def save_text_field_key(e)  :

    key_value[0] = e.control.value 

def save_text_field_todo_value(e)  :

    todo_value[0] = e.control.value 

def acess_json(name :str) :
    
    from pathlib import Path 

    import json 
    

    if (name == 'todo') :


        path = Path()/'todo.json'
        with open(path,'r')  as file :


            dic =  json.load(file) 

    
    if (name == 'finance') : 

        path = Path()/'finance.json'


        with open(path,'r') as file :

            dic = json.load(file  ) 

        
    if (name == 'openorend') : 

        path = Path()/'openorend.json'


        with open(path,'r') as file :

            dic = json.load(file  ) 

        

        
    
    return dic 
    


    

def  save_todo() :

    ...

    

def edit_todo() :
    ...
def delete_todo(e,key) :

    import json 
    from pathlib import Path 
     

    path =  Path()/'todo.json'


    with open(path , 'r')  as file :


        dic  = json.load(file)


    del dic[default_key[0]][key]

    with open(path,'w') as file :


        json.dump(dic,file,indent=2) 
    
    show_todo()


def show_save_todo()  :

    from pathlib import Path 
    import json 

    path = Path()/'todo.json'


    with open(path,'r') as file :


        dic = json.load(file)
    



    save_show.content = Row(
        controls=[

            Container(width=300) , TextField( hint_text=' 7 as 8',width= 100 , height= 100 , bgcolor= colors.BLACK ,on_change= save_text_field_key) ,

            TextField( hint_text='Fazer café',width= 400 , height= 100 , bgcolor= colors.BLACK,on_change= save_text_field_todo_value)   , 

            ElevatedButton(text=' Save ',on_click= save_text_field_value)  ,
        ]
    )


    show_todo()  

def dropdowntodosave(e,key) :
    
    from datetime import  date
    from pathlib import Path 
    import json 


    dic = acess_json('openorend')    
    
    today = date.today() 

    
    key1 = str(today.strftime('%d') )   + str(today.strftime('%m') ) + str(today.strftime('%y') ) 

    
    isopen =  e.control.value  


    
    way = Path()/'openorend.json'  

    dic[key1][key] =  isopen

    with open(way,'w') as file : 

        json.dump(dic,file,indent=2)   

    
def show_todo() :
    from datetime  import time ,timedelta , datetime ,date
    import json 
    from pathlib import Path 

    

    dic = acess_json('todo')  


    today = date.today() 

    key = str(today.strftime('%d') )   + str(today.strftime('%m') ) + str(today.strftime('%y') ) 
        
    if default_key[0] == '':
     
        default_key[0] = key


    if dic.get(key,0) == 0 : 


        path = Path()/'todo.json'


        dic[default_key[0]]  =  {
            '7 as 8' :'fazer café'
        }


        with open(path,'w')  as file :


            json.dump(dic,file,indent=2 )

   
    if dic.get(default_key[0],0) == 0 : 


        path = Path()/'todo.json'


        dic[default_key[0]]  =  {

        }


        with open(path,'w')  as file :


            json.dump(dic,file,indent=2 )


    
    dic_2 = acess_json('finance')

    
    if dic_2.get(key,0) == 0 : 


        path = Path()/'finance.json'


        dic_2[key]  =  {
        "gasto":{ },
        "ganho":{},
        "investido":{}
    }


        with open(path,'w')  as file :


            json.dump(dic_2,file,indent=2 )



    
    current_todo =  dic[default_key[0]] 

    dic3 = acess_json('openorend')
    
    if dic3.get(key,0) == 0 : 


        path = Path()/'openorend.json'


        dic3[key]  =  {
    }

        with open(path,'w')  as file :


            json.dump(dic3,file,indent=2 )


    if dic3.get(default_key[0],0) == 0 : 


        path = Path()/'openorend.json'


        dic3[default_key[0]]  =  {
    }


        with open(path,'w')  as file :


            json.dump(dic3,file,indent=2 )


    current_todo =  dic[default_key[0]] 




    containers= []
    for todo in current_todo :
        
        conteudo =  current_todo[todo] 
        
      
        if   dic3[default_key[0]].get(todo,0) != 0 :
             dropdown_value =  dic3[default_key[0]][todo]

        else :
            dropdown_value ='erro'


       
        containers.append(
            Container(
                width=  400 , 
                height = 100 , 
                bgcolor = colors.TRANSPARENT , 


                content= Row(
                    controls=[
                        

                        Dropdown(
                            width= 100 , 
                            height= 100 , 
                            bgcolor= colors.WHITE10 ,
                            value= dropdown_value,
                            on_change = lambda e,key = todo:  dropdowntodosave(e,key) ,

                            options= [

                               
                               
                               dropdown.Option(text='End')  ,

                               dropdown.Option(text='open')


                            ]
                        ), 
                        Text(
                            value= f' {todo}  ',font_family= 'poppins',weight= FontWeight.BOLD , size= 15,color= colors.BLUE_100
                             
                             ),


                             Container(width= 20) ,

                                           Text(
                                               
                            value= f' {conteudo} ',font_family= 'poppins',weight= FontWeight.BOLD , size= 15

                             ),


                             ElevatedButton(
                                 text='Delete',
                                 on_click=  lambda e ,todo = todo :  delete_todo(e,todo)
                             )


                    ]
                )
            )
        )

    todo_show.content = Column(

        controls= containers

    )


    square_page.update() 


def  show_change_for_another_page() :

    ...

def end_of_time_anotations(e=0)  :
    from datetime import date , datetime , time  , timedelta


    today = date.today() 

    last_days =  today 
    counter_days_for_last_year = 0 


    while last_days.year == today.year :

        counter_days_for_last_year += 1 

        last_days += timedelta(1)



    
    
    end_week = today + timedelta(days=(6 - today.weekday()))
    
    end_week_days = (end_week.day - today.day)
    
  
    end_of_time_anotations_variable.content = Row(

        controls= [
                

                Container(width=200,
                         
                          height= 80 , 
                          bgcolor= colors.WHITE10 , 
                          border_radius= 4 ,  
                        alignment = alignment.center,

                          content= Text(
                              value = f" Endyear in {str(counter_days_for_last_year)} days",
                              font_family= 'poppins' ,
                              weight= FontWeight.BOLD , 

                          )
                          ) ,

                          
                Container(width=200,
                          
                          height= 80 ,
                          border_radius= 4 ,  
                          bgcolor= colors.WHITE10 , 
                        alignment = alignment.center,

                          content= Text(
                              value = f"End week in{str(end_week_days)} days",
                               font_family= 'poppins' ,
                              weight= FontWeight.BOLD , 
                          )
                          )

            
        ]
    )







def show_calendar(e=0)  :

    from datetime import date , datetime , time  , timedelta
    import json 

    from pathlib import Path 

    
    every_days = []

    today_key =  date.today()

    current_year = today_key.year 

    count_days =  datetime(current_year,1,1)

    while (count_days.year == current_year)  :

        
        count_days += timedelta(1) 
        
        if str(count_days.strftime('%Y') )+str(count_days.strftime('%m') )+str(count_days.strftime('%d') ) >= str(today_key.strftime('%Y') )+str(today_key.strftime('%m') )+str(today_key.strftime('%d') ) :  
           every_days.append(count_days)  

    


    containers = []

    if default_key[0] == '' :


         from datetime import date 
         today = date.today()
        
         key_default = str(today.strftime('%d') )   + str(today.strftime('%m') ) + str(today.strftime('%y') ) 

    else :

        key_default =  default_key[0]

    
    for day in every_days :
        
        current_key  = str(day.strftime('%d') )   + str(day.strftime('%m') ) + str(day.strftime('%y') ) 
        
        if  current_key == key_default:

            name = day.strftime("%a")  

            conteudo =  current_key
            containers.append(

                Container(
                    
                        width= 200 , 
                        height= 80 , 

                        bgcolor= colors.WHITE10 , 
                        border_radius= 4 , 
                        alignment= alignment.center,
                        on_click= lambda e , today  :  show_new_todo_of_other_day(e,today) ,
                        content = Text(
                            
                            value =  f'  {name}/ {conteudo[0:2]} / {conteudo[2:4]} '
                        )

                    
                )
            )

        else : 

              name = day.strftime("%a")

              conteudo = str(day.strftime('%m') )+str(day.strftime('%d') )+str(day.strftime('%Y') )
              containers.append(

                Container(
                    
                        width= 200 , 
                        height= 80 , 

                        bgcolor= colors.BLACK12, 
                        border_radius= 4 , 
                        alignment= alignment.center,
                        on_click= lambda e , day = day  :  show_new_todo_of_other_day(e,day) ,
                        content = Text(
                            value =  f' {name} / {conteudo[2:4]} / {conteudo[0:2]} '
                        )

                    
                )
            )
              
    
    
    
    
    calendar_of_year.content =  Row(
        scroll= ScrollMode.AUTO,
        controls= containers )   

    


    


def  show_main_page(e) :
 
    counter_of_todo() 
    show_calendar() 
    show_change_for_another_page()  
    show_todo()
    end_of_time_anotations() 
    show_save_todo()
  


    
    change_for_another_page = Container(

    width= 200 , 
    height= 80 , 
    
    border_radius=   8 , 

    bgcolor= colors.WHITE10, 

    alignment= alignment.center ,

    content= ElevatedButton(
        text='change page' , on_click= show_finance_page
    ) , )

    

    square_page.content = Column(
        scroll= ScrollMode.AUTO ,
        controls=[

            Container(
                content= Row(
                controls=[
                    

                    Text(
                        value='Make money' ,
                        weight = FontWeight.BOLD , 
                        font_family= 'heveltica'  , 
                        size= 21 ,
                    ) , 

                    Container(
                        width= 700 
                    ) , 

                    change_for_another_page , 


                ])
            ),

            calendar_of_year , 
            end_of_time_anotations_variable , 
            save_show,
            Container(

                width= 900  , 
                height = 500 , 
                padding= padding.only(left=300) , 
                bgcolor= colors.TRANSPARENT , 
                
                content=   todo_show ,


            ) , 
            counter_for_todo , 


        ]
        


    )







    
    square_page.update()  


def show_login_page() :


    square_page.content = Column(

        controls=[

           Container(

            width= 1200 , 
            height = 700 , 
            gradient=  SweepGradient(
                colors=[

                     colors.BLACK ,'#292401','#473E00','#292401','#1B1701', colors.BLACK 
                ]
            ),
            alignment= alignment.center,  
            content= Container(

                width= 400 , 
                height= 500 , 
                border_radius= 4 , 
    
                bgcolor= colors.WHITE10 , 
                content = Column(
                    controls=[

                        Text(value='Sign in ',font_family='heveltica', weight= FontWeight.BOLD,size=15 ),


                        TextField(
                            hint_text='Enter your name' ,
                            bgcolor= colors.WHITE10 , 
                            color= colors.BLACK ,
                            width = 400 , 
                            height= 100 , 

                        ) ,


                         TextField(
                            hint_text='password ' ,
                            bgcolor= colors.WHITE10 , 
                            color= colors.BLACK ,
                            width = 400 , 
                            height= 100 , 
                            
                        ) ,


                        Divider(

                        ) , 


                        Container( 
                            width= 300 , 
                            height= 50 , 
                            padding=padding.only(left=100), 
                            content = Text(
                            value='Forgot my password',color= colors.BLUE_200,  font_family= 'heveltica' , weight= FontWeight.BOLD , 


                        ),
                        
                        ),
 
                        Container(
                            width= 300 , 
                            height= 50 , 
                            padding= padding.only(left= 100) ,
                            on_click =  show_main_page, 
                            content=   Container(
                                width= 200 , 
                                height= 50 , 
                                bgcolor= colors.WHITE10,
                                border_radius = 4 ,
                                alignment= alignment.center,
                                content= Text(value='Sign in',font_family= 'poppins',weight= FontWeight.BOLD,size=12)  ,


                            )
                        ), 
                        
                        







                    ]
                )

               


                

                
            )           )

        ]
    )






def init_function() :

    
    show_login_page()