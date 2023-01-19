import colorgram

colors = colorgram.extract('image.jpg', 10)

first_color = colors[0]

rgb = first_color.rgb
hsl = first_color.hsl
proportion = first_color.proportion