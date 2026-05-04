import math
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
     
    stride = image_size/feature_size
    box = []
    for i in range(feature_size):
        for j in range(feature_size):
            
            cx = (j+0.5) * stride
            cy = (i+0.5) * stride

            for s in scales:
                for r in aspect_ratios:
                    
                    w = s * math.sqrt(r)
                    h = s/math.sqrt(r)

                    x_min = cx-w/2
                    y_min = cy-h/2
                    x_max = cx+w/2
                    y_max = cy+h/2

                    box.append([x_min, y_min,x_max,y_max])

    return box

                    
        
