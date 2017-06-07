import web

urls = (
	'/', 'index'
	)

app = web.application(urls, globals())
render = web.template.render('')

class index:
	def GET(self):
		return render.login()

if __name__ == "__main__":
	app.run()
