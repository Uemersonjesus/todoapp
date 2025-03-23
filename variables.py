
# here are the  main variables of project . 


from flet import*





square_page = Container(

    width=1200 ,
    height= 700 , 
    gradient = SweepGradient(
        colors=[

            colors.BLACK,'#1B1902','#494100','#1B1902','#1B1902',colors.BLACK 
        ]
    )
) 


drop_down_todo_current_value = ['']

calendar_of_year = Container(
    width= 1200,
    height=  200  , 
    bgcolor= colors.TRANSPARENT , 
)



end_of_time_anotations_variable = Container(


    width = 1200 , 
    height=  100 , 

    gradient= LinearGradient(
        colors=[

            colors.TRANSPARENT,colors.WHITE10,colors.BLACK12,colors.BLACK

        ]
    ) ,
    padding= padding.only(left=600) ,




)


change_for_another_page = Container(

    width= 200 , 
    height= 100 , 
    
    border_radius=   8 , 

    bgcolor= colors.BLACK , 

    alignment= alignment.center ,

    content= ElevatedButton(
        text='change page'
    ) ,


)


todo_show = Container(

    width= 1200 , 
    height= 300 , 
    bgcolor= colors.TRANSPARENT , 


)

default_key = ['']


save_show =  Container(

    width=  1200 , 
    height= 150, 
    bgcolor= colors.WHITE10 , 
    
    content = Row(
        controls=[

            Container(width=300) , TextField( hint_text=' 7 as 8',width= 100 , height= 100 , bgcolor= colors.BLACK ) ,

            TextField( hint_text='Fazer café',width= 400 , height= 100 , bgcolor= colors.BLACK )  
        ]
    )
)

todo_value = ['']
key_value =['']


#page variables  finance 


save_finance = Container(
    width= 1200 , 
    height= 200 , 
    bgcolor= colors.TRANSPARENT ,


)


total_of_finance = Container(
    width= 1200 , 
    height= 100 , 
    bgcolor= colors.TRANSPARENT , 
    padding= padding.only(left=200)  , 
)
date_of_finance = Container(
    width= 1200 , 
    height=  400 , 

    bgcolor= colors.BLACK12,
    padding= padding.only(left=200)

)

text_field_money_value = ['']

text_field_money_key = ['']

registers_in_finance_show = Container(
    width= 800, 
    height= 350 , 
    bgcolor= colors.TRANSPARENT , 
    alignment= alignment.center 

)

all_money_variable = Container(
    width= 1200,
    height= 100 , 

    bgcolor= colors.TRANSPARENT ,
    alignment= alignment.center , 


)

crud_of_money = Container(

    width= 1200 , 
    height= 100 , 
    bgcolor= colors.TRANSPARENT , 
    data= 'in'
)


kind_for_register_in_dic =  Dropdown(
    width= 100 , 
    height = 100 , 
    bgcolor= colors.WHITE10 ,
    
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
graph_circle_of_all_money = PieChart(

    width= 150 , 
    height= 150,

    center_space_radius=0,

)


graph_of_all_money = BarChart(

    width = 800  , 
    height= 400 , 

    bgcolor= colors.WHITE , 
    

    
    horizontal_grid_lines= ChartGridLines(
        color= colors.BLACK
    ),
    left_axis= ChartAxis(
        title= Text(value =' Total ') ,labels_size=40
    ),

    bottom_axis= ChartAxis(

        title= Text(value=' moths of year') , 
        labels= [

            ChartAxisLabel(

                label= Text(value='jan') ,
                value= 0

            ) ,

            
            ChartAxisLabel(

                label= Text(value='feb') ,
                value= 1

            ) ,

            
            ChartAxisLabel(

                label= Text(value=' mar') ,
                value=2 

            ),

            
            ChartAxisLabel(

                label= Text(value='apr') ,
                value=3 

            ),

            
            ChartAxisLabel(

                label= Text(value='may') ,
                value=4 

            ),

            
            ChartAxisLabel(

                label= Text(value='jun') ,
                value=5 

            ),

            
            ChartAxisLabel(

                label= Text(value='jul') ,
                value=6

            ),

            
            ChartAxisLabel(

                label= Text(value='aug') ,
                value=7 

            ),

            
            ChartAxisLabel(

                label= Text(value='sep') ,
                value=8 

            ),

            
            ChartAxisLabel(

                label= Text(value='oct') ,
                value=9

            ),
            
            ChartAxisLabel(

                label= Text(value='nov') ,
                value=10

            ),
             ChartAxisLabel(

                label= Text(value='dec') ,
                value = 11

            ),


        ]
        

    )


)


register_drop_down = ['']  


alert_dialog_drop_down =  Container(
    width= 300 , 
    height= 100, 
    border_radius = 6 , 
    bgcolor= colors.RED_600 , 
    visible= False 
)



counter_for_todo = Container(

    width=  1000 , 
    height=  300 , 
    bgcolor= colors.TRANSPARENT , 
    padding= padding.only(left=300)  , 
)
