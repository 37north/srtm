

from flask_restful import Resource, reqparse 
from price.tariff_api import tariff, topo

class Topo(Resource):
	
	def post(self):
		return {"dasht": 2}
		

	def get(self):
		return {"dasht": 3}
	

		
		'''
		parser = reqparse.RequestParser()
		parser.add_argument('ppp',
				type=str,
				required=True,
				help="This field cannot be left blank!"
				)

		parser.add_argument('N',
				type=float,
				required=True,
				help="This field cannot be left blank!"
				)
		parser.add_argument('service',
				type=str,
				required=True,
				help="This field cannot be left blank!"
				)


			
		data = parser.parse_args()
		topo_result = topo(data['ppp'])
		service = data['service']
		N = data['N']
		dasht = topo_result[0]
		mahur = topo_result[1]
		kuhestan = topo_result[2]
		sakht = topo_result[3]
		kheili_sakht = topo_result[4]
		lat = topo_result[5]
		lon = topo_result[6]
		'''
		
	
		price = tariff(service,  N, dasht, mahur, kuhestan,  sakht, kheili_sakht)
		return {'dasht': dasht, 'mahur':mahur, 'kuhestan': kuhestan, 'sakht': sakht, 'kheili_sakht': kheili_sakht, 'lat':lat, 'lon':lon, 'price':price, 'service': service}
		
		