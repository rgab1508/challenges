def reverse(x: int) -> int:
    sx = str(x)
    n = False
    if sx.startswith("-"):
        sx = sx[1:]
        n =True
    rs = "".join(reversed(sx))
    
    while rs.startswith("0"):
        rs = rs[1:]
    
    if n:
        rs = '-' + rs
    
    return int(rs)

reverse(-321)