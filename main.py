'''import streamlit as st
st.button("signin")
st.checkbox("java")
gender = st.radio("Gender",options=['male','female'])
st.error(gender)
st.success("ok")
st.info("shagda")
st.warning("warning")
st.text_input("enter your user name")
st.text_input("enter your password",type='password')'''

import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
def connectdb():
   conn= sqlite3.connect("mydb.db")
   return conn
def createTable():
   with connectdb() as conn:
      cur= conn.cursor()
      cur.exeute("CREATE TABLE IF NOT EXISTS student(name, text , password,roll int primary key, branch text)")
      conn.commit()
def addRecord(data):
   with connectdb() as conn:
      cur=conn.cursor()
      try:
        cur.execute("INSERT INTO student(name, password, roll, branch) VALUES(?,?,?,?)",data)
        conn.commit()
      except sqlite3.IntegrityError:
         st.error("student already registered")
def display():
   with connectdb() as conn:
      cur= conn.cursor()
      cur.execute("SELECT * FROM  student")
      result = cur.fetchall()
      return result


def signup():
   st.title("registration form")
   name =st.text_input("enter  name")
   password = st.text_input("enter the pssword here", type = 'password')
   repassword = st.text_input("retype your password", type='password')
   roll = st.number_input("enter the roll number", format="%0.0f")
   branch= st.selectbox("enter branch", options=['cse','aiml','csit'])
   if st.button('signin'):
      if password!=repassword:
         st.warning("password mismatch")
      else:addRecord((name.password,roll,branch))
      st.success("student registered!!!!")
with  st.sidebar:
   selected = option_menu("my app ", [ "signup",'display all record'])

   if selected == 'signup':
        signup()
   else:
      data = display()
      st.table(data)




