from flask import Flask
from flask import jsonify 
from flask_restful import Api
from flask_json import FlaskJSON
from flask_cors import CORS, cross_origin


from api import support_jsonp
from api import Cliente
from api import ClienteList
from api import ChatBotSowa
from api import ChatBotTrainSowa
from api import ChatBotDBTest
from api import Ingles
from api import InglesList
from api import Categories
from api import CategoriesList
 
application = Flask(__name__, static_url_path='')
application.debug = True
application.config['PROPAGATE_EXCEPTIONS'] = True
CORS(application, supports_credentials=True)
json = FlaskJSON(application)



# then in your view
@application.route('/test', methods=['GET'])
@support_jsonp
def test():
       return '{"username":"username2017-08-05","email":"test@gmail.com","id":"1597"}'

@application.route('/')
def index():
	return application.send_static_file('index.html')






api = Api(application)
api.add_resource(ClienteList, '/api/cliente')
api.add_resource(Cliente, '/api/cliente/<id>')

api.add_resource(ChatBotSowa, '/api/chatbot')
api.add_resource(ChatBotTrainSowa, '/api/train')
api.add_resource(ChatBotDBTest, '/api/db')
api.add_resource(Ingles, '/api/ingles/phrases/<id>')
api.add_resource(InglesList, '/api/ingles/phrases')

api.add_resource(Categories, '/api/ingles/categories/<id>')
api.add_resource(CategoriesList, '/api/ingles/categories')







if __name__ == "__main__":
	application.run()