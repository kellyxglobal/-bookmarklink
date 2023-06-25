from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from flask import Blueprint, request
from flask.json import jsonify
import validators
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.database import Bookmark, db
from flasgger import swag_from

#Blueprint for users' authentication
bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")

#Tell a user that his bookmark data got submitted succesfully
"""
@bookmarks.get('/')
def get_all():
    return {"bokmarks":[]}
"""

#Creating an end point that handles two methods via route
@bookmarks.route('/', methods=['POST', 'GET'])
@jwt_required()
def handle_bookmarks():
    current_user = get_jwt_identity()
    #check the request method from the user
    if request.method == 'POST':

        body=request.get_json().get('body', '')
        url=request.get_json().get('url', '')

        if not validators.url(url):
            return jsonify({
                'error': 'Enter a valid url'
            }), HTTP_400_BAD_REQUEST
        
        if Bookmark.query.filter_by(url=url).first():
            return jsonify({
                'error': 'URL already exists'
            }), HTTP_409_CONFLICT
        
        bookmark=Bookmark(url=url, body=body, user_id=current_user)
        db.session.add(bookmark)
        db.session.commit()

        return jsonify({

            'id': bookmark.id,
            'url': bookmark.url,
            'short_url': bookmark.short_url,
            'visit': bookmark.visits,
            'body': bookmark.body,
            'created_at': bookmark.created_at,
            'updated_at': bookmark.updated_at,
        }), HTTP_201_CREATED
    
    else:
        #Paginating and retrieving  data
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)

        bookmarks = Bookmark.query.filter_by(user_id=current_user).paginate(page=page, per_page=per_page)


        data=[]

        for bookmark in bookmarks.items:
            data.append({
                'id': bookmark.id,
                'url': bookmark.url,
                'short_url': bookmark.short_url,
                'visit': bookmark.visits,
                'body': bookmark.body,
                'created_at': bookmark.created_at,
                'updated_at': bookmark.updated_at,
            })

            meta = {
                "page": bookmarks.page,
                'pages': bookmarks.pages,
                'total': bookmarks.total,
                'prev_page': bookmarks.prev_num,
                'next_page': bookmarks.next_num,
                'has_next': bookmarks.has_next,
                'has_prev': bookmarks.has_prev,
                
            }

        return jsonify({'data': data, "meta": meta}), HTTP_200_OK

#Creating a page that can retrieve single item.
@bookmarks.get("/<int:id>")
@jwt_required()
def get_bookmark(id):
    current_user = get_jwt_identity()

    bookmark = Bookmark.query.filter_by(user_id=current_user, id=id).first()

    if not bookmark:
        return jsonify({'message':'Item not found'}), HTTP_404_NOT_FOUND
    
    return jsonify({
            'id': bookmark.id,
            'url': bookmark.url,
            'short_url': bookmark.short_url,
            'visit': bookmark.visits,
            'body': bookmark.body,
            'created_at': bookmark.created_at,
            'updated_at': bookmark.updated_at,
        }), HTTP_200_OK 

#Editing an item and updating the single item. via PUT or PATCH Method
#http://127.0.0.1:8000/api/v1/bookmarks/19
@bookmarks.put('/<int:id>')
@bookmarks.patch('/<int:id>')
@jwt_required()
def editbookmark(id):
    current_user = get_jwt_identity()

    bookmark = Bookmark.query.filter_by(user_id=current_user, id=id).first()

    if not bookmark:
        return jsonify({'message': 'Item not found'}), HTTP_404_NOT_FOUND

    body=request.get_json().get('body', '')
    url=request.get_json().get('url', '')
 
    if not validators.url(url):
        return jsonify({
            'error': 'Enter a valid url'
        }), HTTP_400_BAD_REQUEST
    
    bookmark.url = url
    bookmark.body = body

    db.session.commit()

    return jsonify({

            'id': bookmark.id,
            'url': bookmark.url,
            'short_url': bookmark.short_url,
            'visit': bookmark.visits,
            'body': bookmark.body,
            'created_at': bookmark.created_at,
            'updated_at': bookmark.updated_at,
        }), HTTP_200_OK


@bookmarks.get("/stats")
@swag_from("./docs/bookmarks/stats.yaml")
@jwt_required()
def get_stats():
    current_user = get_jwt_identity()

    data=[]

    items = Bookmark.query.filter_by(user_id=current_user).all()

    for item in items:
        new_link = {
            'visits': item.visits,
            'url': item.url,
            'id': item.id,
            'short_url': item.short_url,
        }

        data.append(new_link)

    return jsonify({'data': data}), HTTP_200_OK


#Deleting a retrieved single item via delete method
@bookmarks.delete("/<int:id>")
@jwt_required()
def delete_bookmark(id):
    current_user = get_jwt_identity()

    bookmark = Bookmark.query.filter_by(user_id=current_user, id=id).first()

    if not bookmark:
        return jsonify({'message':'Item not found'}), HTTP_404_NOT_FOUND
    
    db.session.delete(bookmark)
    db.session.commit()

    return jsonify({}), HTTP_204_NO_CONTENT