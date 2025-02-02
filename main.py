import mysql.connector as ms
import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from random import *
db=ms.connect(host='localhost',user='root',password='root',database='agriconnect')
cur=db.cursor()
global go               #the status variable, base of entire agriconnect operations
global uid2             #creates the variable to avoid errors in other webpages
uid2=str(random())      #gives value to avoid errors in other webpages
go=0                    #gives value to avoid errors in other webpages

#Home page
def home():
    #Main heading
    st.header("Welcome to Agriconnect: Empowering Agriculture, Connecting Communities")
    
    #Content for display
    st.markdown("""

At Agriconnect, we cultivate more than crops; we cultivate connections. Our platform serves as the bridge between discerning consumers and dedicated farmers, fostering a community that values quality, sustainability, and the rich tapestry of agriculture. As you step into our digital fields, discover a world where every purchase makes a positive impact, supporting local farmers and ensuring access to fresh, responsibly grown products.

**Why Agriconnect?**

_Direct Access to Farmers:_ By eliminating intermediaries, Agriconnect provides a direct channel for consumers to connect with local farmers. This transparency ensures fair returns for farmers and guarantees that your produce is sourced from the roots.

_Diverse Agricultural Marketplace:_ Explore a diverse range of agricultural products, from farm-fresh fruits and vegetables to artisanal goods. Our curated marketplace celebrates the diversity of agriculture, offering you a one-stop destination for quality produce.

_Secure and Seamless Transactions:_ Shop with confidence. Agriconnect prioritizes the security of your transactions, offering a seamless and user-friendly experience. Your privacy and data protection are our top priorities.

**How It Works**

Discover the simplicity behind Agriconnect. Farmers easily join our network to showcase their products, and customers can effortlessly browse, purchase, and track orders. It's a seamless journey from farm to table, putting the power back into the hands of both producers and consumers.

**About Us**

Agriconnect is more than an e-commerce platform; it's a movement. Learn about our mission, values, and the dedicated team behind the scenes. We're committed to reshaping the agricultural landscape and empowering farmers to thrive in the digital age.

**Join Agriconnect Today**

Ready to be a part of a community that values quality, sustainability, and community connection? Sign up now to explore our marketplace, support local farmers, and enjoy the freshest produce delivered straight to your door.""")

#Sign up page
def register():
    global uid2# user id that runs all the user operations
    global s #name of user
    global password#password for later use
    
    #Main Header
    st.header('Register')

    #Registeration form
    with st.form('Register'):

        #A message to the user
        st.write('''Hello dear user and welcome to Agri-Connect. Please enter the necessary details and join our e-com system of customers and produces that promotes equity and welfare of the farmers' of our nation.''')
        options1=['Kerala']
        options2=['Thiruvananthapuram', 'Kollam', 'Alappuzha', 'Pathanamthitta', 'Kottayam', 'Idukki', 'Ernakulam', 'Thrissur', 'Palakkad', 'Malappuram', 'Kozhikode',' Wayanad',' Kannur','Kasaragod']
        name=st.text_input('Name',placeholder='Enter your name').strip()
        email=st.text_input('Email id',placeholder='eg:xyz@gmail.com').strip()
        phone= st.number_input("Phone no:",placeholder='90xxxxxx28', step=1, value=0, format="%d")
        state = st.selectbox("State:", options1)
        district=st.selectbox("Select your district:",options2).strip()
        town_village=st.text_input('Enter your town/village:').strip()
        address=st.text_input('Enter your address:').strip()
        status = st.selectbox("Select your status:", ["Producer", "Customer"])
        uid=st.text_input('Enter a suitable User ID ',placeholder='Max 8 characters').strip()
        passw=st.text_input('Enter a strong password ',placeholder='Max 8 characters',type='password').strip()
        passw2 = st.text_input('Confirm password', type='password').strip()
        sub = st.form_submit_button("Submit")   #Submit button

        #After form submission:
        if sub:
            if status=='Producer':
                pid=9001 #Producer ID 
                
                #To get max pid within producers
                q1='select max(id) from register where status="Producer"'
                cur.execute(q1)
                
                #Highest producer id
                maxp=cur.fetchall()[0][0]
                
                if type(maxp)==int:
                    pid=maxp+1
                else:
                    pid=9001
            elif status=='Customer':
                pid=4501 #Customer ID of same variable name to facilitate easy insert
                
                #To get max pid within customers
                q2='select max(id) from register where status="Customer"'#To get max pid within customers
                cur.execute(q2)
                
                #Highest customer ID
                maxc=cur.fetchall()[0][0]  
                
                #To check if there is any record with status customer
                if type(maxc)==int:
                    pid=maxc+1
                else:
                    pid=4501
                    
            #Query to insert values into the table register
            q3="""insert into register values({},'{}','{}',{},'{}','{}','{}','{}','{}','{}','{}')"""
            if name!='' and email!= ''and town_village != ''and uid !='' and passw!=''and passw2!= ''and  phone!=0 and len(str(phone))==10 and '@' in email and '.' in email and passw==passw2:
                try:
                    #format function to insert variable values
                    cur.execute(q3.format(pid,name,email,phone,state,district,town_village,status,uid,passw,address))
                    
                    #s & password are variables needed in the login page, uid2 is required everywhere
                    uid2=uid
                    password=passw
                    s=name
                    st.write('Registeration sucessful!!')
                    st.balloons
                        
                except (ms.IntegrityError,ms.DataError) as error:
                    
                    #Gets the error keyword generated by MySQL by the name err
                    err=str(error).split()[-1][10:-1:]
                    if err.lower()=='uid':
                        st.write('Duplicate user id')
                    elif err.lower()=='pass':
                        st.write('Duplicate password')
                    elif err.lower()=='email_id_2':
                        st.write('Duplicate email id')
                    elif err.lower()=='phone_no':
                        st.write('Duplicate phone no.')
                    else: 
                        st.write('You have already registered')
                        
                #Saves all the values if inserted without error
                db.commit()
                
            else:
                st.write('Please make sure all fields are filled properly and try again')
