# StokesMonteCarlo.py
# Author: bobse ()
# Created: 2022.02.21
# Description: Monte Carlo simulation of Stokes Theorem by Rhett Allain (https://www.youtube.com/watch?v=_X_X_X_X_X)
# ---------------------------------------------------------------------------------------------------------------------
GlowScript 3.0 VPython
#From the tutorial of the same name by Rhett Allain

N = 5000
R = 1
dr = 0.001
dA = .5*pi*R**2/N

def F(rr):
  return(vector(rr.y, -rr.x, rr.z))
  
def curlF(rr):
  return(vector(0,0,-2))

n=0
phi=0

while n < N:
  rt = R*vector(random(), random(), random())
  if (mag(rt) > R-dr and mag(rt)<R+dr):
    cylinder(pos=rt, axis=dr*norm(rt), radius=sqrt(dA/pi))
    dphi = dot( curlF(rt), norm(rt)*dA )
    phi = phi + dphi
    n = n + 1

print("Flux = ", phi)

ball = sphere(pos=vector(R,0,0), radius=0.04, color=color.yellow, make_trail=True)

# Calculate the Work
# initialize some variables
theta = 0
Np = 100
dtheta = .5 * pi/Np
W = 0
myrate = 100

# along x-y plane (z=0)
while theta <= .5 * pi:
  rate(myrate) # <myrate> frames a sec
  
  ball.pos=vector(cos(theta), sin(theta), 0) * R
  dr=vector(-sin(theta), cos(theta),0) * R * .5 * pi / Np
  
  dW = dot(F(ball.pos), dr)
  W = W + dW
  theta = theta + dtheta

print ("Work = ", W)

# along y-z plane (x=0)
theta = 0
while theta <= .5 * pi:
  rate(myrate) # <myrate> frames a sec
  
  ball.pos = vector(0, cos(theta), sin(theta)) * R
  dr = vector(0, -sin(theta), cos(theta)) * R * .5 * pi / Np
  
  dW = dot(F(ball.pos), dr)
  W = W + dW
  theta = theta + dtheta

print ("Work = ", W)

# along x-z plane (y=0)
theta = 0
while theta <= .5 * pi:
  rate(myrate) # <myrate> frames a sec
  
  ball.pos=vector(sin(theta), 0, cos(theta)) * R
  dr = vector(cos(theta), 0, -sin(theta)) * R * .5 * pi / Np
  
  dW = dot(F(ball.pos), dr)
  W = W + dW
  theta = theta + dtheta
  
  
print ("Work = ", W)
