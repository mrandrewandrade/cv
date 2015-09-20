import json

#Open .html to scrape jobs 

with open('jobs.txt') as fp:
    read_jobs  = fp.read()

##Given courses html, return first term 
##else return -1, -1
#def get_next_term(page):
#    end_term= page.find(')</em>')
#    if -1 == end_term:
#        return -1, -1
#    start_term= page.rfind('">', end_term-20 , end_term)
#    term_info=page[start_term+2:end_term+1]
#    return term_info, end_term
#
##Given award.html rturn description
#def get_next_award_description(page):
#    start_desc= page.find('>')
#    end_desc=page.find('<')
#    desciption=page[start_desc+1:end_desc]
#    return desciption, end_desc
#
#end_desc = 0
#
##empty list of terms 
#all_terms = []
#
#while True:
#    term, end_term = get_next_term(page)
#    terms = dict()
#    if -1 == term:
#        break
#    else:
#        print term
#        #description, end_desc = get_next_award_description(page[end_link:])
#        
#
#
#        #role, oganization, time
#        
#        #start seach 4 characters later
#        #this is to pass </em>
#        page = page[end_term+4:]
#        ##links has href and descrption
#        #links=[]
#        #link_json = dict()
#        #link_json["href"] = link
#        #link_json["desc"] = "Insert link type"
#        #links.append(link_json)
#        #award["date"] = "2015-03-03 00:00:00"
#        #award["title"] = description
#        #award["location"] = "Insert location"
#        #award["links"] = links 
#        #award_json = json.dumps(award)
#        #all_awards.append(award_json)
#
##print array of awards json
##print repr(all_awards)
