# -*- coding: utf-8 -*-
"""
App created June 12th 2023
"""
import numpy as np
import streamlit as st

#
# GPOS sliders
#
st.title('GPOS - Geologic Probability of Success')

st.divider()

st.markdown("""This minimum example lists different parameters which can affect the _GPOS_.
            'Success is defined by discovering an economically _viable_ geothermal resource.""")

st.markdown("""The GPOS can comprise different probabilities which constitute to the overall probability of success.
            [van Lochem et al., 2021](https://www.earthdoc.org/content/papers/10.3997/2214-4609.202010694) for
            'instance lists multiple different probabilities:""")

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

st.markdown("""$$GPOS = P_{aq} \\times P_{perm} \\times P_{fluid} \\times P_{T} \\times P_{con}$$""")

st.divider()

st.markdown("""To get to a GPOS, the estimated percent confidences that the prospected reservoir meets the aforementioned 
criteria based on available data and a geological, conceptual model.""")


col1, col2, col3, col4, col5 = st.columns(5)  # Show sliders in 3 columns

Paq    = col1.slider('Presence', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='$P_{aq}$')
Pperm  = col2.slider('Permeability', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='$P_{perm}$')
Pfluid = col1.slider('Fluid', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='$P_{fluid}$')
Ptemp  = col2.slider('Temperature', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='$P_{temp}$')
Pcon   = col3.slider('Connectivity', value=50, min_value=1, max_value=100, step=1, format='%i%%', key='$P_{con}$')

st.markdown("""For an exploration well, only the first two estimates, $P_{aq}$ and $P_{perm}$ are important. Thus,
the others can be set to 100.""")

# Calculate GPOS in decimal percent
Paq    /= 100
Pperm  /= 100
Pfluid /= 100
Ptemp  /= 100
Pcon   /= 100

POSexpl = Paq * Pperm * Pfluid * Ptemp * Pcon


# GPOS as text output, rounded

st.write(f"""_{np.round(Paq * 100)} % presence \* {np.round(Pperm * 100)} % permeability \* 
{np.round(Pperm * 100)} % permeability \* {np.round(Ptemp * 100)} % temperature 
\* {np.round(Pcon * 100)} % cconnectivity = {np.round(POSexpl * 100)} % GPOS_""")
