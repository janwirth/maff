from skimage import data, io, filters

image = data.coins()
print('TYPE', type(image))
# ... or any other NumPy array!
edges = filters.sobel(image)
# io.imshow(edges)
# io.show()
