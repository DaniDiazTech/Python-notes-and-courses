from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("simple_graphic.html") 
    fig = figure()

    total_val = int(input("How many values do you want to get a graphic ? >> ")) 
    x_val = list(range(total_val))
    y_val = []

    for x in x_val:
        val = int(input(f"Value y for {x} >> "))
        y_val.append(y_val)
    
    fig.line(x_val, y_val, line_width=2)
    show(fig)