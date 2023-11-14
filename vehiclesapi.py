import falcon
import json
from wsgiref.simple_server import make_server
from models import User, Holding, Vehicle, Company
from data import records

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///VehicleMan.db", echo=True)


# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# session.add_all(records)
# with Session(engine) as session:
#     session.add(students)
# session.commit()

# rows = session.query(Students).all()

# students = []
# for row in rows:
#     students.append({"id": row.id, "name": row.name, "marks": row.marks})


class VehicleResource:
    def on_get(self, req, resp):
        rows = session.query(User).all()
        students = []
        for row in rows:
            students.append({"id": row.id, "name": row.name, "marks": row.marks})
            # print(students)
            resp.text = json.dumps(students)
            resp.status = falcon.HTTP_OK
            resp.content_type = falcon.MEDIA_JSON

#     def on_post(self, req, resp):
#         data = json.load(req.bounded_stream)
#         student = Students(id=data["id"], name=data["name"], marks=data["marks"])
#         session.add(student)
#         session.commit()
#         resp.text = "Student added successfully."
#         resp.status = falcon.HTTP_OK
#         resp.content_type = falcon.MEDIA_TEXT

#     def on_get_student(self, req, resp, id):
#         data = session.query(Students).filter(Students.id == id).first()
#         student = [{"id": data.id, "name": data.name, "marks": data.marks}]
#         resp.text = json.dumps(student)
#         resp.status = falcon.HTTP_OK
#         resp.content_type = falcon.MEDIA_JSON

#     def on_put_student(self, req, resp, id):
#         # student = students[id - 1]
#         # data = json.load(req.bounded_stream)

#         # student.update(data)
#         student = session.query(Students).filter(Students.id == id).first()
#         data = json.load(req.bounded_stream)
#         student.name = data["name"]
#         student.marks = data["marks"]
#         session.commit()
#         resp.text = "Student updated successfully."
#         resp.status = falcon.HTTP_OK
#         resp.content_type = falcon.MEDIA_JSON

    # def on_delete_student(self, req, resp, id):
    #     students.pop(id - 1)
    #     print(students)
    #     resp.text = json.dumps(students)
    #     resp.status = falcon.HTTP_OK
    #     resp.content_type = falcon.MEDIA_JSON


app = falcon.App()
app.add_route("/vehicles", class VehicleResource())
# app.add_route("/vehicles/{id:int}", class VehicleResource(), suffix="user")
# if __name__ == '__main__':
#     serve(app, host='0.0.0.0', port=8000)

if __name__ == "__main__":
    with make_server("", 8000, app) as httpd:
        print("Serving on port 8000...")
        # Serve until process is killed
        httpd.serve_forever()