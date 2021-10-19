from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello_world", __name__)
books_bp= Blueprint("book_list",__name__, url_prefix="/books")

class book():
    def __init__(self,id,title, description):
        self.id = id
        self.title = title
        self.description= description
    
    def to_json(self):
        return{
            "id": self.id,
            "name": self.title,
            "description": self.description
        }
    
        
books_lst=[
    book(1, "The attack of the guineapig", "A fantasy novel where guineapigs get mad."),
    book(2, "A squirrell's life", "Decoding the mistery of the wilderness") 
    ]

@books_bp.route("", methods=["GET"])
def handle_books():
    book_response = []
    for book in books_lst:
        book_response.append(book.to_json())
    return jsonify(book_response)

@books_bp.route("/<book_id>", methods=["GET"])
def get_book(book_id):
    book_id= int(book_id)
    for book in books_lst:
        return book.to_json()

@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    robot_greeting = "Hello world! uwu"
    return robot_greeting

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code", methods=["GET"])
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body

