import matplotlib.pyplot as plt
import matplotlib.image as img 

start = time.time()
class PyPersonGraph():
    def __init__(self,
                    first_rate = 10,
                    dimensions=(10,10), 
                    first_color="red",
                    second_color="green",
                    title ="HOLA HOLA"):

        self.first_rate = first_rate    
        self.dimensions = dimensions
        self.first_color = first_color
        self.second_color = second_color
        self.title = title


    def show(self):
        fig, axs = plt.subplots(self.dimensions[0], 
                                self.dimensions[1],
                                sharex='col', sharey='row',
                                gridspec_kw={'hspace': .001,
                                'wspace': .001})
        fig.suptitle(self.title, fontsize=16,fontweight ="bold")
        
        data1 = img.imread("personimages/person_"+ self.first_color +".jpg") ## (1281, 820, 3) data.shape
        data2 = img.imread("personimages/person_"+ self.second_color +".jpg") ## (1281, 820, 3) data.shape
        
        images = []

        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                if self.first_rate > 0:
                    images.append(axs[i, j].imshow(data1))
                    self.first_rate -= 1
                else:
                    images.append(axs[i, j].imshow(data2))
                axs[i, j].set_axis_off()
        plt.show()


#showing = PyPersonGraph(dimensions=(10,10),
#                    first_rate = 10, 
#                    first_color = "green", 
#                    second_color  = "red",
#                    title =  "Hello bro")
#showing.show()
