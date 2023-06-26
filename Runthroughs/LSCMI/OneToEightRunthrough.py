import utils
from Models.ExtractedModels.LSCMI.Section1to8.OneToEightOffenderInfoModel import OneToEightOffenderInfoModel
from Models.ExtractedModels.LSCMI.Section1to8.OneToEightOffenderCriminalHistoryModel import OneToEightOffenderCriminalHistoryModel
from Models.ExtractedModels.LSCMI.Section1to8.EducationEmploymentInfoModel import EducationEmploymentInfoModel
from Models.ExtractedModels.LSCMI.Section1to8.FamilyMarital import FamilyMarital
from Models.ExtractedModels.LSCMI.Section1to8.LeisureRecreation import LeisureRecreation
from Models.ExtractedModels.LSCMI.Section1to8.Companion import Companion
from Models.ExtractedModels.LSCMI.Section1to8.AlcoholDrugProblem import AlcoholDrugProblem
from Models.ExtractedModels.LSCMI.Section1to8.ProcriminalAttitude import ProcriminalAttitude
from Models.ExtractedModels.LSCMI.Section1to8.AntisocialPattern import AntisocialPattern

def one_to_eight(common_data):
    common_data.response = common_data.session.get(common_data.site + '/LSCMI/Section1/OneToEightOffenderInfo?assessmentId=' + utils.get_assessment_id(common_data.response))

    data = OneToEightOffenderInfoModel.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/OneToEightOffenderInfo', data=data, allow_redirects=True, verify=False)

    data = OneToEightOffenderCriminalHistoryModel.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/OffenderCriminalHistory', data=data, allow_redirects=True, verify=False)

    data = EducationEmploymentInfoModel.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/EducationEmploymentInfo', data=data, allow_redirects=True, verify=False)

    data = FamilyMarital.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/FamilyMarital', data=data, allow_redirects=True, verify=False)

    data = LeisureRecreation.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/LeisureRecreation', data=data, allow_redirects=True, verify=False)

    data = Companion.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/Companion', data=data, allow_redirects=True, verify=False)

    data = AlcoholDrugProblem.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/AlcoholDrugProblem', data=data, allow_redirects=True, verify=False)

    data = ProcriminalAttitude.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/ProcriminalAttitude', data=data, allow_redirects=True, verify=False)

    data = AntisocialPattern.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section1/AntisocialPattern', data=data, allow_redirects=True, verify=False)

    return common_data