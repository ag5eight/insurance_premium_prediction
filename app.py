from joblib import load
import streamlit as st

# loading the trained model
pickle_in = open("insuranceclassifier.pkl", "rb")
classifier = load(pickle_in)

st.title("Hello World")
st.write("This is my first Streamlit app.")


# @st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(sex, age, bmi, children, smoker, region):

    # Pre-processing user input
    if sex == "Male":
        sex = 0
    else:
        sex = 1

    if smoker == "No":
        smoker = 0
    else:
        smoker = 1

    if region.lower() == "north":
        region_num = 0
    elif region.lower() == "east":
        region_num = 1
    elif region.lower() == "west":
        region_num = 2
    elif region.lower() == "south":
        region_num = 3

    # Making predictions
    prediction = classifier.predict([[sex, age, bmi, children, smoker, region_num]])

    return prediction


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Insurence Premium Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    sex = st.selectbox("Gender", ("Male", "Female"))
    age = st.number_input("Age")
    bmi = st.number_input("Bmi")
    children = st.number_input("Children")
    smoker = st.selectbox("Smoker", ("No", "Yes"))
    region = st.selectbox("Region", ("North", "East", "West", "South"))
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(sex, age, bmi, children, smoker, region)
        st.success("Your Premium is {}".format(result))


if __name__ == "__main__":
    main()
