from bs4 import BeautifulSoup
import requests
import time
def find_jobs():
    print("Put some skills that you are not familiar with:")
    unfamiliar_skill = input('>')
    print(f"Filtering out {unfamiliar_skill}")
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    #job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish_date = job.find('span', class_='sim-posted').span.text
        if 'few' in publish_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
    #         print(f'''
    #         Company Name: {company_name}
    #         Required Skills: {skills}''')
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f: #need to create a new empty folder beside there
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