#Login Page
def login():
    global uid2
    global s
    global password
    
    #Main header
    st.header('Login')
    #Message to users
    st.write('If you are new here please sign-up')
    
    #Login form
    with st.form('login'):
        
        #Input from user
        uid1=st.text_input('User ID:')
        passw=st.text_input('Password:',type='password')
        sub = st.form_submit_button("Submit")#Submit button
        
        if sub:
            # to check if the user is already logged in
            if uid2==uid1 and password==passw:
                st.write('You are already logged in')
                
            else:
                uid2=uid1
                password=passw
                #Query to get name, uid and pass from the table register only if the uid and password match
                q4='Select name from register where uid=%s and pass=%s' 
                cur.execute(q4,(uid2,password))
                
                #Fetches the result
                user=cur.fetchall()
                
                #Empty list indicates no such registeration is present
                if user==[]:
                    st.write('Incorrect user id or password')
                else:
                    s=str(user[0][0])
                    st.write('Hello',s.title(),'Welcome to Agri-Connect. You may now begin to utilise our markets as per your requirements.')
        
#Orders
def order():
    #Main header
    st.header('Fresh Orders:')
    
    #Query to get status
    q5='Select status from register where uid="{}"'
    try:
        cur.execute(q5.format(uid2))
    except:
        pass
    #Initiates stat
    stat='' 
    
    try:
        stat=cur.fetchall()[0][0]
    except:
        pass
    #the status variable, base of entire agriconnect operations
    global go
    if stat=='Producer':
        go=1
    elif stat=='Customer':
        go=2
    elif stat=='Admin':
        go=3
    else:
        go=0
    
    #Query to get required attributes from table inventory
    q6='Select oid,product,100-stock from inventory where stock<50'
    cur.execute(q6)
    
    #Converted to list for dataframe conversion purposes
    res=list(cur.fetchall())
    
    #Datadrame created with columns defined by us
    df=pd.DataFrame(res,columns=['ID','Product name','Qty Required'])
    
    #Status check. This page is reserved only for admin and producer
    if go==1 or go==3:
        #hide_index removes auto generated index. width found by trial & error
        st.dataframe(df,width=755,hide_index=True)
        st.write('Please share your quotations to xyz@gmail.com')
    elif go==2:
        st.write('This page is for producers only. If you wish to be a producer please create another account')
    else:
        #Gives error message
        st.write('You have not logged in yet. Please log in. If you have not created an account yet, please sign up')

