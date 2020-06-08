#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """[summary]

    Args:
        Base ([type]): [description]
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """[summary]"""
            return self.__width

        @width.setter
        def width(self, var):
            if not isinstance(var, int):
                raise TypeError("width must be an integer")
            if var <= 0:
                raise ValueError("width must be > 0")
            self.__width = var

        @property
        def height(self):
            """[summary]"""
            return self.__height

        @height.setter
        def height(self, var):
            if not isinstance(var, int):
                raise TypeError("height must be an integer")
            if var <= 0:
                raise ValueError("height must be > 0")
            self.__height = var

        @property
        def x(self):
            """[summary]"""
            return self.__x

        @x.setter
        def x(self, var):
            if not isinstance(var, int):
                raise TypeError("x must be an integer")
            if var < 0:
                raise ValueError("x must be >= 0")
            self.__x = var

        @property
        def y(self):
            """[summary]"""
            return self.__y

        @y.setter
        def y(self, var):
            if not isinstance(var, int):
                raise TypeError("y must be an integer")
            if var < 0:
                raise ValueError("y must be >= 0")
            self.__y = var