import requests

username = 'student1'
password = 'postgres123'

base_url = 'http://127.0.0.1:8000/api/'

r = requests.get(f'{base_url}courses/')
courses = r.json()


availables_courses =', '.join([course['title'] for course in courses])
print(f'availables courses:{availables_courses}')

for course in courses:
  course_id = course['id']
  course_title = course['title']
  r = requests.post(f'{base_url}courses/{course_id}/enroll/', auth=(username, password))

  if r.status_code == 200:
    print(f'successfully enrolled {course_title}')