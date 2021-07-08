row_length = float(input("Please enter the row length in feet: "))
end_post_space = float(input("Please enter the space taken up by the end post in feet: "))
space_between_vines = float(input("Please enter the space between each set of vines in feet: "))
grape_vines = row_length - 2.0*space_between_vines*end_post_space
print("The number of grapevines you can use is:", grape_vines)
