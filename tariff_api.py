import psycopg2
from collections import Counter
from osgeo import gdal_array
import os


def tariff(service,  N, dasht, mahur, kuhestan,  sakht, kheili_sakht):

	#72021211
	if service == '72021211':
		TF = N*(121930*dasht+143170*mahur+191810*kuhestan+238680*sakht+312940*kheili_sakht)/100

	#72021311		
	elif service=='72021311':
		TF = (area1*249390*dasht+area1*298850*mahur+area1*414530*kuhestan+area1*537140*sakht+area1*726340*kheili_sakht)/100

	#72021411
	elif  service=='72021411':
		TF = (area1*491250*dasht+area1*593950*mahur+area1*812050*kuhestan+area1*1107050*sakht+area1*1467890*kheili_sakht)/100
			
	#72021511
	elif map=='72021511':
		TF = (area1*2069490*dasht+area1*2525960*mahur+area1*3422110*kuhestan+area1*4885610*sakht+area1*6064230*kuhetan_kheili_sakht)/100

	#72031211_1			
	elif service == '72031211_1':             #if avg_area < 0.25:
		TF=N*425890
	elif  service == '72031211_2':    
		TF=N*3014200
	elif service == '72031211_3':   
		TF=N*235680
	elif service == '72031211_4':   
		TF=N*193610
	elif service == '72031211_5':   
		TF=N*171350

	#72031511
	elif service == '72031511_1':
		TF=N*2923390
	elif service == '72031511_2':
		TF=N*2300260
	elif service == '72031511_3':
		TF=N*1686340
	elif service == '72031511_4':
		TF=N*1377980
	elif service == '72031511_5':
		TF=N*746390
			

	#72041111
	elif service == '72041111':     #profile2000_100
		TF=N*(2977420*dasht+3323450*mahur+4331260*kuhestan+6110230*sakht+8639200*kheili_sakht)/100

	#72041211
	elif service == '72041211':  #profile2000_50'
		TN=N*(4565850*dasht+5515640*mahur+7616020*kuhestan+10907380*sakht+14310450*kheili_sakht)

	#72051111		
	elif service=='72051111':    #leveling3
		TF=(L1*662120*dasht+L1*725310*mahur+L1*807700*(kuhestan+sakht+kheili_sakht))/100


	#72051116
	elif service=='72051116':   #leveling1
		TF=(L1*1181170*dasht+L1*1566110*mahur+L1*2335970*(kuhestan+sakht+kheili_sakht))/100

			
			
	#72061111
	elif service=='72061111_1':  #static_GPS avg_L<=25 and avg_L>10
		TF=GPS_N*1367960
	elif service=='72061111_2':    #avg_L<10
		TF=GPS_N*1096260
	#else:
	#	TF='Please enter closer points'
			

	#72071211			
	elif service=='72071211_1':  #RTK N<=30
		TF=RTK_N*273690
	elif service=='720171211_2':                        # RTK_N>30 and RTK_N<=100
		TF=RTK_N*148580
	elif service== '720171211_3':                                         #RTK_N>100
		TF=RTK_N*86350
			


	return int(round((TF), -3))+1000000
	
	

def topo(ppp):
	ppp=str(ppp)
	pw = ppp.replace('LatLng', '')
	pw = pw.replace('(', '')



	pw = pw.replace(')', '')


	pw = ppp.replace('LatLng', '')
	pw = pw.replace('(', '')
	pw = pw.replace(')', '')
	pw=pw.split(',')
	n=0

	L1=[]


	n=0

	L1=[]
	for i in pw:
		if (n % 2)==0:
			try:
				L1.append( [  (float(pw[n+1])), (float(pw[n]))] )
			except:
				pass
					#L1.append( [  (float(pw[n])), (float(pw[n]))] )
		n+=1
	L1.append( [  (float(pw[1])), (float(pw[0]))] )






	f=open('price/sample.json', 'r')
	f=f.read()
	f=f.replace('LL', str(L1))



		#jsonpath = '/home/north/IT/NDVI/data/R10m/cropped/sample1'
		#Path(jsonpath).mkdir(parents=True, exist_ok=True)


	with open('price/jsonArchive/'+str(int(L1[0][0]*100000))+str(int(L1[0][1]*100000))+'.json', 'w') as ff:
		fff = ff.write(f)
				
	with open( 'price/json/'+str(int(L1[0][0]*100000))+str(int(L1[0][1]*100000))+'.json', 'w') as ff:
		fff = ff.write(f)
	N=len(L1[0])
	lat0=0
	lon0=0
	for i in range(N+1):
		lat0=lat0+L1[i][1]
		lon0=lon0+L1[i][0]
	lat = lat0/(N+1)
	lon = lon0/(N+1)


	os.system("gdalwarp -cutline {}  -crop_to_cutline -dstalpha {} {}".format('price/json/'+str(int(L1[0][0]*100000))+str(int(L1[0][1]*100000))+'.json', 'price/slope.tif', 'price/cropped/slope_cropped_'+str(int(L1[0][0]*100000))+str(int(L1[0][1]*100000))+'.tif'))

		#os.system(f"gdal_translate -stats {datapath + '/cropped/slope_cropped_'+str(int(L1[0][0]*100000))+str(int(L1[0][1]*100000))+'.tif srtm_46_05/slope_stats_float.tif")
		#os.system('gdalinfo srtm_46_05/slope_stats.tif')




		# Read raster data as numeric array from file
	try:
		rasterArray = gdal_array.LoadFile("{}".format('price/cropped/slope_cropped_'+str(int(L1[0][0]*100000))+str(int(L1[0][1]*100000))+'.tif'))
		band1 = rasterArray[0]
		dd = dict(Counter(band1.flatten()))
			#print(dd)
		n1=0
		n2=0
		n3=0
		n4=0
		n5=0

			
		# The 1rd band

		

		# Flatten the 2D array to 1D and count occurrences of each values
		# Then simple to get the stat for a pixel value in particular


		for i in dd.keys():
			if i>=0.0001 and i <3 :
				n1=n1+dd[i]
			elif i>=3 and i<7:
				n2=n2+dd[i]
			elif i>=7 and i<20:
				n3=n3+dd[i]
			elif i>=20 and i<60:
				n4=n4+dd[i]
			elif i>=60:
				n5=n5+dd[i]
					
		n=n1+n2+n3+n4+n5
		dasht = round(float(n1/n*100),2)
		mahur = round(float(n2/n*100),2)
		kuhestan = round(float(n3/n*100),2)
		kuhestan_sakht = round(float(n4/n*100),2)
		kuhestan_kheili_sakht = round(float(n5/n*100),2)
			


	except:
		dasht = 100
		mahur = 0
		kuhestan = 0
		kuhestan_sakht = 0
		kuhestan_kheili_sakht = 0
		
		#cur1 = conn.cursor()
		#cur1.execute('''SELECT * FROM public.taqsimat where st_within(st_GeomFromText('POINT({} {})', 4326), geom)'''.format(lon, lat))
		#row1 = cur1.fetchall()
		#zari1=row1[0][11]
	return(dasht, mahur, kuhestan, kuhestan_sakht, kuhestan_kheili_sakht, lat, lon)
		

