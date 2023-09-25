# -*- coding: utf-8 -*-
"""
App created June 12th 2023
"""
import numpy as np
import streamlit as st


st.set_page_config(layout="wide")
if "P_aq" not in st.session_state:
    st.session_state.disabled = False
if "P_perm" not in st.session_state:
    st.session_state.disabled_perm = False
if "P_fluid" not in st.session_state:
    st.session_state.disabled_fluid = False
if "P_temp" not in st.session_state:
    st.session_state.disabled_temp = False
if "P_con" not in st.session_state:
    st.session_state.disabled_con = False

#
# GPOS sliders
#
st.image("https://tool.energy4climate.nrw/branchenfuehrer-erneuerbare/img/companies/373/online.jpg", width=300)

st.title('GPOS - Geologic Probability of Success')

st.divider()

st.markdown("""This minimum example lists different parameters which can affect the _GPOS_.
            Success is defined by discovering an economically _viable_ geothermal resource.""")

st.markdown("""The GPOS can comprise different probabilities which constitute to the overall probability of success.
            [van Lochem et al., 2021](https://www.earthdoc.org/content/papers/10.3997/2214-4609.202010694), for
            instance, lists multiple different probabilities:""")

st.markdown("""
| Element  | Short Description  | Main Risks  |  
|---|---|---|  
| $P_{aq}$  | Chance that the target aquifer is present  | Faulting / Erosion / Facies change  |  
| $P_{perm}$   | Chance that the system is sufficiently permeable  | Compaction / Diagenesis / No Karst or Fractures  |  
| $P_{fluid}$  | Chance that the fluid present is compatible for geothermal power extraction  | Hydrocarbons / Scaling |  
| $P_{T}$  | Chance that the fluid temperature meets requirement  | low geothermal gradient  |  
| $P_{con}$  | Chance that two doublet-boreholes have a hydraulic connection  | Sealing fault / Truncation  |    
""")

st.divider()


col1, col2, col3, col4 = st.columns([0.5,1,1,2])

with col1:
    check_box_presence      = st.checkbox("Presence", key="disabled_aq")
    check_box_permeability  = st.checkbox("Permeability", key="disabled_perm")
    check_box_fluid         = st.checkbox("Fluid", key="disabled_fluid")
    check_box_temperature   = st.checkbox("Temperature", key="disabled_temp")
    check_box_connectivity  = st.checkbox("Connectivity", key="disabled_con")

with col2:
    Paq    = st.slider('Presence', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_aq',
                       disabled=st.session_state.disabled_aq)
    Pperm  = st.slider('Permeability', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_perm',
                       disabled=st.session_state.disabled_perm)
    Pfluid = st.slider('Fluid', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_fluid',
                       disabled=st.session_state.disabled_fluid)
    Ptemp  = st.slider('Temperature', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_temp',
                       disabled=st.session_state.disabled_temp)
    Pcon   = st.slider('Connectivity', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_con',
                       disabled=st.session_state.disabled_con)

with col3:
    sel_presence        = st.selectbox("Presence", ("High", "Moderate", "Low"))
    sel_permeability    = st.selectbox("Permeability", ("High", "Moderate", "Low"))
    sel_fluid           = st.selectbox("Fluid", ("High", "Moderate", "Low"))
    sel_temperature     = st.selectbox("Temperature", ("High", "Moderate", "Low"))
    sel_connectivity    = st.selectbox("Connectivity", ("High", "Moderate", "Low"))


with col4:
    st.image(r"https://raw.githubusercontent.com/Japhiolite/gpos/dev_dgk/imgs/Rose_risk.PNG")
    st.text("Chance Matrix after Rose (2001)")



st.title("Check Boxes")

check_box_1 = st.checkbox("Partial ratio")

check_box_2 = st.checkbox("Token sort ratio", value=True)

st.title("Sliders")

if check_box_1 == True:

    Partial_ratio_slider = st.slider('partial ratio values')

if check_box_2 == True:

    Token_sort_slider = st.slider('token sort ratio values')

#tab1, tab2 = st.tabs(["Exploration", "Development"])

#with tab1:
#    st.markdown("""$$GPOS = P_{aq} \\times P_{perm}$$""")

#    st.divider()

#    st.markdown("""To get to a GPOS, the estimated percent confidences that the prospected reservoir meets the
#    aforementioned criteria based on available data and a geological, conceptual model.""")

#    col1e, col2e = st.columns(2)  # Show sliders in 3 columns

#    Paq_ex = col1e.slider('Presence', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='paq_ex')
#    Pperm_ex = col2e.slider('Permeability', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='pperm_ex')

#    Paq_ex /= 100
#    Pperm_ex /= 100

#    POSexpl_ex = Paq_ex * Pperm_ex

#    st.write(f"""## {np.round(POSexpl_ex * 100, 2)} % GPOS""")

#with tab2:
#    st.markdown("""$$GPOS = P_{aq} \\times P_{perm} \\times P_{fluid} \\times P_{T} \\times P_{con}$$""")

#    st.divider()

#    st.markdown("""To get to a GPOS, the estimated percent confidences that the prospected reservoir meets the
#    aforementioned criteria based on available data and a geological, conceptual model.""")

#    col1, col2, col3, col4, col5 = st.columns(5)  # Show sliders in 3 columns

#    Paq    = col1.slider('Presence', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_aq')
#    Pperm  = col2.slider('Permeability', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_perm')
#    Pfluid = col3.slider('Fluid', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_fluid')
#    Ptemp  = col4.slider('Temperature', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_temp')
#    Pcon   = col5.slider('Connectivity', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='P_con')

#    st.markdown("""For an exploration well, only the first two estimates, $P_{aq}$ and $P_{perm}$ are important.
#    Please select the tab 'Exploration'. """)

#    # Calculate GPOS in decimal percent
#    Paq    /= 100
#    Pperm  /= 100
#    Pfluid /= 100
#    Ptemp  /= 100
#    Pcon   /= 100

#    POSexpl = Paq * Pperm * Pfluid * Ptemp * Pcon


#    # GPOS as text output, rounded
#    st.write(f"""## {np.round(POSexpl * 100,2)} % GPOS""")


st.markdown("""### References:
Niederau, J., Ritzmann, O., Jüstel, A., Wellmann, F., & Kettermann, M. (2023, June). Green field exploration in the 
Aachen-Weisweiler region, Germany: Constraints and concepts for uncertainty and risk assessment. 
_In 84th EAGE Annual Conference & Exhibition_ (Vol. 2023, No. 1, pp. 1-5). _European Association of Geoscientists 
& Engineers._

Rose, P. R. (2001). Risk analysis and management of petroleum exploration ventures (Vol. 12). 
_Tulsa, OK: American Association of Petroleum Geologists._

Van Lochem, H. (2021, October). GPOS Evaluation For Geothermal Projects in the Netherlands. 
_In 82nd EAGE Annual Conference & Exhibition_ (Vol. 2021, No. 1, pp. 1-5). _EAGE Publications BV_.""")

#st.write(f"""_{np.round(Paq * 100)} % presence \* {np.round(Pperm * 100)} % permeability \*
#{np.round(Pperm * 100)} % permeability \* {np.round(Ptemp * 100)} % temperature
#\* {np.round(Pcon * 100)} % cconnectivity = {np.round(POSexpl * 100)} % GPOS_""")
