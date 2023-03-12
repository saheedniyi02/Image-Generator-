from PIL import Image, ImageFont, ImageDraw




def generate_image(image_path,text,background_color=(0,0,0),text_color=(255,255,255),strip_color=(168, 50, 50)):
	width=1500
	height=1800
	image_background_color=background_color
	
	#background
	img = Image.new(mode="RGB", size=(width, height), color=image_background_color)
	drawer = ImageDraw.Draw(img)
	
	#add red strips
	
	#top strip 
	strip_margin_vert=int(height/25)
	strip_margin_hor=int(width/50)
	strip_thickness=int(height/100)
	top_strip_gap=int(width/15)
	strip_length=((width-(2*strip_margin_hor))/2)-top_strip_gap
	strip_color=strip_color
	
	#left strip
	drawer.rectangle([(strip_margin_hor, strip_margin_vert), (strip_length+strip_margin_hor, strip_thickness+strip_margin_vert)],fill=strip_color)
	
	#right strip
	drawer.rectangle([(width-strip_margin_hor-strip_length, strip_margin_vert), (width-strip_margin_hor, strip_thickness+strip_margin_vert)],fill=strip_color)
	
	top_bottom_strip_distance=200#int(height/6)
	#bottom strip        
	drawer.rectangle([(strip_margin_hor, strip_margin_vert+top_bottom_strip_distance+strip_thickness), (width-strip_margin_hor, strip_margin_vert+top_bottom_strip_distance+2*strip_thickness)],fill=strip_color)
	
	#double quote
	double_quote= '“”'
	double_quote_margin= int(top_strip_gap/5)
	double_quote_size=int(height/10)
	double_quote_color= text_color#(0,0,0)
	double_qoute_font = ImageFont.truetype("assets/Oswald-Bold.ttf", double_quote_size)
	drawer.text((strip_length+strip_margin_hor+double_quote_margin, 0), double_quote, font=double_qoute_font, fill=double_quote_color)
	
	#i will be there no matter what
	caption="I WILL BE THERE NO MATTER WHAT"
	caption_margin_top= int(top_bottom_strip_distance/5)
	caption_size=int(top_bottom_strip_distance/2)
	caption_color=double_quote_color
	caption_font = ImageFont.truetype("assets/Oswald-Bold.ttf", caption_size)
	drawer.text((strip_margin_hor, strip_margin_vert+strip_thickness+caption_margin_top), caption, font=caption_font, fill=caption_color)
	
	#text
	text=text.upper()
	text_margin_top= int(top_bottom_strip_distance/7)
	text_margin_hor= int(width/11)
	text_size=40
	text_color=double_quote_color
	text_font = ImageFont.truetype("assets/Nunito-SemiBoldItalic.ttf", text_size)
	
	drawer.text((text_margin_hor,strip_margin_vert+top_bottom_strip_distance+strip_thickness+text_margin_top), text, font=text_font, fill=text_color)
	
	#image
	attached_image=Image.open(image_path)
	attached_image=attached_image.resize((width, height -(strip_margin_vert+top_bottom_strip_distance+strip_thickness+text_margin_top+text_size+30)))
	img.paste(attached_image, (0, strip_margin_vert+top_bottom_strip_distance+strip_thickness+text_margin_top+text_size+30))
	
	return img
	
	
#pep
img_pep=generate_image("attached_images/pep.jpg","pep guardiola on winning the champions league for city", background_color=(0, 0, 0),strip_color=(82, 218, 242))	
img_pep.save("generated_images/pep.jpg")

#mbappe
img_mbappe=generate_image("attached_images/mbappe.jpeg","mbappe on leaving PSG to Madrid this season", background_color=(26, 43, 69))	
img_mbappe.save("generated_images/mbappe.jpg")

#haaland
img_haaland=generate_image("attached_images/Haaland.jpeg","Haaland on breaking the EPL goal scoring record", background_color=(26, 25, 24))	
img_haaland.save("generated_images/haaland.jpg")

#arteta
img_arteta=generate_image("attached_images/arteta.jpeg","Mikel arteta on Winning the EPL title this season",background_color=(255, 255, 255),text_color=(0,0,0))	
img_arteta.save("generated_images/arteta.jpg")


