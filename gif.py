
import object_detector.file_io as file_io
import imageio

if __name__ == '__main__':
    images = []
    filenames = file_io.list_files("frames", "*.jpg")
#     for filename in filenames:
#         images.append(imageio.imread(filename))
#     imageio.mimsave('faces.gif', images)

    with imageio.get_writer('faces.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
 
    print "done"

