import math

class Polygon:
    """
    This is a polygon class which generated regular polygon of
    desired vertex and circumradius.
    """

    def __init__(self,no_edges:int,circumradius:int)->None:
        """
        This is a constructor

        @params:
            no_edges: int - Number of vertices of the plygon
            circumradius: int - circumradius of the regular polygon.
        
        @returns:
            None
        """
        self.no_edges = no_edges
        self.circumradius = circumradius
    
    def __repr__(self)->str:
        """
        This function is used to display the output of the class object.
        
        @params:
            None

        @returns:
            str - representation of the class
        """
        return f"Polygon with {self.no_edges} sides and {self.circumradius} as Circumradius"
    
    @property
    def interior_angle(self)->float:
        """
        This function calculates the interior angle based on the formula mentioned in the readme

        @params:
            None

        @returns:
            float  - Calculated output
        """
        return self.no_edges*(self.no_edges-2)/180
    
    @property
    def edge_length(self)->float:
        """
        This function calculates the edge length based on the formula mentioned in the readme

        @params:
            None

        @returns:
            float  - Calculated output
        """
        return 2*self.circumradius*math.sin(math.pi/self.no_edges)
    
    @property
    def apothem(self)->float:
        """
        This function calculates the apothem based on the formula mentioned in the readme

        @params:
            None

        @returns:
            float  - Calculated output
        """
        return self.circumradius*math.cos(math.pi/self.no_edges)
    
    @property
    def area(self)->float:
        """
        This function calculates the area based on the formula mentioned in the readme

        @params:
            None

        @returns:
            float  - Calculated output
        """
        return 0.5*self.apothem*self.edge_length * self.no_edges
    
    @property
    def perimeter(self)->float:
        """
        This function calculates the perimeter based on the formula mentioned in the readme

        @params:
            None

        @returns:
            float  - Calculated output
        """
        return self.no_edges * self.edge_length

    def __eq__(self, other:'Polygon class')->bool:
        """
        This class is to check equality. It checks the self.no_edges and self.circumradius with the ones
        of the other passed in as argument

        @params:
            other : Polygon Class - The class which is being checked

        @returns:
            bool  - True if equal else False
        """
        if not isinstance(other,Polygon):
            raise ValueError('Polygons must be compared with polygons and not with something else')
        return ((self.no_edges == other.no_edges) and (self.circumradius == other.circumradius))
    
    def __gt__(self, other:'Polygon class')->bool:
        """
        This class is to check greater than. It checks the self.no_edges and self.circumradius with the ones
        of the other passed in as argument

        @params:
            other : Polygon Class - The class which is being checked

        @returns:
            bool  - True if equal else False
        """
        if not isinstance(other,Polygon):
            raise ValueError('Polygons must be compared with polygons and not with something else')
        return self.no_edges > other.no_edges