from Models.ExtractedModels.LSCMI.Section10.ProgressRecord import ProgressRecord
from Models.ExtractedModels.LSCMI.Section10.ProgressRecordTwo import ProgressRecordTwo
from Models.ExtractedModels.LSCMI.Section10.ProgressRecordThree import ProgressRecordThree
from Models.ExtractedModels.LSCMI.Section10.ProgressRecordFour import ProgressRecordFour

def section10(common_data):

    data = ProgressRecord.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section10/ProgressRecord', data=data, allow_redirects=True, verify=False)

    data = ProgressRecordTwo.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section10/ProgressRecordTwo', data=data, allow_redirects=True, verify=False)

    data = ProgressRecordThree.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section10/ProgressRecordThree', data=data, allow_redirects=True, verify=False)

    data = ProgressRecordFour.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section10/ProgressRecordFour', data=data, allow_redirects=True, verify=False)