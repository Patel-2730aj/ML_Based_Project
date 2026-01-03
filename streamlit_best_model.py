import pickle
from PIL import Image
import streamlit as st
 
 # Load the image and set up the app title
img1 = Image.open("bank1.png")
st.image(img1, use_column_width=False)

 
# loading the trained model
pickle_in = open('bestmodelxgboost.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
# defining the function which will make the prediction using the data which the user inputs 

def prediction(loan_amnt, term, int_rate, installment, grade, 
        home_ownership, annual_inc, verification_status, 
        purpose, dti, earliest_cr_line, 
        pub_rec, revol_bal, revol_util, total_acc, 
        mort_acc, postal_code):   
   

     #verification_status
    if verification_status == "Not Verified":
        verification_status = 0
    elif verification_status == "Source Verified":
        verification_status = 1
    elif verification_status == "Verified":
        verification_status = 2
    else :
        verification_status = 2
        
    #purpose 
    if purpose == "vacation":
        purpose = 0
    elif purpose == "debt_consolidation":
        purpose = 1
    elif purpose == "credit_card":
        purpose = 2
    elif purpose == "home_improvement":
        purpose = 3
    elif purpose == "small_business":
        purpose = 4
    elif purpose == "major_purchase":
        purpose = 5
    elif purpose == "other":
        purpose = 6
    elif purpose == "medical":
        purpose = 7
    elif purpose == "wedding":
        purpose = 8
    elif purpose == "car":
        purpose = 9
    elif purpose == "moving":
        purpose = 10
    elif purpose == "house":
        purpose = 11
    elif purpose == "educational":
        purpose = 12
    elif purpose == "renewable_energy":
        purpose = 13
    else :
        purpose = 2

    #home_ownership
    if home_ownership == "RENT":
        home_ownership = 0
    elif home_ownership == "MORTGAGE":
        home_ownership = 1
    elif home_ownership == "OWN":
        home_ownership = 2
    elif home_ownership == "OTHER":
        home_ownership = 3
    else:
        home_ownership=3
 
    # Making predictions 
    prediction = classifier.predict( 
        [[loan_amnt, term, int_rate, installment, grade, 
        home_ownership, annual_inc, verification_status, 
        purpose, dti, earliest_cr_line, 
        pub_rec, revol_bal, revol_util, total_acc, 
        mort_acc, postal_code]])
     
    if prediction == 0:
        pred ='Unfortunately the loan is likely to be rejected'
    else:
        pred ='Congratulations the loan is likely to be approved.'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
      
    # following lines create boxes in which user can enter data required to make prediction 
    loan_amnt = st.number_input("Loan Amount", min_value=1000, max_value=5000000, value=10000)
    term = st.selectbox("Term (in months)", [36,60])
    int_rate = st.number_input("Interest Rate", min_value=5.0, max_value=40.0, value=10.0)
    installment = st.number_input("Installment", min_value=10.0, max_value=2000.0, value=200.0)
    grade = st.number_input("Grade (1 to 7)", min_value=1, max_value=7, value=1)
    home_ownership = st.number_input("Home Ownership (1: Own, 2: Mortgage, 3: Rent)", min_value=1, max_value=3, value=2)
    annual_inc = st.number_input("Annual Income", min_value=1000.0, max_value=1000000.0, value=50000.0)
    verification_status = st.number_input("Verification Status (1: Verified, 0: Not Verified)", min_value=0, max_value=1, value=1)
    purpose = st.number_input("Purpose (1: Debt consolidation, 2: Credit card, ...)", min_value=1, max_value=14, value=1)
    dti = st.number_input("Debt-to-Income Ratio (DTI)", min_value=0.0, max_value=10000.0, value=10.0)
    earliest_cr_line = st.number_input("Earliest Credit Line (Year)", min_value=1900, max_value=2024, value=2000)
    pub_rec = st.number_input("Public Records", min_value=0, max_value=86, value=0)
    revol_bal = st.number_input("Revolving Balance", min_value=0.0, max_value=3500000.0, value=1000.0)
    revol_util = st.number_input("Revolving Utilization Rate (%)", min_value=0.0, max_value=100.0, value=30.0)
    total_acc = st.number_input("Total Accounts", min_value=2, max_value=151, value=10)
    mort_acc = st.number_input("Mortgage Accounts", min_value=0, max_value=34, value=1)
    postal_code = st.number_input("Postal Code")
    
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(loan_amnt, term, int_rate, installment, grade, 
        home_ownership, annual_inc, verification_status, 
        purpose, dti, earliest_cr_line, 
        pub_rec, revol_bal, revol_util, total_acc, 
        mort_acc, postal_code) 
        st.success(result)
        
     
if __name__=='__main__': 
    main()
