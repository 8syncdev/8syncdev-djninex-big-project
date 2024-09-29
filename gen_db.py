import subprocess


class TestDB:

    list_data = {
        'user': {
            'user': 'py manage.py loaddata ./dump/export/user.json',
            'instructor': 'py manage.py loaddata ./dump/export/instructor.json',
        },
        'course': {
            'lesson': 'py manage.py loaddata ./dump/export/lesson.json',
            'chapter': 'py manage.py loaddata ./dump/export/chapter.json',
            'course': 'py manage.py loaddata ./dump/export/course.json',
        }
    }

    list_run_cmd = [
        'py manage.py loaddata ./dump/export/user.json',
        'py manage.py loaddata ./dump/export/instructor.json',
        'py manage.py loaddata ./dump/export/lesson.json',
        'py manage.py loaddata ./dump/export/chapter.json',
        'py manage.py loaddata ./dump/export/course.json',
    ]

    @staticmethod
    def create_all_data():
        for cmd in TestDB.list_run_cmd:
            subprocess.run(cmd, shell=True)

    @staticmethod
    def create_one_data(path_cmd):
        subprocess.run(path_cmd, shell=True)

if __name__ == '__main__':
    TestDB.create_all_data()

