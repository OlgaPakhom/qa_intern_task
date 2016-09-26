import requests
import unittest


class ApiTest(unittest.TestCase):
    main_url = 'http://qainterview.cogniance.com/candidates'
    name = "Super Tester3"
    position = "Intern2"
    user_id = 50

    def test_correct_respone(self):
        r = requests.get(self.main_url)
        assert (r.status_code == 200)

    def test_adding_user(self):
        r = requests.post(self.main_url, json={"name": self.name, "position": self.position})
        assert (r.status_code == 201)

    def test_incorrect_content_type(self):
        r = requests.post(self.main_url, {"name": self.name, "position": self.position})
        assert (r.status_code == 400)

    def test_deleting_user(self):
        r = requests.delete(self.main_url + str(self.user_id))
        assert (r.status_code == 200)

    def test_opening_user(self):
        r = requests.get(self.main_url + str(self.user_id))
        assert (r.status_code == 200)

if __name__ == '__main__':
    unittest.main()
"ashtan" 
