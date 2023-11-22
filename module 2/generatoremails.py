emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	      'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	      'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

def get_email(emails):
    email_list = [f"{user}@{domain}" for domain in emails for user in emails[domain]]
    email_list.sort()

    for email in email_list:
        print(email)