# print("this one")
from Experiments.Navigate import *
from Behaviors.VRBall import *
from Stimuli.PandaVR import *


# define session parameters
session_params = {
    'trial_selection'        : 'staircase',
    'staircase_window'       : 10,
    'noresponse_intertrial'  : True,
    'max_reward'             : 2000,
    'bias_window'            : 5,
    'stair_up'               : 0.8,
    'stair_down'             : 0.5,
    'setup_conf_idx'         : 12,
}


exp = Experiment() 
exp.setup(logger, VRBall, session_params)
conditions = []

#I don't think these are used
non_resp = .1
scale = 2   #has to change every time the environment size changes - depending on the space the radii change
radius = 2**.5*(scale/2) - non_resp #peripou riza 

def_key = {
        'x_sz'                  : 18.8,
        'y_sz'                  : 18.8,
        'trial_duration'        : 6000000,
        'response_loc_x'        : (0.7, 1.7),
        'response_loc_y'        : (0.7, 1.7),
        'x0'                    : 0.0,
        'y0'                    : 0.0,
        'theta0'                : 0,
        'reward_loc_x'          : [0.7, 1.7],
        'reward_loc_y'          : [0.7, 1.7],
        'extiction_factor'      : 3,
        'radius'                : 0.2, # How close to the object you have to get to initiate reward process
        'reward_amount'         : 12    }

conditions += exp.make_conditions(stim_class=Panda(), conditions={**def_key,

                'background_color': (255/255, 80/255, 170/255),
                'ambient_color': (0.1, 0.1, 0.1, 1),
                'light_idx': (1, 2, 3),
                'light_color': (np.array([1, 1, 1, 1]), np.array([1, 1, 1, 1]), np.array([1, 1, 1, 1])),
                'light_dir': (np.array([0, -20, 0]), np.array([180, -20, 0]), np.array([0, -90, 0])),
                'obj_id': (5, 6, 4),
                'obj_pos_x': (1.8, 0.2, 1.8), 'obj_pos_y': (1.8, 1.8, 0.2), 
                'obj_mag': (0.01, 0.01, 0.01), 
                'obj_rot': (0), 'obj_tilt': 0, 'obj_yaw': 0,
                'rot_duration' : 2, # How long for a 360 rotation of the object
                'plane_id': 9,
                'plane_x' : 4, # x_dimension of plane
                'plane_y' : 4, # y_dimension of plane
                # The area of movement for the mouse ((0, xmx), (0, ymx)) will be set in the middle of the plane
                'xmx': 2, 
                'ymx': 2,     
                'movie_name_does_not_exist' : 'MadMax'
                                })

exp.push_conditions(conditions)
exp.start()
