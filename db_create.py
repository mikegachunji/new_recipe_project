from nrp_env import db
from nrp_env.models import Recipe, User
 
 
# drop all of the existing database tables
db.drop_all()
 
# create the database and the database table
db.create_all()
 
# insert recipe data
recipe1 = Recipe('Slow-Cooker Tacos', 'Delicious ground beef that has been simmering in taco seasoning and sauce.  Perfect with hard-shelled tortillas!')
recipe2 = Recipe('Hamburgers', 'Classic dish elevated with pretzel buns.')
recipe3 = Recipe('Mediterranean Chicken', 'Grilled chicken served with pitas, hummus, and sauted vegetables.')
db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)
 

# insert user data
user1 = User('mikegachunji@yahoo.com', 'mikegachunji')
user2 = User('kennedyfamilyrecipes@gmail.com', 'kennedyfamilyrecipes')
user3 = User('blaa@blaa.com', 'blaa')
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)


admin_user = User(email='mikegachunji@gmail.com', plaintext_password='awesomeness', role='admin')
db.session.add(admin_user)

db.session.commit()

