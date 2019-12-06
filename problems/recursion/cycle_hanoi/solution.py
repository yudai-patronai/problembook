def chanoi(disc, start, other, finish):
    if disc == 1:
        if (3+start-finish) % 3 == 1:
            return [[1, start, other], [1, other, finish]]
        else:
            return [[1, start, finish]]
   
    else:
        
        if (3+start-finish) % 3 == 1:
            return chanoi(disc-1, start, other, finish)+[[disc, start, other]]+chanoi(disc-1, finish, other, start)+[[disc, other, finish]]+chanoi(disc-1, start, other, finish)
        else:
            return chanoi(disc-1, start, finish, other)+[[disc, start, finish]]+chanoi(disc-1, other, start, finish)
            

