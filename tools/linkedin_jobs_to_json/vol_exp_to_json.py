import json

#Open news.html to scrape awards

with open('volunteer.txt') as fp:
    content  = fp.readlines()

all_ind_exp = []
print type(content)
for iii in range (0,len(content)/4):
    ind_exp = dict()
    ind_exp["position"]=content[iii*4]
    ind_exp["company"] = content[iii*4+1]
    ind_exp["date"] = content[iii*4+2] + ", "
    ind_exp["location"] = content[iii*4+3]
    ind_exp["caption"] = "insert caption"
    ind_exp["thumbnail"] = "/img/" + content [iii*4+1] + ".jpg"
    ind_exp_json = json.dumps(ind_exp)
    all_ind_exp.append(ind_exp)
print repr(all_ind_exp)
#while True:
#    link, end_link = get_next_award_link(page)
#     = dict()
#    if -1 == link:
#        break
#    else:
#        description, end_desc = get_next_award_description(page[end_link:])
#        page = page[end_link:]
#        links.append(link_json)
#        award["date"] = "2015-03-03 00:00:00"
#        award["title"] = description
#        award["location"] = "Insert location"
#        award["links"] = links 
#        award_json = json.dumps(award)
#        all_awards.append(award_json)

#print array of awards json
#print repr(all_awards)
