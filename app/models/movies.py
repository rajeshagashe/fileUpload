from app.extensions import sql_db
import datetime

class MoviesData(sql_db.Model):
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    name = sql_db.Column(sql_db.Text, default = "")
    nn_popularity = sql_db.Column(sql_db.Float, default = "")
    director = sql_db.Column(sql_db.Text, default = "")
    genre = sql_db.Column(sql_db.Text, default = "")
    imdb_score = sql_db.Column(sql_db.Float, default = "")

    enabled = sql_db.Column(sql_db.Boolean, default = True)
    deleted = sql_db.Column(sql_db.Boolean, default = False)
    created_at = sql_db.Column(sql_db.DateTime, default=datetime.datetime.now)
    updated_at = sql_db.Column(sql_db.DateTime, default=datetime.datetime.now)

    def add(self):
        super().session.add(self)
    
    def commit(self):
        super().session.commit()
