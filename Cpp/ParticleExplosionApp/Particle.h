#ifndef PARTICLE_H_
#define PARTICLE_H_


namespace sdlApp {

class Particle {
public:
    double x;
    double y;
    double speed_angle;
    double speed_value;
    double x_speed;
    double y_speed;

private:
    void init(double init_x, double init_y);

public:
    Particle();
    
    virtual ~Particle();
    void update(int interval); // updates particle position and color
};
}
#endif