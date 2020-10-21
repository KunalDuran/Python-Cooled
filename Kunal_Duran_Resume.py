#!python programmer Resume

class Resume:
    def __init__(self, name, home, age=23):
        self.name = name
        self.home = home
        self.age = age
        

    def education(self):
        """
        Economics Bachelor Student (2019 pass out)
        """
        return {'school': 'Kendriya vidhyalaya(commerce)', 'college': 'Rajasthan University (Economics)'}


    def experience(self):
        """Started Programming in october 2019"""
        import webbrowser
        webbrowser.open('https://github.com/KunalDuran')


    def projects(self):
        projects = {'Cricket Analysis Package':'https://pypi.org/project/cricsummary/',
                    'chatbot': 'https://github.com/KunalDuran/Python-projects-/tree/master/chatbot_with_python',
                    'webscraper':'https://youtu.be/KoYM91HZmPU',
                    'Flask API':'https://github.com/KunalDuran/Python-Cooled/tree/master/flasksql',
                    'Data Analysis':'https://github.com/KunalDuran/Python-projects-/tree/master/EDA',
                    'Machine Learning':'https://github.com/KunalDuran/ML_from_scratch'}

        print('Here are some of the projects I created \n: ')

        for key in projects:
            print(key, projects[key])


    def personal_info(self):
        linkedIn = 'https://www.linkedin.com/in/kunal-duran-35126310a/'
        instagram = 'https://www.instagram.com/kunalduran/' #Not so active
        return linkedIn, instagram


candidate = Resume("Kunal Duran", home='Jaipur, Rajasthan', age=23)
