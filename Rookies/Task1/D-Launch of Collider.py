number_of_particles = input() 
number_of_particles = int(number_of_particles)
event = input()  
particles = input()
particles = list(map(int, particles.split()))
def collision(number_of_particles , event , particles):
    min_time=1e10
    for i in range(number_of_particles-1):
        if event[i]=='R' and event[i+1] =='L':
            time=(particles[i+1]-particles[i])/2
            min_time=min(time, min_time)   
        
    if min_time == 1e10: return(-1)
    else:return(min_time)


result = int(collision(number_of_particles , event , particles))
print(result)



T