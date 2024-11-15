"""#create dataframe and a vizualisation
df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)

for tick in range(10):
    time.sleep(.5)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.add_rows(add_df)

st.button("Regenerate")"""
"""second_question = st.text_input('Enter your second question')
first_answers =st.text_input('Enter possible answers spaced by a comma')
third_question = st.text_input('Enter your third question')
first_answers =st.text_input('Enter possible answers spaced by a comma')
fourthed_question = st.text_input('Enter your fourthed question')
first_answers =st.text_input('Enter possible answers spaced by a comma')
fithed_question = st.text_input('Enter your fithed question')
first_answers =st.text_input('Enter possible answers spaced by a comma')"""

#use the button when the code is conditioned on button's value
animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'
