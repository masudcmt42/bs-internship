class Bangladesh():
    def capital(self):
        print('Dhaka is Capital of Bangladesh')
    def language(self):
        print('Bangla is the Mother language of Bangli peopel')
    def type(self):
        print('Bangladesh is Developing Country')
class USA:
    def capital(self):
        print('Washington is Capital of United State of america')
    def language(self):
        print('English is the Mother language of american peopel')
    def type(self):
        print('United state is Developed Country')  
ban=Bangladesh()
usa=USA()
for country in [ban,usa]:
    country.capital()
    country.language()
    country.type()

