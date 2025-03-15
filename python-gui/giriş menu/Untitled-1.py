"""# Shape arayüzü
class Shape:
    def draw(self):
        pass

    def set_color(self, color):
        self.color = color


# ShapeWithSize arayüzü
class ShapeWithSize:  # Shape'ten türetildi
    def set_size(self, size):
        self.size = size


# Circle sınıfı, sadece Shape arayüzünü uygular
class Circle(Shape):
    def draw(self):
        print(f"Drawing a circle with color {self.color}")


# Square sınıfı, hem Shape hem ShapeWithSize arayüzünü uygular
class Square(ShapeWithSize):
    def draw(self):
        print(f"Drawing a square with color {self.color} and size {self.size}")


def main():
    # Circle örneği
    circle = Circle()
    circle.set_color("red")
    circle.draw()

    # Square örneği
    square = Square()
    square.set_color("blue")  # Rengi ayarladık
    square.set_size(20)       # Boyutu ayarladık
    square.draw()


if __name__ == "__main__":
    main()

"""
#------------------------------------------------------------------------------------------------------------------

# Shape sınıfı
class Shape:
    def draw(self, shape_interface):
        shape_interface.draw()


# ShapeInterface arayüzü
class ShapeInterface:
    def draw(self):
        pass


# Circle sınıfı
class Circle(Shape):
    def draw(self, shape_interface):
        shape_interface.circle_draw()

    

    def circle_draw(self):
        print("Drawing a circle")


# Square sınıfı
class Square(Shape):
    def draw(self, shape_interface):
        shape_interface.square_draw()

    def square_draw(self):
        print("Drawing a square")


def main():
    # Circle örneği
    circle = Circle()
    circle.draw(circle)  # Circle kendi metodunu kullanır

    # Square örneği
    square = Square()
    square.draw(square)  # Square kendi metodunu kullanır


if __name__ == "__main__":
    main()
