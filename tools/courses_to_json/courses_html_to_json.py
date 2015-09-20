import json

#Open .html to scrape jobs 

with open('uw_courses.html') as fp:
    page  = fp.read()


#Given courses html, return first term 
#else return -1, -1
def get_next_term(page):
    end_term= page.find(')</em>')
    if -1 == end_term:
        return -1, -1
    start_term= page.rfind('">', end_term-20 , end_term)
    term_info=page[start_term+2:end_term+1]
    return term_info, end_term

#Given html for single course, return link
def get_course_link(page):
    start_link= page.find('<a href="')
    end_link=page.find('">')
    link=page[start_link+1:end_link]
    return link, end_link 

#given html for single course, return name
def get_course_name(page):
    start_name= page.find('</a>')
    end_name=page.find('<')
    name=page[start_name+1:end_name]
    return name, end_name

def extract_course_data(page):
    start_data = page.find('<td><span')
    end_data = page.find('</tr><tr>')
    data=page[start_data+1:end_data]
    return data, end_data

#given html for courses, return name and link
def get_course_link_name(page):
    #find the first course
    print extract_course_data(page)
    data = extract_course_data(page) 
    name = get_course_name(data)


    #loop for all course    


end_desc = 0



#empty list of terms 
all_terms = []

currrent_term, end_current_term = get_next_term(page)

next_term, end_next_term = get_next_term(page[end_current_term+4:])
course_html = page[:end_next_term-14]
print course_html

#while True:
#    print current term
# 
#    next_term, end_next_term = get_next_term(page)
#    if -1 == next_term:
#        break
#    else:
#        courses_html = page[:end_next_term+4]
#        #collect courses here
#
#    terms = dict()
#        print term
#        #description, end_desc = get_next_award_description(page[end_link:])
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

#print array of awards json
#print repr(all_awards)
