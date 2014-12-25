from app import db

class Additive(db.Model):
    index = db.Column(db.String, primary_key = True)
    additive_name = db.Column(db.String, index = True)
    description = db.Column(db.String, index = True)
    
    def __repr__(self):
        return unicode(self.additive_name)

class Foodstuff(db.Model):
    gtin = db.Column(db.Integer, primary_key = True)
    foodstuff_name = db.Column(db.String, index = True)
    trademark = db.Column(db.String, index = True)
    measure = db.Column(db.String, index = True)
    ingredients = db.Column(db.String, index = True)

    def __repr__(self):
        return '<Foodstuff %r>' % (self.foodstuff_name)
