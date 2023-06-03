from flet import *

# NOW GET IMAGE URL
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Mounth_Road_-_geograph.org.uk_-_115988.jpg/272px-Mounth_Road_-_geograph.org.uk_-_115988.jpg"

def main(page:Page):

	page.window_width = 250
	page.window_height = 500

	def runhover(e):
		# NOW I SET SCALE EFFECT WHEN YOU HOVER IMAGE
		# page.controls is i will get IMAGE WIDGET
		page.controls[0].controls[0].content.controls[0].scale = 1.5 if e.data == "true" else 1

		# AND IF YOU HOVER IMAGE . iMAGE WILL SCALE
		# AND SET OVERLAY BG TOO scale
		overlay.scale = 1.5 if e.data == "true" else 1
		
		page.update()	





	# NOW I WILL SET OVERLAY COLOR BG 
	overlay = Container(
		on_hover=runhover,
		bgcolor="black",
		height=200,
		opacity=0.2,
		width=250,
		scale=transform.Scale(1),
		animate_scale=animation.Animation(500,"bounce_out")
					
		)

	text_container = Container(
		margin=30,
		alignment=alignment.center,
		content=Text("my Overlay ",size=30,
			weight="bold",color="white"
			)
		)

	myimagecontainer = Container(
		# NOW I WILL SET OVERLAY BG BLACK
		alignment=alignment.center,
		content=Stack([
			overlay,
			text_container
			])
		)

	page.add(
		Column([
		Container(
			alignment=alignment.center,
			content=Stack([
				Image(
					src=url,
					fit="cover",
					height=200,
					width=250,
					# AND SET SCALE EFFECT
					# IF YOU HOVER
					scale=transform.Scale(1),
					animate_scale=animation.Animation(500,"bounce_out")
					),
				myimagecontainer
				])
			)
			])
		)
flet.app(target=main)
