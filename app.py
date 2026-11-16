import streamlit as st

# 1. Create the web page title and description
st.title("Lean Process Efficiency Calculator")
st.write("Enter your process times below to calculate Process Cycle Efficiency (PCE).")

# 2. Create point-and-click number inputs for the user
value_add_time = st.number_input("Value-Add Process Time (minutes):", min_value=0.0, value=15.0)
total_lead_time = st.number_input("Total Lead Time (minutes):", min_value=0.1, value=120.0)

# 3. Create a clickable button
if st.button("Calculate Efficiency"):
    # Run the Lean math
    pce = (value_add_time / total_lead_time) * 100
    
    # Display the result cleanly on the page
    st.metric(label="Process Cycle Efficiency", value=f"{round(pce, 1)}%")
    
    # Give automated Lean feedback based on the result
    if pce < 10:
        st.warning("High waste detected! Over 90% of lead time is spent waiting.")
    else:
        st.success("Healthy flow! This process is moving efficiently.")
          
