class Engine(object):
    def __init__(self,name,bhp,rpm,volume,cylinders=4,type_='petrol'):
        self.name = name
        self.bhp = bhp
        self.rpm = rpm
        self.volume = volume
        self.cylinders = cylinders
        self.type_ = type_
    
    def start(self):
        print('Engine Started')

    def stop(self):
        print('Engine Stopped')

class Transmisison(object):
    def __init__(self, gears, torque):
        self.gears = gears
        self.torque = torque
        self.gear_pos = 0
    
    def shift_up(self):
        if self.gear_pos == self.gears:
            print('Can`t shift up anymore')
        else:
            self.gear_pos += 1
            print('Shifted up to gear', self.gear_pos)
    
    def shift_down(self):
        if self.gear_pos == -1:
            print("In reverse, Can`t shift down")
        else:
            self.gear_pos -=1
            print("Shifted down to gear", self.gear_pos)
    
    def shift_reverse(self):
        print('Reverse shifting')
        self.gear_pos = -1
    
    def shift_to(self, gear):
        self.gear_pos = gear
        print("Shifted to gear", self.gear_pos)

class Brake(object):
    def __init__(self, number, type_='disc'):
        self.type_ = type_
        self.number = number
    
    def engage(self):
        print('%s %d engaged' % (self.__class__.__name__, self.number))
    
    def release(self):
        print('%s %d released' % (self.__class__.__name__, self.number))
    
class ParkingBrake(Brake):
    def __init__(self, type_='drum'):
        super(ParkingBrake, self).__init__(type_=type_, number=1)

class Suspension(object):
    def __init__(self, load, type_='mcpherson'):
        self.type_ = type_
        self.load = load

class Wheel(object):
    def __init__(self, material, diameter, pitch):
        self.material = material
        self.diameter = diameter
        self.pitch = pitch
    
class WhieelAssembly(object):
    def __init__(self, brake, suspension):
        self.brake = brake
        self.suspention = suspension
        self.wheels = Wheel('alloy', 'M12', 1.25)
    
    def apply_blakes(self):
        print('Applying brakes')
        self.brake.engage()

class Frame(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Car(object):
    """ Facade Pattern"""
    def __init__(self, model, manufacturer):
        self.engine = Engine('Turbo',90,9000,1.3)
        self.frame = Frame(385,170)
        self.wheel_assemblies = [WhieelAssembly(Brake(i+1),Suspension(1000)) for i in range(4) ]
        self.transmisison = Transmisison(5,115)
        self.model = model
        self.manufacturer = manufacturer
        self.park_brake = ParkingBrake()
        self.ignition = False
    
    def start(self):
        print("Start the car")
        self.ignition = True
        self.park_brake.release()
        self.engine.start()
        self.transmisison.shift_up()
        print('Car started.')
    
    def stop(self):
        print('Stopping the car')
        for w_a in self.wheel_assemblies:
            w_a.apply_blakes()
        self.transmisison.shift_to(2)
        self.transmisison.shift_to(1)
        self.transmisison.shift_to(0)
        self.park_brake.engage()
        print('Car stopped')

if __name__ == '__main__':
    car = Car('StepWagon', 'Honda')
    car.start()
    car.stop()



        
    