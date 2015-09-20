import json

#Open news.html to scrape awards

with open('news.html') as fp:
    page  = fp.read()


#Given awards html, return first link
#else return -1, -1
def get_next_award_link(page):
    start_link= page.find('<a href=')
    if -1 == start_link:
        return -1, -1
    start_quote= page.find('"', start_link)
    end_quote= page.find('"', start_quote+1)
    url=page[start_quote+1:end_quote]
    return url, end_quote

#Given award.html rturn description
def get_next_award_description(page):
    start_desc= page.find('>')
    end_desc=page.find('<')
    desciption=page[start_desc+1:end_desc]
    return desciption, end_desc

end_desc = 0

#empty list of awards
all_awards = []

while True:
    link, end_link = get_next_award_link(page)
    award = dict()
    if -1 == link:
        break
    else:
        description, end_desc = get_next_award_description(page[end_link:])
        page = page[end_link:]
        #links has href and descrption
        links=[]
        link_json = dict()
        link_json["href"] = link
        link_json["desc"] = "Insert link type"
        links.append(link_json)
        award["date"] = "2015-03-03 00:00:00"
        award["title"] = description
        award["location"] = "Insert location"
        award["links"] = links 
        award_json = json.dumps(award)
        all_awards.append(award_json)

#print array of awards json
print repr(all_awards)
