serve:
	hugo server --disableFastRender --noHTTPCache -D

build:
	rm -rf web
	hugo --minify

# deploy:
# 	rm -rf web
# 	hugo
# 	ssh root@csv.aeducar.es rm -rf info-libros-catedu/web
# 	scp -r web root@csv.aeducar.es:"/root/info-libros-catedu/"
# 	ssh -t root@csv.aeducar.es 'cd info-libros-catedu/ && docker-compose restart'