def find_roots(a, b, c):
    ax2 = a
    bx = b
    c = c
    delta = ((b**2)-4*ax2*c)*(1/2)
    if delta > 0:
      res = ((-b) + ((b**2)-4*ax2*c)*(1/2))/(2*a)
      res2 = ((-b) - ((b**2)-4*ax2*c)*(1/2))/(2*a)
      tupla = (res, res2)
    elif delta < 0 
      res = ((-b) + ((b**2)-4*ax2*c)*(1/2))/(2*a)
      tupla = res
    return tupla
    
  
    
    
    
    
    

print(find_roots(2, 10, 8));