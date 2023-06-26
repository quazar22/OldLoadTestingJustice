from Runthroughs.LSCMI.Section2 import section2
from .Section2 import section2
from .Section3to5 import section3to5
from .Section6 import section6
from .Section7 import section7
from .Section8 import section8
from .Section9 import section9
from .Section10 import section10
from .Section11 import section11

def eleven_sections(common_data):
    section2(common_data)
    section3to5(common_data)
    section6(common_data)
    section7(common_data)
    section8(common_data)
    section9(common_data)
    section10(common_data)
    section11(common_data)
    # print(common_data.response.text)