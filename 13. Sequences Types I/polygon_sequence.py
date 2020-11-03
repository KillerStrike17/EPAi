from polygon import Polygon as pgn
from functools import lru_cache

class Polygon_seq:
    """
    This is a polygon sequence class used to develop a custom sequence
    """
    def __init__(self,no_edges:int, circumradius:int)->None:
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
        self.ratios = dict()
    
    def __repr__(self)->str:
        """
        This function is used to display the output of the class object.
        
        @params:
            None

        @returns:
            str - representation of the class
        """
        if bool(self.ratios):
            data = [f"{key}:{value}\n" for key,value in self.ratios.items()]
            dict_info =''.join(data)
        else:
            dict_info = "Empty Dictionary"
            
        stat = f"Total {self.no_edges} Polygons with circumradius as {self.circumradius}"
        return f"{stat}\n {dict_info}"

    def __len__(self)->int:
        """
        This function is returns the length i.e. no of veritices/edges
        
        @params:
            None

        @returns:
            int - no of edges
        """
        return self.no_edges
    
    def __getitem__(self, vertex:int)->float:
        """
        This function returns the generated sequence. It takes in number of vertex and returns a sequence 
        containing the ratio of of areaby perimeter

        @params:
            vertex: int - No of vertex

        @returns:
            Sequence - sequence containing the ratio
        """
        if isinstance(vertex, int):
            if vertex < 0:
                vertex = self.no_edges + vertex
            if vertex < 0 or vertex >= self.no_edges:
                raise IndexError
            else:
                if vertex>1:
                    return Polygon_seq._ratio(vertex,self.circumradius)
                else:
                    return 'it is not a polygon'
        else:
            raise IndexError
    @staticmethod
    @lru_cache(2 ** 10)
    def _ratio(no_edges:int,circumradius:int)->float:
        """
        This funcation returns the calculated ratio, Here we used the polygon class defined
        in objective 1 and fetch the area and perimeter property. Then the ratio is calculated and returned
        @params:
            no_edges: int - Number of vertices of the plygon
            circumradius: int - circumradius of the regular polygon.

        @returns:
            float - ratio of area is to perimeter
        """
        if no_edges < 2:
            return 1
        else:
            p1 = pgn(no_edges,circumradius)
            return p1.area/p1.perimeter
    
    @property
    def max_efficieny(self)->str:
        """
        This function calculates the maximum_efficieny and returns the string displaying the output

        @params:
            None

        @returns:
            float  - Calculated output
        """
        for i in range(self.no_edges):
            if i> 1:
                self.ratios[i+1] = self.__getitem__(i)
        key = max(self.ratios,key = self.ratios.get)
        return f"Max Ratio is {self.ratios[key]} at vertex {key}"