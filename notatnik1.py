class User:
    def __init__(self, name, surname, location, posts):
        self.name=name
        self.surname=surname
        self.location=location
        self.posts=posts
        self.coordinates = self.get_coordinates()

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        return [latitude, longitude]

user_1 = User(name = "Krzysztof", surname = "Ofiara", location="Warszawa", posts=[5])

print(user_1.name)
print(user_1.coordinates)
