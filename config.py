N = 100  # Number of fog nodes
M = 30 # Number of VMs in the cloud
TASK_SIZES = [8]  # in MB
ACTIVE_RATIOS = [0.8]  # Test with 0.5 for now
PROCESSING_DENSITY_FN = (10, 30)  # cycles/bit
CPU_FREQ_FN = (2.0, 3.0)  # GHz
PROCESSING_DENSITY_VM = (20, 40)  # cycles/bit
CPU_FREQ_VM = (2.0, 3.0)  # GHz
TRANSMISSION_RATE = (100, 500)  # Mbps
AREA_SIZE = (200, 200)  # meters
COVERAGE_RADIUS = 40  # meters
SIMULATION_TIME = 1000  # seconds
NUM_ROUNDS = 20  # Reduced for testing