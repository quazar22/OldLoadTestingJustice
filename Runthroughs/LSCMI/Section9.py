from Models.ExtractedModels.LSCMI.Section9.PlanningSelection import PlanningSelection
from Models.ExtractedModels.LSCMI.Section9.ManagementPlan import ManagementPlan
from Models.ExtractedModels.LSCMI.Section9.InterventionPlan import InterventionPlan
from Models.ExtractedModels.LSCMI.Section9.InterventionPlanTwo import InterventionPlanTwo
from Models.ExtractedModels.LSCMI.Section9.InterventionPlanThree import InterventionPlanThree
from Models.ExtractedModels.LSCMI.Section9.InterventionPlanFour import InterventionPlanFour
from Models.ExtractedModels.LSCMI.Section9.AgreementNextReview import AgreementNextReview

def section9(common_data):

    data = PlanningSelection.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section9/PlanningSelection', data=data, allow_redirects=True, verify=False)

    data = ManagementPlan.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section9/ManagementPlan', data=data, allow_redirects=True, verify=False)

    data = InterventionPlan.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section9/InterventionPlan', data=data, allow_redirects=True, verify=False)

    data = InterventionPlanTwo.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section9/InterventionPlanTwo', data=data, allow_redirects=True, verify=False)

    data = InterventionPlanThree.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section9/InterventionPlanThree', data=data, allow_redirects=True, verify=False)

    data = InterventionPlanFour.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section9/InterventionPlanFour', data=data, allow_redirects=True, verify=False)

    data = AgreementNextReview.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section9/AgreementNextReview', data=data, allow_redirects=True, verify=False)

