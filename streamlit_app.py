import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('breakfest menu')
streamlit.text('🥣 Omega 3 blueberry Oatmeal')
streamlit.text('🥗 Kale, spinach & Rocket smoothie')
streamlit.text('🐔 Hard boiled egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Create the repeatable code block (called function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruitvice_normalized
 
  back_from_function = get_fruityvice_data(fruit_choice)
  back_from_function
    
  streamlit.error()

streamlit.header("The fruit load list contains:")
#snowflake-related functions
def get_fruit_load_list():
 with my_cnx.cursor() as my_cur:
  my_cur.execute("select * from fruit_load_list")
 return my_cur.fetchall()
  
# add a button to load the fruit
if streamlit.button('get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  Streamlit.dataframe(my_data_rows) 



streamlit.dataframe(my_data_rows)


# adding new fruit
streamlit.header("What fruit you like to add?")
Add_my_fruit = streamlit.text_input('What fruit would you like information about?','Jackfruit')
streamlit.write('Thanks for adding', Add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
