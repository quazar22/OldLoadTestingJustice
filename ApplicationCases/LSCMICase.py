from Runthroughs.LSCMI.OffenderHistoryRunthrough import offender_history
from Runthroughs.LSCMI.OneToEightRunthrough import one_to_eight
from Runthroughs.LSCMI.ElevenSections import eleven_sections

def begin_workflow(common_data):
    offender_history(common_data)
    one_to_eight(common_data)
    eleven_sections(common_data)
