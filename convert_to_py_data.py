# This program takes the contents of quick_convert.txt, which should be a bash cURL request, 
# converts it into a python dictionary and places the output into converted.txt

def main():
    ignore_list = ['CaseId', 'AssessmentId', 'LocalAuthorityId', 'submit', '__RequestVerificationToken']
    bool_dict = {'true': True, 'false': False}
    remove_data = False
    with open('quick_convert.txt', 'r') as f, open('converted.txt', 'w') as c:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(":", 1)
            if line[0] not in ignore_list:
                l2 = "\'\'"
                if not remove_data:
                    key = str.lower(line[1].strip())
                    l2 = (f"{bool_dict[key]}" if key in bool_dict else f"\'{line[1].strip()}\'")
                c.write(f"\'{line[0]}\': {l2},\n")

if __name__ == "__main__":
    main()