#Purchasing page      
def buy():
    global uid2
    
    #Main header
    st.header('Fresh products from your fellow farmers')
    
    #Query to select product details from table inventory
    q7='Select product, unit_price,image_url ,stock,oid from inventory'
    
    #go!=1 implies that normal viewers not logged in can view the products but not buy them
    if go!=1:    
        cur.execute(q7)
        res=cur.fetchall()      # fetches result to be used in the following loop
        keyy=1                  #key variable for making each slider unique
        for p in res:
            #html tag for displaying image with f mode to place variables within string quotes
            html=f'<div style="text-align: center; padding: 20px"><img src="{p[2]}" style="width: 250px; height: auto;border-radius: 20px;"></div><p><I>{p[0]}\n Rs.{p[1]} per kilo</I></p>'
            st.markdown(html,unsafe_allow_html=True)
            
            #Creates slider for getting integer values as qty with 1 as min value, stock value as max and key with a changing value as sliders must be unique
            qty=st.slider('Qty:',min_value=1,max_value=p[3],value=1,step=1,key=keyy)
            
            button_clicked = st.button(f"Add to cart:  {p[0]}", key=p[0], help=p[0])
            keyy+=1#updates key
            
            if button_clicked:
                #Queries defined for both cart and sale tables' update
                q8='insert into cart values(\'{}\',{},{})'
                q9='insert into sale values(\'{}\',{},{})'
                try:
                    cur.execute(q8.format(uid2,p[4],qty))# Inserting into cart uid, oid & qty
                    cur.execute(q9.format(uid2,p[4],qty))# Inserting into sale uid, oid & qty
                    db.commit()# saved to both tables
                    
                    #success and error gives a colour based answer
                    st.toast('Added to cart',icon='🛒')
                except:
                    st.write("You have not logged in. If you don't have an account yet, please sign up")
    elif go==1:
        st.write('This page is for customers only. If you wish to be a customer as well please create another account') 

#Your activity and cart
def cart():
    global uid2
    global go
    global s
    #Main header
    st.header('Your activity')
    
    #Sub Header
    st.subheader('Your account')
    try:
        #Query to get all details other than uid and password as a profile
        q10='select name,email_id,phone_no,state,district,town_vill,status,address from register where uid="{}"'.format(uid2)
        
        #Column 1 values
        nl=['Name: ', 'Email id: ', 'Mobile number: ', 'State: ', 'District: ', 'Town/Village: ', 'Status: ', 'Address: ']
        cur.execute(q10)
        res10=cur.fetchall()
        
        #Creates 2 columns
        col1,col2=st.columns(2)
        
        #variable for index value which starts at 0
        n=0
        
        #res[0] indicates a list of values
        for i in res10[0]: 
            with col1:
                st.write(nl[n])
                n+=1
            with col2:
                #n-1 as n is already incremented
                st.write(str(res10[0][n-1]))

        #Logout button with help attribute
        if st.button('Logout',help='logout'):
            uid2=str(random())#Sets uid2 to a random unknown value
            go=0              #go variable val determines the status of the person
            del(s)            #now when s will be invoked, error will be raised and except part will be activated
            st_autorefresh(interval=200, limit=2)
    except:
        st.write("You have not logged in. If you don't have an account yet, please sign up")
                
    #Sub Header
    st.subheader('Cart')
    try: 
        st.write('Hello',s, 'Here are your orders')
        
        #Query to get product, qty, total price wherever the foreign key oid of both tables are equal
        q11=' Select product, qty ,c.qty* i.unit_price from inventory i, cart c where i.oid=c.oid and c.uid="{}"'.format(uid2)
        
        #To clear cart for that user only
        q12='Delete from cart where uid="{}"'

        #Executing q9
        cur.execute(q11)
        res=cur.fetchall()
        
        #Dataframe creation with column names of our choice
        df=pd.DataFrame(res,columns=['Product','Qty','Price'])
        
        #Variable to calculate total cost
        sum=0
        for i in res:
            sum+=i[2]#Price
        #Displays dataframe with specified width and removes auto generated index    
        st.dataframe(df,width=755,hide_index=True)
        
        #Checks whether cart is empty or not
        if res!=[]:
            st.write('Click to proceed')
            if sum!=0:
                button='Grand Total: ' + str(sum)
                if st.button(button,help='Purchase'):
                    st.write('Payment sucessful!!')
                    st.balloons()
                    st_autorefresh(interval=200, limit=2)
                    #st.rerun()
                    for i in res:
                        q13='Update inventory set stock=stock-%s where product=%s'
                        cur.execute(q13,(i[1],i[0]))
                    cur.execute(q12.format(uid2))
                    db.commit()             #To make deletion permanent
        else:
            st.write('Your cart is empty. Please add your desired items if you wish to purchase them')
            
    except:
        st.write("You have not logged in. If you don't have an account yet, please sign up")