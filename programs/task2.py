colors = [
{
"colors": "red",
"values": "#f00"
},
{
"colors": "green",
"values": "#0f0"
},
{
"colors": "blue",
"values": "#00f"
},
{
"colors": "cyan",
"values": "#0ff"
},
{
"colors": "magenta",
"values": "#f0f"
},
{
"colors": "yellow",
"values": "#ff0"
},
{
"colors": "black",
"values": "#000"
}
]

# if you want to check the type of object ...
print(type(colors))
print(isinstance(colors,list)) #True
print(isinstance(colors,dict)) #False


for item in colors:
    print(item['colors'] , item['values'])