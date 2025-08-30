from typing import TypedDict
from typing import Union
from typing import Optional
from typing import Any

class Movie(TypedDict):
    name: str
    year: int
   
   
movie=Movie(name="dark", year=2010)
# print(movie)



def square(x:Union[int,float])->float:
    return x*x

    
x=square(5)
# print(x)

def nice_messsage(name:Optional[str])->None:
    if name is None:
        print("Hello, Guest")
    else:
        print(f"Hello,{name}")
    
# nice_messsage("hemanth")


def print_value(x:Any):
    print(x)
    
# print_value([1,2,3])
# print_value({"name":"hemanth","age":22})
# print_value((1,2,3))        

nums=[1,2,3,4,5]


square=list(map(lambda x:x*x,nums))

print(square)