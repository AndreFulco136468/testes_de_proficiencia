def find_roots(a, b, c):
    ax2 = a
    bx = b
    cx = c
    delta = ((bx**2)-4*ax2*cx)
    if delta >= 0:
      res = ((-bx) + ((bx**2)-4*ax2*cx)*(1/2))/(2*ax2)
      res2 = ((-bx) - ((bx**2)-4*ax2*cx)*(1/2))/(2*ax2)
      tupla = (res, res2)
    elif delta <= 0 :
      res = (-bx)/(2*ax2)
      tupla = res
    return tupla
    
  
    
    
    
    
    

print(find_roots(2, 10, 8));