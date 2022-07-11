import numpy as np

def convert_units(y_mm, s_mm, L_m, lam_nm):
    y_m = y_mm * 1e-3
    s_m = s_mm * 1e-3
    lam_m = lam_nm * 1e-9
    return y_m, s_m, L_m, lam_m

def r(y_in_m, s_in_m, L_in_m):
    return np.sqrt(L_in_m**2 + (y_in_m-s_in_m)**2)

def ComplexWave(r_in_m, lam_in_m):
    return np.exp(1j * 2 * np.pi * r_in_m / lam_in_m)

def DoubleSlitIntensity(y_in_mm, d_in_mm, L_in_m, lam_in_nm):
    y_m, d_m, L_m, lam_m = convert_units(y_in_mm, d_in_mm, L_in_m, lam_in_nm)
    
    total_wave = 0
    
    r_value = r(y_m, -d_m/2, L_m)
    total_wave = total_wave + ComplexWave(r_value, lam_m)
    
    r_value = r(y_m, d_m/2, L_m)
    total_wave = total_wave + ComplexWave(r_value, lam_m)
    
    return (np.abs(total_wave))**2

def convert_units2D(x_mm, y_mm, s_mm, L_m, lam_nm):
    x_m = x_mm * 1e-3
    y_m = y_mm * 1e-3
    s_m = s_mm * 1e-3
    lam_m = lam_nm * 1e-9
    return x_m, y_m, s_m, L_m, lam_m
    

def NIntensity2D(x_in_mm, y_in_mm, N):
    d_in_mm = 0.05
    L_in_m = 2
    lambda_in_nm = 400
    
    x_m, y_m, d_m, L_m, lam_m = convert_units2D(x_in_mm, y_in_mm, d_in_mm, L_in_m, lambda_in_nm)
    
    def r_2D(x_in_m, a_in_m, y_in_m, b_in_m):
        return np.sqrt(L_in_m**2 + ((x_in_m-a_in_m))**2 + ((y_in_m-b_in_m))**2)
    def ComplexWave(r,wv):
        return np.exp(1j * 2 * np.pi * r / wv)
    def hole_locations(N,d_in_m):
        a = np.zeros(N)
        b = np.zeros(N)
        for i in range(N):
            a[i] = d_in_m * np.cos(2 * np.pi * i / N)
            b[i] = d_in_m * np.sin(2 * np.pi * i / N)
        return a, b

    a, b = hole_locations(N,d_m)
    wave = 0
    for i in range(N):
        r = r_2D(x_m,a[i],y_m,b[i])
        wave = wave + ComplexWave(r, lam_m)
    return (np.abs(wave))**2