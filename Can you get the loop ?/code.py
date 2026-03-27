def loop_size(node):
    turtle = node
    ferari = node
    
    while ferari and ferari.next:
        turtle = turtle.next
        ferari = ferari.next.next
        
        if turtle == ferari:
            count = 1
            turtle = turtle.next
            
            while turtle != ferari:
                turtle = turtle.next
                count += 1
                
            return count
            
    return 0
